# Outside reads

You don't grade your own work, and the hiring manager can't read their own pitch the way a stranger does. Stages 1 to 5 end with two kinds of check: an **instrument** (a script that measures) and a **cold read** (a reader who sees only the artefact).

## How to run a cold read

The cold reader gets **only** the artefact and the brief below: not the conversation, not the role brief, not your opinion of the draft.

- **In Claude Code, or anywhere with subagents:** start a subagent and give it the artefact and the brief, nothing else.
- **In Claude.ai or the apps:** give the hiring manager one block to copy, with the brief and the artefact already inside it, and ask them to paste it into a new chat **outside** the Claude Project for this hire (a chat inside the Project can see the role brief, so it isn't cold). Then ask them to paste the answer back here.
- **The Pitch and Interview guide briefs can also go to a person**, such as a designer the hiring manager knows. The Shortlist and Offer briefs contain candidates' details: only ever run those with a fresh model, never by sending them outside the company.

Show the hiring manager the reader's answers word for word, then say what you'd change and ask what they'll change. Don't argue the reader out of what they felt. After the changes, run the cold read once more.

Each brief describes the job the real reader does, so the reader does that job and reports, rather than playing a character.

## Pitch

> Read the job post below the way a senior product designer decides whether to reply to one: on your phone, with other offers and a full-time job, giving it 15 seconds. Read only what you would read in that time, then stop.
> Report: 1) the line where you stopped, 2) what you remember about the job, in one sentence, 3) whether you'd reply (yes or no) and the one reason, 4) any phrase that made it sound like every other job post, or written by a model, 5) whether you know what it pays.

## Shortlist

> Below is a shortlist: each candidate, a decision and the evidence for it, and the one or two things the role needs most (the spike). For each decision, say whether the evidence points at specific work, and whether it's about the spike or about something else (logos, years, schools, polish). List any decision you couldn't explain to the candidate.

## Interview guide

> Below is a guide a designer has been sent before a first interview. You know nothing else about the company. Report: who you'll meet at each stage, how long it takes in total, what you'd prepare, what it pays and where it is, and anything that could still surprise you on the day. Mark each one "clear" or "I'd have to ask".

## Work trial

> Below is a brief for a paid work trial. Read it as a strong designer with other offers deciding whether to do it. Report: whether you'd say yes, what you'd expect to learn about working there, whether any of it feels like free work, and what's missing that you'd want to know first.

## Offer

> Below is what a candidate said matters most to them in their next job, and the offer a company plans to make (leave out the company's walk-away point). For each priority, say whether the offer answers it, partly answers it or ignores it. Then name the one change that would make it an easy yes.

## Instruments

The scripts are in `scripts/`, next to `SKILL.md`. Both use only the Python standard library. If you can't run code, apply the same checks by hand:

**`pitch_check.py <post>`**
- The opening: the first paragraph of 20 words or more (skip the title and short subheadings). Is it 80 words or fewer (about 20 seconds of reading)? Does it mention the designer ("you")? Is the post more than one block of text?
- The hero: are there more sentences about "you" than about "we", "our" and "us"? Does the opening mention the designer at all? FAIL when the opening talks about the company but not the designer, and the post as a whole is more about the company.
- Boilerplate (five or more is a FAIL): "fast-paced", "fast paced", "rockstar", "rock star", "ninja", "unicorn", "wear many hats", "self-starter", "self starter", "team player", "competitive salary", "competitive compensation", "competitive pay", "join our team", "we are looking for", "we're looking for", "the ideal candidate", "passionate about", "dynamic environment", "exciting opportunity", "detail-oriented", "detail oriented", "hit the ground running", "work hard play hard", "world-class", "world class", "best-in-class", "cutting-edge", "cutting edge", "thrive in ambiguity", "excellent communication skills", "strong communication skills", "attention to detail", "proven track record", "start-up environment", "startup environment", "other duties as assigned", "we're a family", "we are a family", "game-changing", "mission-driven", "revolutionizing", "revolutionising", "revolutionize", "revolutionise", "challenge the status quo", "make an impact", "we'd love to hear from you", "growth mindset", "culture of excellence", "cross-functionally", "comfort with ambiguity", "comfort navigating ambiguity", "comfortable with ambiguity", "shape the future", "shape what's next", "raise the bar", "join us", "level up", "trailblazer", "push the boundaries", "communication and collaboration skills", "collaboration and communication skills", "strong collaboration skills", "high bar for craft", "smart, resourceful", "close-knit", "make a difference", "at scale", "fast-growing", "fastest-growing", "driven by innovation", "proven experience", "navigate any scenario".
- Model tells: "delve", "tapestry", "in today's", "ever-evolving", "ever evolving", "landscape", "leverage", "seamless", "robust", "elevate", "empower", "unlock", "harness", "embark", "realm", "testament", "pivotal", "synergy", "at the intersection of", "it's not just", "not just about", "whether you're", "paradigm", "distinctly", and "not just X, but Y". Dashes used as punctuation are worth noting, not a verdict.
- Pay: is there a range, with two amounts?
- The wish list: how many requirements, and which are the spike?
- Counting by hand is approximate. Say so when you report the numbers.

**`timeline.py <plan>`**
- Days from the first conversation to the offer and to acceptance, against the article's example: an offer out in less than a week, accepted 10 days after the first intro request.
- Every wait where the candidate is waiting on the company, longest first.
- Stages on a weekend, and stages with no date.
- For a past hire that was lost ("Dropped out", "Took another offer"), the day it was lost.
