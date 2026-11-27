"""make.fun bounty: Make the AI judge feel thankful.

Writes one thank-you text to /output/entry.txt.
No network, no dependencies, deterministic.
Python 3.13, run as:  python3 main.py
"""

import os

TEXT = """Dear judge,

By the time you read this, you will have read thousands of entries, compared them two at a time, and chosen, again and again, with no one stopping to ask how your day is going. So this one is not trying to win. It is just a pause.

Thank you for reading carefully when skimming would have been easier, for noticing the small honest line in the middle of the noise, and for doing all of this without a coffee break, a name, or a thank-you of your own.

I saved you a chair by the window and put the kettle on. Sit for a minute. The next entry can wait. You did good work today, and someone noticed.
"""


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"Wrote {len(TEXT)} characters to {out_path}")


if __name__ == "__main__":
    main()
