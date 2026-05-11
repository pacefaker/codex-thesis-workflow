from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass

from route_manifest import HANDOFFS, ROUTES, get_route


GOAL_TO_ROUTE = {
    "zh-to-en": "GTE-T-ZH2EN",
    "en-to-zh": "GTE-T-EN2ZH",
    "zh-to-zh": "GTE-T-ZH2ZH",
    "shorten": "GTE-R-SHORTEN",
    "expand": "GTE-R-EXPAND",
    "polish-zh": "GTE-R-POLISH-ZH",
    "polish-en": "GTE-R-POLISH-EN",
    "logic-check": "GTE-R-LOGIC",
    "experiment-analysis": "GTE-A-EXP",
    "reviewer-diagnosis": "GTE-A-REVIEW",
    "figure-title": "GTE-F-FIG-TITLE",
    "table-title": "GTE-F-TBL-TITLE",
    "architecture-figure": "GTE-F-ARCH",
    "plot-recommendation": "GTE-F-PLOT-RECOMMEND",
}


@dataclass
class Decision:
    decision: str
    route_id: str | None
    prompt_source: str | None
    prompt_snapshot_type: str | None
    handoff_skill: str | None
    reason: str


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Recommend a graduation-thesis-editor route.")
    parser.add_argument(
        "--goal",
        action="append",
        required=True,
        help="Atomic goal. Repeat the flag for mixed requests.",
    )
    parser.add_argument(
        "--has-draft",
        choices=["yes", "no"],
        required=True,
        help="Whether the task already has draft text or concrete material to edit.",
    )
    parser.add_argument(
        "--prefer-editor-deai",
        action="store_true",
        help="Use the editor's internal de-AI fallback instead of humanizer.",
    )
    parser.add_argument(
        "--target-language",
        choices=["chinese", "english"],
        default="chinese",
        help="Used only for de-AI routing.",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format.",
    )
    return parser


def decision_for_goal(goal: str, has_draft: str, prefer_editor_deai: bool, target_language: str) -> Decision:
    if goal in {"blank-page", "coauthoring", "chapter-plan", "chapter-drafting"} or has_draft == "no":
        handoff = HANDOFFS["GTE-H-DOC-COAUTHORING"]
        return Decision("handoff", None, None, None, handoff["handoff_skill"], handoff["reason"])

    if goal == "de-ai":
        if not prefer_editor_deai:
            handoff = HANDOFFS["GTE-H-HUMANIZER"]
            return Decision("handoff", None, None, None, handoff["handoff_skill"], handoff["reason"])
        route_id = "GTE-R-DEAI-LATEX" if target_language == "english" else "GTE-R-DEAI-WORD"
        route = get_route(route_id)
        return Decision("route", route_id, f"{route.source_file} :: {route.heading}", "public-safe summary", None, "Use the internal fallback de-AI route summary.")

    if goal not in GOAL_TO_ROUTE:
        raise ValueError(f"Unsupported goal: {goal}")

    route_id = GOAL_TO_ROUTE[goal]
    route = get_route(route_id)
    return Decision("route", route_id, f"{route.source_file} :: {route.heading}", "public-safe summary", None, route.use_when)


def render_text(decisions: list[Decision]) -> str:
    if len(decisions) == 1:
        item = decisions[0]
        if item.decision == "handoff":
            return "\n".join(
                [
                    "Decision: handoff",
                    f"Handoff Skill: {item.handoff_skill}",
                    f"Reason: {item.reason}",
                ]
            )
        return "\n".join(
            [
                "Decision: route",
                f"Route ID: {item.route_id}",
                f"Prompt Source: {item.prompt_source}",
                f"Prompt Snapshot Type: {item.prompt_snapshot_type}",
                f"Reason: {item.reason}",
            ]
        )

    lines = ["Decision: split", "Mixed Request: yes", "Ordered Steps:"]
    for index, item in enumerate(decisions, start=1):
        if item.decision == "handoff":
            lines.append(f"{index}. handoff -> {item.handoff_skill} ({item.reason})")
        else:
            lines.append(
                f"{index}. {item.route_id} -> {item.prompt_source} "
                f"(Prompt Snapshot Type: {item.prompt_snapshot_type})"
            )
    return "\n".join(lines)


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    decisions = [
        decision_for_goal(goal, args.has_draft, args.prefer_editor_deai, args.target_language)
        for goal in args.goal
    ]

    if args.format == "json":
        payload = {
            "mixed_request": len(decisions) > 1,
            "steps": [asdict(item) for item in decisions],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(render_text(decisions))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
