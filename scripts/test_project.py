from pathlib import Path
import json
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent

SCRIPT = ROOT / "scripts" / "update_log.py"

STATS_FILE = ROOT / "data" / "stats.json"

LOG_DIR = ROOT / "logs"


print("Running Daily Developer Log tests...")
print()


# ---------------------------------------------------------
# Test 1 — Run update script
# ---------------------------------------------------------

print("[1/4] Running update_log.py...")

subprocess.run(
    [
        sys.executable,
        str(SCRIPT)
    ],
    check=True
)

print("PASS")
print()


# ---------------------------------------------------------
# Test 2 — Check stats file
# ---------------------------------------------------------

print("[2/4] Checking stats.json...")

if not STATS_FILE.exists():

    raise RuntimeError(
        "stats.json was not created."
    )

print("PASS")
print()


# ---------------------------------------------------------
# Test 3 — Validate JSON
# ---------------------------------------------------------

print("[3/4] Validating statistics...")

with open(
    STATS_FILE,
    "r",
    encoding="utf-8"
) as file:

    stats = json.load(file)


assert "total_days" in stats

assert "last_updated" in stats

assert stats["total_days"] >= 1


print("PASS")
print()


# ---------------------------------------------------------
# Test 4 — Check daily log
# ---------------------------------------------------------

print("[4/4] Checking development logs...")

logs = list(
    LOG_DIR.glob("*.md")
)


if len(logs) == 0:

    raise RuntimeError(
        "No development logs were generated."
    )


print(
    f"PASS — {len(logs)} log(s) found."
)

print()

print("All tests passed successfully!")