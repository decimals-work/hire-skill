#!/usr/bin/env python3
"""timeline.py: check a design hiring plan's dates (Stage 3 of the hire-a-designer skill).

Usage:  python3 timeline.py plan.md

One stage per line, as a list item, a table row or "Stage: when". "When" is a date (2026-12-01, 1 Dec, Dec 1,
Tue 1 Dec 2026) or a day count from the first conversation (day 0, day 3). Lines starting with "Note" are skipped.
    - First call: day 0
    - Assignment back (candidate): day 1
    - Onsite work trial: day 4
    - Offer: day 6
    - Accepted (candidate): day 8
The first conversation is the earliest stage where someone from the company talks to the candidate (a call, a
screen, an interview, a chat or an intro, an agency screen included); otherwise the first stage. The offer is the stage named "offer" ("Offer", "Offer call", "Make the offer").
A stage named "Dropped out", "Lost", "Withdrew" or "Took another offer" ends a past hire that didn't land (audit mode).
Mark stages where the time is the candidate's, not yours, with "(candidate)", or name them "... back" or "Accepted".

What it checks (references/judges.md has the same list in plain words, for checking by hand):
  1. Days from the first conversation to the offer and to acceptance, against the example in the article: an offer
     out less than a week after the first conversation, accepted 10 days after the first intro request.
  2. Every wait where the candidate is waiting on you, longest first (in working days when the plan has dates).
  3. Stages on a weekend, dates whose weekday doesn't match, and stages with no date.
Prints PASS, WARN, FAIL or INFO per check. Exits 1 if anything FAILs. Python standard library only.
"""
import re
import sys
from datetime import date, timedelta

MONTHS = {m: i + 1 for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split())}
ISO = re.compile(r"\b(20\d\d)-(\d\d)-(\d\d)\b")
MON = r"(jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\.?"
DMY = re.compile(rf"\b(\d{{1,2}})(?:st|nd|rd|th)?\s+{MON}(?![a-z])(?:,?\s+(20\d\d))?\b", re.I)
MDY = re.compile(rf"\b{MON}(?![a-z])\s+(\d{{1,2}})(?:st|nd|rd|th)?\b(?:,?\s+(20\d\d))?", re.I)
DAY = re.compile(r"\bday\s*(\d+)\b", re.I)
STAGE_WORDS = re.compile(r"(call|interview|trial|assignment|take-?home|on-?site|offer|accept|meet|chat|review|round|panel|screen|presentation|intro)", re.I)
START = re.compile(r"\b(call|conversation|interview|chat|intro|screen)", re.I)
WEEKDAY = re.compile(r"\b(mon|tue|wed|thu|fri|sat|sun)[a-z]*\b", re.I)
OFFER = re.compile(r"^(make (the |an )?)?offer\b|\boffer (call|sent|made|out|letter)\b", re.I)
LOST = re.compile(r"\b(dropped out|withdrew|withdrawn|lost|declined|took another offer)\b", re.I)
CANDIDATE = re.compile(r"\(candidate\)|\bback\b|\breturned\b|\baccept", re.I)


def parse_date(s):
    if m := ISO.search(s):
        return date(*map(int, m.groups()))
    if m := DMY.search(s):
        d, mon, y = m.groups()
        return date(int(y) if y else date.today().year, MONTHS[mon[:3].lower()], int(d))
    if m := MDY.search(s):
        mon, d, y = m.groups()
        return date(int(y) if y else date.today().year, MONTHS[mon[:3].lower()], int(d))
    return None


def working_days(a, b):
    n, d = 0, a
    while d < b:
        d += timedelta(days=1)
        n += d.weekday() < 5
    return n


