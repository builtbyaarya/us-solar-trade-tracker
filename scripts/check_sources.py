#!/usr/bin/env python3
"""Twice-weekly change check. Fetches each URL in docs/watchlist.txt, hashes the visible text, and compares with
docs/watch-state.json. Prints CHANGED <url> for anything new and exits 0 with "NO CHANGE" when nothing moved, so the
scheduled updater can stop early. Only official pages are watched; the updater reads the changed pages by hand.
Usage: python3 scripts/check_sources.py [--save]   (--save records the new hashes after a successful update)"""
import hashlib, json, re, sys, urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WATCH = ROOT / "docs" / "watchlist.txt"
STATE = ROOT / "docs" / "watch-state.json"
UA = {"User-Agent": "us-solar-trade-tracker/1.0 (+https://github.com/builtbyaarya/us-solar-trade-tracker)"}


def text_of(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read().decode("utf-8", "ignore")
    raw = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S | re.I)
    txt = re.sub(r"<[^>]+>", " ", raw)
    txt = re.sub(r"\s+", " ", txt)
    # drop obvious timestamps / counters that change every visit
    txt = re.sub(r"\b\d{1,2}:\d{2}(:\d{2})?\b", "", txt)
    return txt


def main():
    save = "--save" in sys.argv
    urls = [l.strip() for l in WATCH.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    changed, errors = [], []
    for u in urls:
        try:
            h = hashlib.sha256(text_of(u).encode("utf-8")).hexdigest()
        except Exception as e:  # noqa: BLE001
            errors.append(f"{u}: {e}")
            continue
        if state.get(u, {}).get("hash") != h:
            changed.append(u)
            if save:
                state[u] = {"hash": h, "checked": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        elif save:
            state[u]["checked"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    if save:
        STATE.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    for u in changed:
        print("CHANGED", u)
    for e in errors:
        print("ERROR", e)
    if not changed and errors and len(errors) == len(urls):
        print("UNKNOWN: every fetch failed (no network, or the pages block scripts); read the watchlist by hand")
    elif not changed:
        print("NO CHANGE")


if __name__ == "__main__":
    main()
