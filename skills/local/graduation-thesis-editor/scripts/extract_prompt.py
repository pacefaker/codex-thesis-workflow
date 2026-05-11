from __future__ import annotations

import argparse
import json
import sys

from route_manifest import canonical_prompt, get_route, prompt_hash


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extract a canonical prompt block by Route ID.")
    parser.add_argument("--route-id", required=True, help="Stable route id such as GTE-R-POLISH-ZH")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of plain text")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        route = get_route(args.route_id)
        prompt = canonical_prompt(args.route_id)
    except KeyError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    payload = {
        "route_id": route.route_id,
        "prompt_source": f"{route.source_file} :: {route.heading}",
        "prompt_hash_sha256": prompt_hash(args.route_id),
        "prompt": prompt,
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"Route ID: {payload['route_id']}")
        print(f"Prompt Source: {payload['prompt_source']}")
        print(f"Prompt Hash (SHA256): {payload['prompt_hash_sha256']}")
        print("Prompt Preserved Verbatim: yes")
        print()
        print(payload["prompt"], end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
