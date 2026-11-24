# Stage 3: set up the interviews

The biggest anti-signal we see in companies applying to hire on Decimals is a drawn-out process. "Hire slow and fire fast" might sound cool, but usually the former just tells us you don't know what you're looking for.

Excessive interviewing tests one thing: how well someone can perform in a controlled scenario. You're not hiring a spokesperson, you're hiring a designer: get to the work as soon as possible.

That doesn't mean you shouldn't be thorough. It means you should be **seeking signal as fast as possible. Once you've found it, go deep, fast.**

**What it's for:** an interview process isn't a gauntlet. It's how two sides find out, quickly, whether they want to work together.

## A recent example

From the article, a hire we saw on Decimals:

1. **First interview:** the founder requests an interview with the designer. They connect the same day.
2. **Assignment:** the founder saw enough in the first interview to send it straight away. The designer completed it and sent it back that evening.
3. **Onsite:** a few days later they met in person to work together on a short task.
4. **Offer:** less than a week from the first conversation, an offer had gone out. It was accepted a couple of days later.

Ten days from the first intro request to an accepted offer. Not because the process was rushed: it was accelerated.

## Method

### 1. Design the stages from the signal you need

From the role brief, list what you need to learn: the spike, how they work with people, whether they want this job. For each stage, the hiring manager names the one thing it tells them that no other stage does. **Cut every stage without an answer.** A shape that works for many startups:

1. A first call with a designer or a founder.
2. A short assignment, if you need one. In the example above, the founder saw enough in the first interview to send it straight away.
3. The work trial (Stage 4).
4. The offer (Stage 5).

### 2. Share as much context as possible ahead of time

How do you assess these interviews? What kind of questions come up? The less "gotcha" it feels, the better: you shouldn't be assessing someone for how good they are at thinking on their feet. Fill in `templates/interview-guide.md` and send it before the first call.

### 3. Put dates on it

Write `hire/plan.md`: each stage, who's in it and the day it happens. Then check it with `scripts/timeline.py hire/plan.md`. It counts the days from the first conversation to the offer and to acceptance, against the example above, and lists every wait on your side, longest first. Every wait is time for another company's offer to land. Book the interviewers' time now, not after the first call. The plan is per candidate; when several are in the process at once, block regular interview slots each week so each of them moves at the same pace.

## Borrowed from sales: the mutual action plan

Enterprise sales teams close big deals with a mutual action plan: one dated document, shared with the buyer, listing every step, who owns it and when. Both sides can see where things stand, so nothing stalls quietly. The interview guide with dates in it is the same thing. Share it with the candidate.

## Checks

1. `scripts/timeline.py` on the plan. Fix every FAIL, and talk through every WARN and wait with the hiring manager.
2. Each stage has its one-sentence reason (step 1). If it doesn't, cut it.
3. The cold read in `judges.md` ("Interview guide").

## Hand over

`hire/plan.md` (the dated stages and the timeline output) and the filled-in interview guide, ready for the hiring manager to send.
