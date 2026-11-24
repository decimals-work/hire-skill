#!/usr/bin/env python3
"""pitch_check.py: measure a design job post (Stage 1 of the hire-a-designer skill).

Usage:  python3 pitch_check.py pitch.md        (or pipe the text in: ... | python3 pitch_check.py -)

What it checks (references/judges.md has the same list in plain words, for checking by hand):
  1. The opening. A designer gives a post 10 to 20 seconds. At an average reading speed of 238 words a minute
     (Brysbaert, 2019) that's about 40 to 80 words, so the first paragraph has to carry the pitch. Over 80 words
     is a WARN; over 120 (about 30 seconds, twice the time a designer gives it) is a FAIL.
  2. The hero. Sentences about the designer ("you", "your") against sentences about the company ("we", "our").
     The designer should be the hero, starting in the opening.
  3. Boilerplate: phrases that are true of every job post ("fast-paced", "rockstar", "competitive salary"...).
     Five or more is a FAIL. Calibrated on eight live design job posts against a blind reader (Nov 2026).
  4. Model tells: phrasing that reads machine-written ("delve", "in today's...", "not just X, but Y"). Dashes used as
     punctuation are counted as INFO only: plenty of people write that way.
  5. Pay: a visible pay range (two amounts, like "$150k to $175k" or "£70,000 - £85,000").
  6. The wish list: how many requirements there are. A role that needs everything has no spike.
Prints PASS, WARN, FAIL or INFO per check. Exits 1 if anything FAILs. Python standard library only.
"""
import re
import sys

WPM = 238

BOILERPLATE = [
    "fast-paced", "fast paced", "rockstar", "rock star", "ninja", "unicorn", "wear many hats", "self-starter",
    "self starter", "team player", "competitive salary", "competitive compensation", "competitive pay", "join our team",
    "we are looking for", "we're looking for", "the ideal candidate", "passionate about", "dynamic environment",
    "exciting opportunity", "detail-oriented", "detail oriented", "hit the ground running", "work hard play hard",
    "world-class", "world class", "best-in-class", "cutting-edge", "cutting edge", "thrive in ambiguity",
    "excellent communication skills", "strong communication skills", "attention to detail", "proven track record",
    "start-up environment", "startup environment", "other duties as assigned", "we're a family", "we are a family",
    "game-changing", "mission-driven", "revolutionizing", "revolutionising", "revolutionize", "revolutionise",
    "challenge the status quo", "make an impact", "we'd love to hear from you", "growth mindset", "culture of excellence",
    "cross-functionally", "comfort with ambiguity", "comfort navigating ambiguity", "comfortable with ambiguity",
    "shape the future", "shape what's next", "raise the bar", "join us", "level up", "trailblazer", "push the boundaries",
    "communication and collaboration skills", "collaboration and communication skills", "strong collaboration skills",
    "high bar for craft", "smart, resourceful", "close-knit", "make a difference", "at scale", "fast-growing",
    "fastest-growing", "driven by innovation", "proven experience", "navigate any scenario",
]
MODEL_TELLS = [
    "delve", "tapestry", "in today's", "ever-evolving", "ever evolving", "landscape", "leverage", "seamless",
    "robust", "elevate", "empower", "unlock", "harness", "embark", "realm", "testament", "pivotal", "synergy",
    "at the intersection of", "it's not just", "not just about", "whether you're", "paradigm", "distinctly",
]
NOT_JUST = re.compile(r"\b(not just|don't just|isn't just|aren't just)\b[^.]{0,80}?\b(but|it's|they're)\b", re.I)
WE = re.compile(r"\b(we|we're|we've|we'll|our|ours)\b|\bus\b", re.I)
YOU = re.compile(r"\b(you|you're|you've|you'll|your|yours)\b", re.I)
AMOUNT = r"[$£€]\s?\d[\d,.]*\s?[kKmM]?|\b\d{2,3}(?:[,.]\d{3})?\s?[kK]\b|\b\d{2,3}[,.]\d{3}\b"
PAY_RANGE = re.compile(rf"({AMOUNT}|\b\d{{2,3}})\s*(?:to|-|–|—|and)\s*({AMOUNT})", re.I)
PAY_WORD = re.compile(rf"\b(salary|base|pay|compensation|comp|per year|a year|OTE)\b[^.\n]{{0,40}}?({AMOUNT})|({AMOUNT})[^.\n]{{0,25}}\b(salary|base|per year|a year)\b|({AMOUNT})\s*/\s*(yr|year)\b", re.I)
REQ_HEAD = re.compile(r"^\s*(#+\s*)?\**\s*(requirements|(minimum |preferred |basic )?qualifications|what you(\W?ll| will| should)? (need|bring|have)|you have|must[- ]haves?( experience)?|about you|who you are|who we.re looking for|we.re looking for .{0,40}who|skills|bonus points|nice to have)\b", re.I)
REQ_INLINE = re.compile(r"(requirements|qualifications|you have|you'll need|must[- ]haves?)\s*:\s*([^\n]+)", re.I)
BULLET = re.compile(r"^\s*([-*•]|\d+[.)])\s+")

