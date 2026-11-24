# Hire a designer

A skill for Claude that runs a designer hire with you, from "we need a designer" to an accepted offer.

The best designers end up with multiple offers. This skill rebuilds your hiring process around that: a job spec written as a pitch, a shortlist made on the work, a fast interview loop with no surprises, a paid work trial with real friction, and an offer that lands.

It's a coach, not a ghostwriter. It won't write your job post for you, because a pitch written by a model reads like every other job post. It gets your own words out of you, checks what you write, and tells you what to cut.

## What it does

| Stage | What you get |
|---|---|
| The role brief | The one or two things this designer must be exceptional at, in your words |
| 1. Write the spec as a pitch | Your job post, checked: the opening, who the hero is, boilerplate, the pay range |
| 2. Shortlist on the work | A shortlist with evidence from the work, and a product designers can try |
| 3. Set up the interviews | A dated plan, checked for waits, and a guide to send candidates before the first call |
| 4. Set up a work trial | A paid trial brief with a real problem and room for real disagreement |
| 5. Land the offer | An offer plan built on what the candidate cares about, beyond salary |
| Audit | Ten yes or no questions with evidence, a score, and the three changes to make first |

Each stage ends with an outside read: a cold read by someone (or a fresh model) who sees only what you wrote, plus a small script for the pitch and the interview plan.

## Install

**Claude Code**

```
/plugin marketplace add decimals-work/hire-skill
/plugin install hire-a-designer@decimals
```

Or copy it in yourself:

```
git clone https://github.com/decimals-work/hire-skill
cp -r hire-skill/skills/hire-a-designer ~/.claude/skills/
```

**Claude.ai and the Claude apps**

Download `hire-a-designer.zip` from the [latest release](https://github.com/decimals-work/hire-skill/releases/latest), then go to Settings, Capabilities, Skills, and upload it. Skills need code execution turned on (Settings, Capabilities). On a Team or Enterprise plan, an admin may need to turn skills on first.

Tip: keep each hire in its own Claude Project, so the role brief is there in every chat.

## Use it

Ask Claude something like:

- "We need to hire our first designer. Help me."
- "Here's our job post for a senior product designer: [link]. Is it any good?"
- "I've got 60 applicants for a designer role. Help me shortlist."
- "What should our design work trial look like?"
- "We want to make an offer to a designer. Help me plan it."
- "Is our design hiring process any good?"

## Tests

`python3 tests/run_tests.py` checks the two scripts against the cases found while testing the skill. The pitch checker was also calibrated on eight live design job posts against a blind reader.

## Where it comes from

The tips are from "Use this skill to hire your next designer", an article on X by Danny Martinez, co-founder of Decimals. Decimals is a scout network for hiring designers: working designers introduce designers whose work they rate. It has been placing designers at startups for over a year. [decimals.co](https://decimals.co)
