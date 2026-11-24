# Audit mode: is your hiring process ready?

Ten yes or no questions, two per stage. They're the checklist at the end of the article. The difference here: every answer needs **evidence**, such as the real job post, the real process and the last offer. A hiring manager's memory of their own process is less reliable than the documents.

## The questions

| Stage | Question | Evidence to ask for |
|---|---|---|
| The spec | Is the designer the hero of your pitch? | The live job post. Run `scripts/pitch_check.py` on it. |
| The spec | Is the pay range there for them to see? | The live job post. |
| The shortlist | Are you shortlisting on the work alone? | How recent applicants were screened, and by whom. |
| The shortlist | Can designers easily play with your product? | The product URL. Try to get in without talking to anyone. |
| The interviews | Is the first call with a designer or founder? | The process, or the last candidate's invitations. |
| The interviews | Do candidates know what's coming at every stage? | What you send candidates before the first call. |
| The work trial | Is it paid, at least a full day? | The last trial brief, and what was paid. |
| The work trial | Does it leave room for real disagreement? | The last trial brief, and how the day ran. |
| The offer | Can you go to the top of your pay range, or above? | The approved range, and who can change it. |
| The offer | Do you know what you can offer beyond salary? | The list, if there is one. |

Also ask for the dates of the last hire. "The first conversation" is the first conversation anyone from the company had with the candidate (an agency screen counts). If there was no offer, add a line for the day the candidate dropped out (call it "Dropped out" or "Took another offer"). Run `scripts/timeline.py` on them.

## How to run it

1. Ask for all the evidence in one message (the list above), then collect it. Open links yourself if you can.
2. Mark each question **yes**, **partly** or **no**, with one line of evidence. If you couldn't see the evidence, write "unverified", not "yes".
3. Say what's already working, with the evidence. Then score it plainly: the number of yeses out of ten, and the days from the first conversation to an offer (or to losing the candidate).
4. Pick the **three** changes that would help most, from the evidence. Weigh how much each one is costing them now (a lost candidate, a week of unpaid work, a pile screened on logos) against how quick it is to fix. Explain each in one sentence.
5. Offer to run the stage behind each of the three.

## Hand over

`hire/audit.md`: the ten answers with evidence, the score, the three changes and the next step.
