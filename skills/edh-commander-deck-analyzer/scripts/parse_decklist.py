#!/usr/bin/env python3
"""Parse Commander/EDH decklists for counts, commanders, duplicates, and rough sections.

This script intentionally does not verify oracle data or legality. Use Scryfall/current web data
for color identity, bans, and legalities.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

BASIC_LANDS = {"Plains", "Island", "Swamp", "Mountain", "Forest", "Wastes"}
HEADER_RE = re.compile(r"^\s*(//\s*)?([A-Z][A-Z\s/]+|COMMANDER|MAINDECK|SIDEBOARD|MAYBEBOARD)\s*$", re.I)
QTY_RE = re.compile(r"^\s*(?:SB:\s*)?(?:(\d+)x?\s+)?(.+?)\s*$", re.I)
SET_CODE_RE = re.compile(r"\s+\([A-Z0-9]{2,6}\)\s*\d+[a-zA-Z]*.*$")
ARENA_RE = re.compile(r"\s+\[[A-Z0-9]{2,6}:\d+[a-zA-Z]*\].*$")


def clean_name(raw: str) -> str:
    raw = raw.strip()
    raw = re.sub(r"^\d+x?\s+", "", raw, flags=re.I)
    raw = SET_CODE_RE.sub("", raw)
    raw = ARENA_RE.sub("", raw)
    raw = raw.split(" #", 1)[0].strip()
    raw = raw.replace("’", "'")
    return raw


def parse_lines(text: str):
    section = "main"
    commanders = []
    cards = []
    ignored = []

    for line_no, line in enumerate(text.splitlines(), 1):
        raw = line.strip()
        if not raw:
            if section == "commander" and commanders:
                section = "main"
            continue
        if raw.startswith("#"):
            continue
        lower = raw.lower()
        if lower.startswith("// commander") or lower in {"commander", "commander:"}:
            section = "commander"
            continue
        if lower.startswith("// sideboard") or lower.startswith("sideboard") or lower.startswith("sb:"):
            if lower.startswith("sb:"):
                section = "sideboard"
            else:
                section = "sideboard"
                continue
        elif lower.startswith("// maybeboard") or lower.startswith("maybeboard"):
            section = "maybeboard"
            continue
        elif lower.startswith("//") or HEADER_RE.match(raw):
            section = raw.strip("/ ").lower()
            continue

        m = QTY_RE.match(raw)
        if not m:
            ignored.append({"line": line_no, "text": raw})
            continue
        qty = int(m.group(1) or 1)
        name = clean_name(m.group(2))
        if not name:
            ignored.append({"line": line_no, "text": raw})
            continue
        item = {"qty": qty, "name": name, "section": section, "line": line_no}
        if section == "commander":
            commanders.append(item)
        elif section not in {"sideboard", "maybeboard"}:
            cards.append(item)

    return commanders, cards, ignored


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("deckfile", type=Path)
    parser.add_argument("--json", action="store_true", help="emit JSON instead of text")
    args = parser.parse_args()

    text = args.deckfile.read_text(encoding="utf-8")
    commanders, cards, ignored = parse_lines(text)

    counts = Counter()
    for item in commanders + cards:
        counts[item["name"]] += item["qty"]

    duplicates = {name: qty for name, qty in counts.items() if qty > 1 and name not in BASIC_LANDS}
    total = sum(counts.values())

    by_section = defaultdict(int)
    for item in commanders + cards:
        by_section[item["section"]] += item["qty"]

    result = {
        "total_cards_including_commanders": total,
        "commander_count": sum(i["qty"] for i in commanders),
        "commanders": commanders,
        "main_count": sum(i["qty"] for i in cards),
        "duplicates_excluding_basic_lands": duplicates,
        "section_counts": dict(by_section),
        "ignored_lines": ignored,
    }

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"Total cards including commanders: {total}")
        print(f"Commanders: {', '.join(i['name'] for i in commanders) or 'none found'}")
        print(f"Main count: {result['main_count']}")
        if duplicates:
            print("Duplicates excluding basic lands:")
            for name, qty in sorted(duplicates.items()):
                print(f"  {qty} {name}")
        if ignored:
            print("Ignored lines:")
            for item in ignored:
                print(f"  line {item['line']}: {item['text']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
