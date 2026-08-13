from datetime import datetime, timezone
from pathlib import Path
import json


# ---------------------------------------------------------
# Project paths
# ---------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent

LOG_DIR = ROOT / "logs"
STATS_FILE = ROOT / "data" / "stats.json"


# ---------------------------------------------------------
# Create directories if necessary
# ---------------------------------------------------------

LOG_DIR.mkdir(parents=True, exist_ok=True)
STATS_FILE.parent.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------
# Current UTC date/time
# ---------------------------------------------------------

now = datetime.now(timezone.utc)

date_string = now.strftime("%Y-%m-%d")
time_string = now.strftime("%H:%M UTC")


# ---------------------------------------------------------
# Today's log file
# ---------------------------------------------------------

log_file = LOG_DIR / f"{date_string}.md"


# ---------------------------------------------------------
# Create today's log if it doesn't exist
# ---------------------------------------------------------

if not log_file.exists():

    content = f"""# Development Log — {date_string}

## Automated Activity

- Daily development log generated automatically.
- GitHub Actions workflow executed successfully.
- Repository maintenance completed.

## Manual Development Notes

Add the work you actually completed today.

### Tasks

- [ ] Add today's development task
- [ ] Update project documentation
- [ ] Review TODO items

### Projects Worked On

_Add your actual project work here._

### Problems Solved

_Add problems you solved today._

### Technologies Used

_Add technologies you worked with today._

### Notes

_Add any additional development notes here._

---

**Generated:** `{time_string}`

**Automation:** GitHub Actions
"""


    log_file.write_text(
        content,
        encoding="utf-8"
    )


# ---------------------------------------------------------
# Load existing statistics
# ---------------------------------------------------------

if STATS_FILE.exists():

    try:

        stats = json.loads(
            STATS_FILE.read_text(
                encoding="utf-8"
            )
        )

    except json.JSONDecodeError:

        stats = {}

else:

    stats = {}


# ---------------------------------------------------------
# Calculate number of development logs
# ---------------------------------------------------------

log_files = sorted(
    LOG_DIR.glob("*.md")
)


# ---------------------------------------------------------
# Update statistics
# ---------------------------------------------------------

stats["total_days"] = len(log_files)

stats["last_updated"] = date_string


# ---------------------------------------------------------
# Save statistics
# ---------------------------------------------------------

STATS_FILE.write_text(
    json.dumps(
        stats,
        indent=2
    ) + "\n",
    encoding="utf-8"
)


# ---------------------------------------------------------
# Console output
# ---------------------------------------------------------

print(
    f"Updated development log for {date_string}"
)

print(
    f"Total logged days: {stats['total_days']}"
)