def stage_lines(text):
    when_col = None
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or re.match(r"^\|?[\s:|-]+\|?$", s):
            continue
        if re.match(r"^(([-*•]|\d+[.)])\s+)?(\*\*)?note\b", s, re.I) or re.match(r"^(PASS|WARN|FAIL|INFO)\b", s):
            continue
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if cells and cells[0].lower() in ("stage", "step", "#"):
                low = [c.lower() for c in cells]
                when_col = next((i for i, c in enumerate(low) if c in ("when", "date", "day", "date and time")), None)
                continue
            src = cells[when_col] if when_col is not None and when_col < len(cells) else s
            yield re.sub(r"[*_`]", "", cells[0]).strip(), src, True
        elif re.match(r"^([-*•]|\d+[.)])\s+", s) or re.match(r"^[^:]{2,60}:\s*\S", s):
            listed = bool(re.match(r"^([-*•]|\d+[.)])\s+", s))
            body = re.sub(r"^([-*•]|\d+[.)])\s+", "", s)
            name = re.split(r":\s|\s[-–]\s", body, maxsplit=1)[0]
            if len(name.split()) > 8:
                continue  # a sentence, not a stage name
            yield re.sub(r"[*_`]", "", name).strip(), s, listed


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    text = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 and sys.argv[1] != "-" else sys.stdin.read()
    stages, undated, wrongday, last = [], [], [], None
    for name, line, listed in stage_lines(text):
        rest = line[line.find(name) + len(name):] if name in line else line
        when = parse_date(rest) or parse_date(line)
        k = DAY.search(rest) or DAY.search(line)
        if when:
            if last and isinstance(last, date) and not re.search(r"20\d\d", rest + line) and (last - when).days > 180:
                when = when.replace(year=when.year + 1)  # "Mon 4 Jan" after "Mon 28 Dec": next year
            wd = WEEKDAY.search(rest)
            if wd and wd.group(1)[:3].lower() != f"{when:%a}".lower():
                wrongday.append((name, wd.group(0), when))
            stages.append((name, when))
            last = when
        elif k:
            stages.append((name, int(k.group(1))))
        elif listed and STAGE_WORDS.search(name):
            undated.append(name)

    if len(stages) < 2:
        print("FAIL  plan: fewer than two dated stages found. Give each stage a date (1 Dec, or 2026-12-01) or a day count (day 3).")
        sys.exit(1)
    kinds = {type(v) for _, v in stages}
    if len(kinds) > 1:
        print("FAIL  plan: mixes dates and day counts. Use one or the other.")
        sys.exit(1)
    dated = date in kinds

    talks = [i for i, (n, _) in enumerate(stages) if START.search(n)]
    si = min(talks, key=lambda i: stages[i][1]) if talks else 0
    start = stages[si][1]
    span = (lambda v: (v - start).days) if dated else (lambda v: v - start)
    fails, out = 0, []

    def report(level, name, detail):
        nonlocal fails
        fails += level == "FAIL"
        out.append(f"{level:4}  {name}: {detail}")

    print("The plan (days from the first conversation):")
    for name, v in stages:
        extra = f"  ({v:%a %d %b})" if dated else ""
        print(f"  day {span(v):>3}  {name}{extra}")
    print()

    lost = next(((n, v) for n, v in stages if LOST.search(n)), None)
    if lost:
        out.append(f'INFO  lost: "{lost[0]}" on day {span(lost[1])} from the first conversation')
    offer = next(((n, v) for n, v in stages if OFFER.search(n) and not LOST.search(n)), None)
    if offer:
        d = span(offer[1])
        report("PASS" if d < 7 else "WARN", "time to offer", f"{d} days from the first conversation"
               + ("" if d < 7 else ". In the article's example the offer went out less than a week after the first conversation"))
    elif not lost:
        report("WARN", "time to offer", 'no stage named "Offer": add it, with a date, so the plan has an end')
    acc = next(((n, v) for n, v in stages if re.search(r"accept", n, re.I)), None)
    if acc:
        d = span(acc[1])
        report("PASS" if d <= 10 else "WARN", "time to acceptance", f"{d} days from the first conversation"
               + ("" if d <= 10 else ". In the article's example the offer was accepted 10 days after the first intro request"))

    waits = []
    for (n1, v1), (n2, v2) in zip(stages, stages[1:]):
        g = working_days(v1, v2) if dated else v2 - v1
        if (v2 - v1).days < 0 if dated else v2 < v1:
            report("FAIL", "order", f'"{n2}" comes before "{n1}"')
        elif g > 0 and not CANDIDATE.search(n2) and not LOST.search(n2):
            waits.append((g, n1, n2))
    unit = lambda g: ("working day" if dated else "day") + ("" if g == 1 else "s")
    for g, n1, n2 in sorted(waits, reverse=True):
        out.append(f'INFO  wait on you: {g} {unit(g)} between "{n1}" and "{n2}". Can it be sooner? If not, say why in the guide')
    for n, wd, v in wrongday:
        report("WARN", "date", f'"{n}" says {wd}, but {v:%d %b %Y} is a {v:%A}')
    if dated:
        for n, v in stages:
            if v.weekday() >= 5:
                report("WARN", "weekend", f'"{n}" is on a {v:%A}')
    if undated:
        report("WARN", "undated", ", ".join(f'"{u}"' for u in undated) + ": give these dates")

    print("\n".join(out))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
