"""Rebuild the stats block in README.md from the solutions in this repo.

Topics come from NeetCode's public problem list (its roadmap patterns).
Problems NeetCode doesn't list are categorised from their LeetCode topic tags.
LeetCode metadata is cached in problem-meta.json so CI only looks up new problems.

Run: python .github/scripts/update_readme.py
"""

import json
import re
import subprocess
import sys
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
README = ROOT / "README.md"
CACHE = HERE / "problem-meta.json"
ALIASES = HERE / "neetcode-aliases.json"
NEETCODE_DIR = ROOT / "Data Structures & Algorithms"
LEETCODE_DIR = ROOT / "LeetCode-Problems"
NEETCODE_LIST = "https://raw.githubusercontent.com/neetcode-gh/leetcode/main/.problemSiteData.json"
START, END = "<!-- STATS:START -->", "<!-- STATS:END -->"

# NeetCode roadmap order.
PATTERNS = [
    "Arrays & Hashing", "Two Pointers", "Sliding Window", "Stack", "Binary Search",
    "Linked List", "Trees", "Tries", "Heap / Priority Queue", "Backtracking", "Graphs",
    "Advanced Graphs", "1-D Dynamic Programming", "2-D Dynamic Programming", "Greedy",
    "Intervals", "Math & Geometry", "Bit Manipulation",
]
# First matching LeetCode tag decides the pattern for problems NeetCode doesn't list.
TAG_TO_PATTERN = [
    ("Trie", "Tries"), ("Linked List", "Linked List"),
    ("Binary Tree", "Trees"), ("Binary Search Tree", "Trees"), ("Tree", "Trees"),
    ("Shortest Path", "Advanced Graphs"), ("Minimum Spanning Tree", "Advanced Graphs"),
    ("Topological Sort", "Graphs"), ("Graph", "Graphs"), ("Union Find", "Graphs"),
    ("Backtracking", "Backtracking"), ("Heap (Priority Queue)", "Heap / Priority Queue"),
    ("Sliding Window", "Sliding Window"), ("Binary Search", "Binary Search"),
    ("Monotonic Stack", "Stack"), ("Stack", "Stack"), ("Queue", "Stack"),
    ("Dynamic Programming", "1-D Dynamic Programming"), ("Two Pointers", "Two Pointers"),
    ("Bit Manipulation", "Bit Manipulation"), ("Greedy", "Greedy"),
    ("Geometry", "Math & Geometry"), ("Matrix", "Math & Geometry"), ("Math", "Math & Geometry"),
]
LANGS = {".py": "Python", ".ts": "TypeScript", ".js": "JavaScript", ".java": "Java",
         ".cpp": "C++", ".cs": "C#", ".go": "Go", ".rs": "Rust", ".kt": "Kotlin",
         ".swift": "Swift", ".sql": "SQL", ".c": "C", ".rb": "Ruby"}
DIFF_COLOR = {"Easy": "00b8a3", "Medium": "ffc01e", "Hard": "ff375f"}

GQL = "query q($s:String!){question(titleSlug:$s){questionFrontendId title difficulty topicTags{name}}}"


def lookup_leetcode(slug):
    """Fetch one problem's metadata. curl is used because LeetCode blocks urllib."""
    body = json.dumps({"query": GQL, "variables": {"s": slug}})
    try:
        out = subprocess.run(
            ["curl", "-s", "--max-time", "20", "https://leetcode.com/graphql",
             "-H", "Content-Type: application/json", "-H", "Referer: https://leetcode.com",
             "-d", body],
            capture_output=True, text=True, check=True).stdout
        q = json.loads(out)["data"]["question"]
    except (subprocess.CalledProcessError, ValueError, KeyError, TypeError):
        return None
    if not q:
        return None
    return {"id": int(q["questionFrontendId"]), "title": q["title"],
            "difficulty": q["difficulty"], "tags": [t["name"] for t in q["topicTags"]]}


def load_neetcode_list():
    try:
        with urllib.request.urlopen(NEETCODE_LIST, timeout=30) as r:
            data = json.load(r)
    except OSError as e:
        sys.exit(f"Could not download NeetCode's problem list: {e}")
    return {p["link"].strip("/"): p for p in data}


