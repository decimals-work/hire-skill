#!/usr/bin/env python3
"""Regression tests for the two scripts: python3 tests/run_tests.py (from the repo root). Standard library only.
Each case is a made-up input and the verdicts it must get. They cover the bugs found while testing the skill."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skills" / "hire-a-designer" / "scripts"


def run(script, text):
    r = subprocess.run([sys.executable, str(SCRIPTS / script), "-"], input=text, capture_output=True, text=True)
    return r.stdout


PITCH = [
    ("good post", "# Founding designer\n\nYou'd own how 40,000 small-business owners see their money each morning. Right now that screen is a spreadsheet, and customers tell us it scares them. Your first month: redesign it with them, then ship it. Pay: $160k to $190k base.\n\nYou'll work every day with our CTO.\n",
     ["PASS  opening", "PASS  hero", "PASS  boilerplate", "PASS  pay range"]),
    ("boilerplate post", "# Senior Product Designer\n\nWe are a fast-paced, world-class startup on a mission to revolutionize healthcare. We're looking for a passionate, self-starter designer to join our team and wear many hats. Competitive salary.\n",
     ["FAIL  hero", "FAIL  boilerplate", "FAIL  pay range"]),
    ("funding is not pay", "# Designer\n\nYou'll design how teams plan their week, with our founders beside you every day. We raised $20M and serve 10,000 to 50,000 teams.\n",
     ["FAIL  pay range"]),
    ("short and pound ranges", "# Designer\n\nYou'll design how teams plan their week, with our founders beside you every day.\n\nSalary: 95-120k EUR, or £70,000 to £85,000 in London.\n",
     ["PASS  pay range"]),
    ("bullets are not dashes", "# Designer\n\nYou'll design how teams plan their week, with our founders beside you every day.\n\nWhat you'll bring:\n- Figma\n- Taste\n- Shipped work\n\nSalary: $150,000 - $175,000\n",
     ["INFO  wish list: 3", "PASS  model tells"]),
    ("US is not us", "# Designer\n\nYou'll lead design for teams across the US and Europe, working with you and your peers every day on what customers see first. Pay: $150k to $170k.\n",
     ["PASS  hero"]),
    ("empty", "", ["FAIL  post"]),
]
TIMELINE = [
    ("fast plan", "- First call: day 0\n- Assignment back (candidate): day 0\n- Onsite: day 4\n- Offer: day 6\n- Accepted (candidate): day 8\n",
     ["PASS  time to offer: 6", "PASS  time to acceptance: 8"]),
    ("words are not dates", "| Stage | Who | When |\n|---|---|---|\n| First call | Head of design | Mon 30 Nov 2026 |\n| Debrief | 2 decision makers; mark 3 things | Fri 4 Dec 2026 |\n| Offer | CEO | Mon 7 Dec 2026 |\n",
     ["day   4  Debrief", "time to offer: 7"]),
    ("year rollover", "- First chat: Mon 28 Dec 2026\n- Work trial: Mon 4 Jan\n- Offer: Wed 6 Jan\n", ["time to offer: 9"]),
    ("screen is the start", "- Recruiter screen: 2026-12-01\n- First interview: 2026-12-08\n- Offer: 2026-12-11\n", ["time to offer: 10"]),
    ("lost hire", "- Agency screen: 2026-10-05\n- CEO call: 2026-10-12\n- Candidate took another offer: 2026-11-16\n", ["INFO  lost", "day 42"]),
    ("notes and output are skipped", "- First call: day 0\n- Note: if the trial slips to day 9 we tell them\n- Offer: day 5\nPASS  time to offer: 5 days\n", ["PASS  time to offer: 5"]),
]

fails = 0
for script, cases in (("pitch_check.py", PITCH), ("timeline.py", TIMELINE)):
    for name, text, expect in cases:
        out = run(script, text)
        missing = [e for e in expect if e not in out]
        fails += bool(missing)
        print(("ok  " if not missing else "FAIL") + f"  {script}: {name}" + (f"  (missing {missing})" if missing else ""))
print(f"\n{fails} failing" if fails else "\nall passing")
sys.exit(1 if fails else 0)