out, fails = [], 0


def report(level, name, detail):
    global fails
    fails += level == "FAIL"
    out.append(f"{level:4}  {name}: {detail}")


def strip_md(t):
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    return re.sub(r"[*_`>#]", "", t)


def sentences(t):
    return [s for s in re.split(r"(?<=[.!?])\s+|\n+", t) if len(s.split()) > 1]


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    src = sys.argv[1] if len(sys.argv) > 1 else "-"
    raw = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
    text = strip_md(raw)
    if len(text.split()) < 10:
        print("FAIL  post: the file is empty or too short to check")
        sys.exit(1)

    # 1. the opening: the first real paragraph (a lone title line doesn't count)
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    body = [p for p in paras if len(p.split()) > 8]
    long_ = [p for p in body if len(p.split()) >= 20]  # the opening is the first real paragraph, not a short subheading
    if long_ and body and len(body[0].split()) < 20:
        body = body[body.index(long_[0]):]
    opening = body[0] if body else paras[0]
    # one block: a single paragraph that is long, or that already runs into the requirements
    one_block = len(body) == 1 and (len(body[0].split()) > 80 or bool(REQ_INLINE.search(body[0])))
    if one_block:  # the whole post is one paragraph: the opening is what fits in 20 seconds
        opening = " ".join(opening.split()[:80])
    ow = len(opening.split())
    secs = ow / WPM * 60
    o_has_you = bool(YOU.search(opening))
    if one_block:
        report("WARN", "opening", "the post is one block of text, so there's no opening to speak of: give the pitch its own first paragraph")
    elif ow <= 80 and not o_has_you:
        report("WARN", "opening", f"{ow} words, about {secs:.0f} s to read, but it's about the company: a designer who stops here doesn't know what's in it for them")
    elif ow <= 80:
        report("PASS", "opening", f"{ow} words, about {secs:.0f} s to read")
    elif ow <= 120:
        report("WARN", "opening", f"{ow} words, about {secs:.0f} s: longer than the 10 to 20 seconds a designer gives it")
    else:
        report("FAIL", "opening", f"{ow} words, about {secs:.0f} s: it won't be read; cut it to what matters most")

    # 2. the hero, leaving out the legal and hiring-policy small print, which every post has
    legal = re.compile(r"equal opportunity|personal data|privacy|accommodation|EEO|background check|applicants? (with|from)|we may process", re.I)
    ss = [x for x in sentences(text) if not legal.search(x) and not x.rstrip().endswith(":")]
    we = sum(1 for s in ss if WE.search(re.sub(r"\bUS\b", "", s)) and not YOU.search(s))
    you = sum(1 for s in ss if YOU.search(s))
    os_ = sentences(opening)
    o_we = sum(1 for s in os_ if WE.search(re.sub(r"\bUS\b", "", s)) and not YOU.search(s))
    o_you = sum(1 for s in os_ if YOU.search(s))
    if o_you == 0 and o_we > 0 and we > you:
        level = "FAIL"
    elif o_you == 0:
        level = "WARN"
    elif you > we and o_you >= o_we:
        level = "PASS"
    else:
        level = "WARN"
    report(level, "hero", f"sentences about the designer {you}, about the company {we} (in the opening: {o_you} against {o_we})"
           + (": the opening doesn't mention the designer at all" if o_you == 0 else ""))

    # 3. boilerplate
    low = text.lower()
    bp = [p for p in BOILERPLATE if re.search(r"(?<![\w-])" + re.escape(p) + r"(?![\w-])", low)]
    report("PASS" if not bp else ("WARN" if len(bp) < 5 else "FAIL"), "boilerplate",
           "none found" if not bp else ", ".join(f'"{p}"' for p in bp))

    # 4. model tells; dashes used as punctuation, not bullets and not number ranges
    tells = [p for p in MODEL_TELLS if re.search(r"(?<![\w-])" + re.escape(p) + r"(?![\w-])", low)]
    if NOT_JUST.search(text):
        tells.append('"not just X, but Y"')
    lines = raw.splitlines()
    first = next((i for i, ln in enumerate(lines) if ln.strip()), 0)  # the title line: "Designer - Acme" is a separator
    prose = "\n".join(BULLET.sub("", ln) for i, ln in enumerate(lines) if i != first and not ln.lstrip().startswith("#"))
    prose = re.sub(rf"({AMOUNT}|\d)\s*[-–—]\s*({AMOUNT}|\d)", " ", prose)
    dashes = len(re.findall(r"—|\s[-–]{1,2}\s", prose))
    report("PASS" if not tells else ("WARN" if len(tells) < 3 else "FAIL"), "model tells",
           "none found" if not tells else ", ".join(tells))
    if dashes:  # plenty of people write with dashes: worth knowing, not a verdict
        out.append(f"INFO  dashes: {dashes} used as punctuation. Some readers take heavy dash use as a sign of machine writing")

    # 5. pay
    def is_pay(m):  # a range of plain numbers ("10,000 to 50,000 teams") is pay only with a currency, a k, or a pay word near it
        ctx = raw[max(0, m.start() - 40):m.end() + 25]
        return bool(re.search(r"[$£€]|\d\s?[kK]\b", m.group(0)) or re.search(r"\b(salary|base|pay|compensation|per year|a year|OTE)\b|/yr", ctx, re.I))
    rng = next((m for m in PAY_RANGE.finditer(raw) if is_pay(m)), None)
    word = PAY_WORD.search(raw)
    if rng:
        report("PASS", "pay range", f'found "{rng.group(0).strip()}"')
    elif word:
        report("WARN", "pay range", f'one amount found ("{word.group(0).strip()}"): a range tells a designer more')
    else:
        report("FAIL", "pay range", "no pay range found: put one in")

    # 6. the wish list: bullets under a requirements heading, or a "Requirements: a; b; c" line
    reqs, in_req = 0, False
    for line in raw.splitlines():
        if REQ_HEAD.search(strip_md(line)) and not REQ_INLINE.search(line):
            in_req = True
            continue
        if in_req and line.strip() and not BULLET.match(line):
            in_req = False  # the list ends at the next line that isn't a bullet
        if in_req and BULLET.match(line):
            reqs += 1
    for m in REQ_INLINE.finditer(raw):
        items = [i for i in re.split(r";|,(?![^()]*\))", m.group(2)) if i.strip()]
        reqs += len(items)
    if reqs:
        report("INFO", "wish list", f"{reqs} requirements. Which one or two are the spike? Lead with those; cut what any good designer has")

    print("\n".join(out))
    print("\nThe opening (the editor's test: would a designer who read only this know what the job is, and why it's for them?)\n  " + opening)
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
