from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Route:
    route_id: str
    source_file: str
    heading: str
    kind: str
    use_when: str
    avoid_when: str


ROUTES: dict[str, Route] = {
    "GTE-T-ZH2EN": Route(
        "GTE-T-ZH2EN",
        "references/translation.md",
        "中转英",
        "route",
        "Translate Chinese notes or prose into English LaTeX.",
        "Do not use for Chinese polishing.",
    ),
    "GTE-T-EN2ZH": Route(
        "GTE-T-EN2ZH",
        "references/translation.md",
        "英转中",
        "route",
        "Translate English LaTeX or prose into Chinese.",
        "Do not use for blank-page drafting.",
    ),
    "GTE-T-ZH2ZH": Route(
        "GTE-T-ZH2ZH",
        "references/translation.md",
        "中转中",
        "route",
        "Rewrite rough Chinese notes into cleaner Chinese prose.",
        "Do not use for explicit logic review or reviewer diagnosis.",
    ),
    "GTE-R-SHORTEN": Route(
        "GTE-R-SHORTEN",
        "references/revision.md",
        "缩写",
        "route",
        "Compress an existing passage without changing meaning.",
        "Do not use for expansion or diagnosis.",
    ),
    "GTE-R-EXPAND": Route(
        "GTE-R-EXPAND",
        "references/revision.md",
        "扩写",
        "route",
        "Expand an existing passage with small, evidence-preserving additions.",
        "Do not use for full chapter drafting.",
    ),
    "GTE-R-POLISH-EN": Route(
        "GTE-R-POLISH-EN",
        "references/revision.md",
        "表达润色（英文论文）",
        "route",
        "Polish English thesis or paper prose.",
        "Do not use for Chinese passages.",
    ),
    "GTE-R-POLISH-ZH": Route(
        "GTE-R-POLISH-ZH",
        "references/revision.md",
        "表达润色（中文论文）",
        "route",
        "Polish existing Chinese thesis prose.",
        "Do not use for reviewer-style diagnosis or blank-page drafting.",
    ),
    "GTE-R-LOGIC": Route(
        "GTE-R-LOGIC",
        "references/revision.md",
        "逻辑检查",
        "route",
        "Check consistency, logic gaps, and fatal wording problems.",
        "Do not use for reviewer-style whole-chapter reports.",
    ),
    "GTE-R-DEAI-LATEX": Route(
        "GTE-R-DEAI-LATEX",
        "references/revision.md",
        "去 AI 味（内部 fallback）",
        "route",
        "Internal fallback for English LaTeX de-AI cleanup.",
        "Prefer humanizer when possible.",
    ),
    "GTE-R-DEAI-WORD": Route(
        "GTE-R-DEAI-WORD",
        "references/revision.md",
        "去 AI 味（内部 fallback）",
        "route",
        "Internal fallback for Chinese thesis de-AI cleanup.",
        "Prefer humanizer when possible.",
    ),
    "GTE-A-EXP": Route(
        "GTE-A-EXP",
        "references/analysis.md",
        "实验分析",
        "route",
        "Analyze experiment metrics, tables, or summaries.",
        "Do not use for general prose polishing.",
    ),
    "GTE-A-REVIEW": Route(
        "GTE-A-REVIEW",
        "references/analysis.md",
        "论文整体以 Reviewer 视角进行审视",
        "route",
        "Provide reviewer-style diagnosis of a substantial section, chapter, or paper.",
        "Do not use for local line edits.",
    ),
    "GTE-F-ARCH": Route(
        "GTE-F-ARCH",
        "references/figures.md",
        "论文架构图",
        "route",
        "Generate a thesis architecture-diagram brief or wording.",
        "Do not use for plain titles only.",
    ),
    "GTE-F-PLOT-RECOMMEND": Route(
        "GTE-F-PLOT-RECOMMEND",
        "references/figures.md",
        "实验绘图推荐",
        "route",
        "Recommend figure forms for experiment results.",
        "Do not use when the user only needs a title or caption.",
    ),
    "GTE-F-FIG-TITLE": Route(
        "GTE-F-FIG-TITLE",
        "references/figures.md",
        "生成图的标题",
        "route",
        "Generate a figure title or figure-caption wording.",
        "Do not use for table titles.",
    ),
    "GTE-F-TBL-TITLE": Route(
        "GTE-F-TBL-TITLE",
        "references/figures.md",
        "生成表的标题",
        "route",
        "Generate a table title or table-caption wording.",
        "Do not use for figure titles.",
    ),
}


HANDOFFS = {
    "GTE-H-DOC-COAUTHORING": {
        "handoff_skill": "doc-coauthoring",
        "reason": "Blank-page drafting, chapter planning, or staged coauthoring belongs to doc-coauthoring.",
    },
    "GTE-H-HUMANIZER": {
        "handoff_skill": "humanizer",
        "reason": "Explicit final de-AI cleanup belongs to humanizer unless the user requires the fallback prompt inside graduation-thesis-editor.",
    },
}


def get_route(route_id: str) -> Route:
    if route_id not in ROUTES:
        raise KeyError(f"Unknown route id: {route_id}")
    return ROUTES[route_id]


def get_handoff(route_id: str) -> dict[str, str]:
    if route_id not in HANDOFFS:
        raise KeyError(f"Unknown handoff id: {route_id}")
    return HANDOFFS[route_id]


def load_section_text(source_file: str, heading: str) -> str:
    path = SKILL_ROOT / source_file
    lines = path.read_text(encoding="utf-8").splitlines()
    marker = f"## {heading}"

    try:
        start = next(index for index, line in enumerate(lines) if line.strip() == marker)
    except StopIteration as exc:
        raise KeyError(f"Heading not found: {marker} in {path}") from exc

    end = len(lines)
    for index in range(start + 1, len(lines)):
        if lines[index].startswith("## "):
            end = index
            break

    section = "\n".join(lines[start:end]).strip() + "\n"
    return section


def canonical_prompt(route_id: str) -> str:
    route = get_route(route_id)
    return load_section_text(route.source_file, route.heading)


def prompt_hash(route_id: str) -> str:
    return sha256(canonical_prompt(route_id).encode("utf-8")).hexdigest()
