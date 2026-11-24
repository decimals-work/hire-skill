# Stage 1: write the spec as a pitch

This is the first time someone's discovering the role, potentially the company. Don't waste a first impression with boilerplate descriptions.

You have about 10 to 20 seconds to make a pitch: make it about them. Why is this the role that's going to be transformational for their career? Make them the hero of your story.

**What it's for:** a job spec isn't a document. It's how you get a designer who has other options to want a conversation with you. Judge every line by whether it does that.

## Method

### 1. Get their words, then hand back the pen

Read `hire/role-brief.md`. Then ask the hiring manager about real things, not opinions, the way a user researcher would:

- "What will this person work on in their first month? Name the actual thing."
- "Why now? What changed?"
- "What will they be able to do here that they can't do where they are now?"
- "Who will they work with every day, and what's that person like to work with?"
- "What's hard about this job?"

Write down their exact phrases. Read the strongest three back to them: "You said this. That could be your opening." Then **they** write the draft, starting from `templates/pitch-skeleton.md` if a structure helps. You don't write it.

### 2. Make the designer the hero

The pitch answers one question: why is this the role that's going to be transformational for *their* career? The company, the funding and the mission matter only as reasons for that. A quick test on any draft: count the sentences about "we" and "our" against the sentences about "you" and "your". If the company wins, the designer isn't the hero yet. The pitch checker counts this for you.

10 to 20 seconds is about the first 40 to 80 words at an average reading speed. That opening has to say what the work is, why it matters to the designer and why now. Everything after it is detail for people who are already interested.

### 3. Be transparent about pay

Be as transparent as possible about compensation: it avoids wasting anyone's time. Put the range in the post.

### 4. Check what they'll see next

A designer who likes the pitch looks at your website next. If it looks like it was vibe-coded, you're signalling that you don't care about design. Pay a contractor if you need to.

### 5. Don't let a model write it

This includes you. If the hiring manager pastes in a model-written draft, say so kindly and ask the step 1 questions anyway. The output is average: precisely the opposite of what they should be aiming for.

## Borrowed from editors: the first paragraph test

An editor checks an opening by asking: if the reader stopped here, would they still know the story? Do the same. Show the hiring manager only the opening (the pitch checker prints it) and ask: "If a designer read only this, would they know what the work is, and why it's for them?" Then the editor's other habit: cut every sentence that would be true of any company ("fast-paced", "passionate team", "competitive salary").

## Pro-tip: a personal video

Some hiring managers go one step further: they create personalised videos for the designers they reach out to, telling them what they especially like about their portfolios. Suggest it for the designers the hiring manager most wants to reach.

## Checks

1. `scripts/pitch_check.py hire/pitch.md`: the opening, the hero, boilerplate, model tells, the pay range, the wish list. Fix every FAIL. Talk through the WARNs.
2. The first paragraph test above, with the hiring manager.
3. The cold read in `judges.md` ("Pitch").

## Hand over

`hire/pitch.md` in the hiring manager's words, the checker's output, the cold reader's answers, and a short list of what changed because of them.
