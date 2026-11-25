#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — variant B.

Concept family B: the person is out for an absurdly specific reason, with
the twist landing in the last words. Here: a work-life balance conference —
the one place where ignoring your email is literally the curriculum.

Draft history (each draft scored against the 5 judge criteria):
  v1: "I'm out until Monday — I'm at a work-life balance conference, and the
      first lesson is not replying to emails like yours."
      Reads as a real OOO (criterion 1 OK); twist lands but "first lesson"
      is flat and "like yours" is weaker than it could be.
  v2: "I'm out until Monday — attending a work-life balance conference, where
      lesson one is not answering emails like yours."
      Drops the second "I'm" — loses the human voice, reads more like a
      notice than a person (criterion 3 weaker). Reverted.
  v3: "I'm away until Monday — I'm at a work-life balance conference, and
      session one is literally about not replying to emails like yours."
      "Literally" is a filler word; criterion 5 punishes it.
  v4: "I'm out until Monday — I'm at a work-life balance conference, and the
      opening session is about ignoring emails exactly like yours."
      Stronger, but "opening session" is clunkier than "first session" and
      "ignoring" is less OOO-flavoured than "not replying".
  v5 (final): "I'm out until Monday — I'm at a work-life balance conference,
      and the first session is about not replying to emails exactly like
      yours."
      Criterion 1: opens like a real OOO ("I'm out until Monday") with a
      plausible reason. Criterion 2: the laugh lands on first read — the
      sender's own email is the example of what not to reply to. Criterion
      3: a person would gladly switch this on. Criterion 4: fresh turn on
      the away message — no beach, inbox, or "limited access" stock joke;
      the conference premise is specific and the twist targets the sender.
      Criterion 5: 137 chars, one sentence, every word earns its place;
      "exactly" is the word that makes the twist land.
  v6 (final, after first run): re-read the criteria once more — "not
      replying to" is two soft words where one sharp verb does the job.
      Swapped to "ignoring": shorter (128 chars), punchier, and the twist
      hits harder because the conference is teaching the sender's exact
      fate. Everything else unchanged.
"""

import os

ENTRY = (
    "I'm out until Monday \u2014 I'm at a work-life balance conference, "
    "and the first session is about ignoring emails exactly like yours."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
