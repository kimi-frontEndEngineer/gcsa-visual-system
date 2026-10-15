#!/usr/bin/env python3
"""Generate a portable GCSA visual-direction brief from the bundled catalog."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


SURFACES = ("marketing", "console", "mobile", "asset")
TASKS = ("design", "review", "refactor", "component")


def load_catalog() -> dict:
    catalog_path = Path(__file__).resolve().parent.parent / "data" / "catalog.json"
    return json.loads(catalog_path.read_text(encoding="utf-8"))


def select_signal(catalog: dict, product: str) -> tuple[str, dict]:
    normalized = product.casefold()
    best_name = "default"
    best_score = 0
    for name, signal in catalog["signals"].items():
        if name == "default":
            continue
        score = sum(1 for keyword in signal["keywords"] if keyword.casefold() in normalized)
        if score > best_score:
            best_name, best_score = name, score
    return best_name, catalog["signals"][best_name]


def build_recommendation(catalog: dict, surface_name: str, task_name: str, product: str) -> dict:
    signal_name, signal = select_signal(catalog, product)
    surface = catalog["surfaces"][surface_name]
    return {
        "brief": {
            "product": product or "GCSA product",
            "surface": surface_name,
            "task": task_name,
            "matched_signal": signal_name,
        },
        "visual_thesis": signal["thesis"],
        "goal": surface["goal"],
        "brand_foundation": catalog["base"]["brand"],
        "semantic_colors": catalog["base"]["tokens"],
        "composition": surface["composition"],
        "visual_motifs": signal["motifs"],
        "theme_strategy": surface["theme"],
        "task_actions": catalog["tasks"][task_name],
        "accessibility": catalog["base"]["accessibility"],
        "avoid": signal["avoid"],
        "validation": surface["validation"],
    }


def markdown(data: dict) -> str:
    brief = data["brief"]
    lines = [
        f"# GCSA Visual Direction — {brief['product']}",
        "",
        f"- Surface: `{brief['surface']}`",
        f"- Task: `{brief['task']}`",
        f"- Matched signal: `{brief['matched_signal']}`",
        "",
        "## Visual thesis",
        "",
        data["visual_thesis"],
        "",
        "## Goal",
        "",
        data["goal"],
    ]
    sections = (
        ("Brand foundation", "brand_foundation"),
        ("Composition", "composition"),
        ("Visual motifs", "visual_motifs"),
        ("Theme strategy", "theme_strategy"),
        ("Task actions", "task_actions"),
        ("Accessibility", "accessibility"),
        ("Avoid", "avoid"),
        ("Validation", "validation"),
    )
    for title, key in sections:
        lines.extend(["", f"## {title}", ""])
        lines.extend(f"- {item}" for item in data[key])
    lines.extend(["", "## Semantic colors", ""])
    lines.extend(f"- `{name}`: `{value}`" for name, value in data["semantic_colors"].items())
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a GCSA visual-direction recommendation.")
    parser.add_argument("--surface", choices=SURFACES, required=True)
    parser.add_argument("--task", choices=TASKS, default="design")
    parser.add_argument("--product", default="", help="Product, industry, and capability keywords.")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    args = parser.parse_args()

    recommendation = build_recommendation(load_catalog(), args.surface, args.task, args.product)
    if args.format == "json":
        print(json.dumps(recommendation, ensure_ascii=False, indent=2))
    else:
        print(markdown(recommendation), end="")


if __name__ == "__main__":
    main()