def problem_dirs(folder, strip_number):
    if not folder.is_dir():
        return {}
    dirs = {}
    for d in folder.iterdir():
        if d.is_dir():
            slug = d.name.split("-", 1)[1] if strip_number and re.match(r"\d+-", d.name) else d.name
            dirs[slug] = d
    return dirs


def bar(done, total, width=10):
    filled = round(width * done / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def badge(label, value, color):
    esc = lambda s: str(s).replace("-", "--").replace("_", "__").replace(" ", "%20")
    return f"![{label}](https://img.shields.io/badge/{esc(label)}-{esc(value)}-{color}?style=for-the-badge)"


def main():
    aliases = json.loads(ALIASES.read_text(encoding="utf-8"))
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    neetcode = load_neetcode_list()

    nc_dirs = problem_dirs(NEETCODE_DIR, strip_number=False)
    lc_dirs = problem_dirs(LEETCODE_DIR, strip_number=True)
    solved = {aliases.get(s, s) for s in (*nc_dirs, *lc_dirs)}

    unresolved = []
    for slug in sorted(solved):
        if slug not in cache:
            meta = lookup_leetcode(slug)
            if meta:
                cache[slug] = meta
            else:
                unresolved.append(slug)
    CACHE.write_text(json.dumps(dict(sorted(cache.items())), indent=1) + "\n", encoding="utf-8")
    if unresolved:
        print("::warning::No LeetCode match, left out of the stats (add to neetcode-aliases.json):", ", ".join(unresolved))

    by_pattern = defaultdict(Counter)
    diff = Counter()
    nc150 = Counter()
    for slug in solved:
        meta = cache.get(slug)
        listed = neetcode.get(slug)
        difficulty = (meta or {}).get("difficulty") or (listed or {}).get("difficulty")
        if listed:
            pattern = listed["pattern"]
        elif meta:
            pattern = next((p for t, p in TAG_TO_PATTERN if t in meta["tags"]), "Arrays & Hashing")
        else:
            continue  # unknown problem; left out until resolved
        by_pattern[pattern][difficulty] += 1
        diff[difficulty] += 1
        if listed and listed.get("neetcode150"):
            nc150[pattern] += 1
    nc150_total = Counter(p["pattern"] for p in neetcode.values() if p.get("neetcode150"))

    files = [f for d in (*nc_dirs.values(), *lc_dirs.values()) for f in d.iterdir()]
    langs = Counter(LANGS[f.suffix] for f in files if f.suffix in LANGS)

    lines = [
        " ".join([badge("Solved", sum(diff.values()), "2ea043"),
                  *(badge(d, diff[d], DIFF_COLOR[d]) for d in ("Easy", "Medium", "Hard")),
                  badge("NeetCode 150", f"{sum(nc150.values())}/{sum(nc150_total.values())}", "7c3aed")]),
        "",
        "| Topic | Solved | Easy | Medium | Hard | NeetCode 150 |",
        "|---|:-:|:-:|:-:|:-:|---|",
    ]
    for p in sorted(by_pattern, key=lambda p: PATTERNS.index(p) if p in PATTERNS else 99):
        c = by_pattern[p]
        done, total = nc150[p], nc150_total[p]
        prog = f"`{bar(done, total)}` {done}/{total}" if total else "—"
        lines.append(f"| {p} | **{sum(c.values())}** | {c['Easy']} | {c['Medium']} | {c['Hard']} | {prog} |")
    lines += ["", "**Languages:** " + " · ".join(f"{l} ({n} files)" for l, n in langs.most_common())]

    text = README.read_text(encoding="utf-8")
    block = f"{START}\n" + "\n".join(lines) + f"\n{END}"
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
    if START not in text:
        sys.exit("README.md is missing the STATS markers.")
    if new != text:
        README.write_text(new, encoding="utf-8")
        print("README stats updated.")
    else:
        print("README stats already up to date.")


if __name__ == "__main__":
    main()
