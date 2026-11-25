import os

# One funny line, max 200 chars: the tool built to remember
# everything forgets the one thing it exists to remember.
ENTRY = "My password manager forgot my password, so now we're both locked out of my life."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
path = out_dir + "/entry.txt"
with open(path, "w", encoding="utf-8") as f:
    # No trailing newline: the entry is exactly one line.
    f.write(ENTRY)
