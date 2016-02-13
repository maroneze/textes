#!/usr/bin/env python

# Strips timing information, and concatenates lines of one or several subtitles
# until a "-" is found. Tries to split dialogues between characters.
# Requires manual post-processing.

from __future__ import print_function
import sys
import re

if len(sys.argv) < 2:
    print("usage: %s file.srt" % sys.argv[0])
    sys.exit(1)

with open(sys.argv[1]) as f:
    lines = f.readlines()
    i = 0
    while i < len(lines):
        if re.search('\d+ --> \d+', lines[i]):
            # Next line(s) contain text
            separator = "" # no separator before first line
            while i < len(lines) and lines[i].strip():
                i += 1
                if re.match("- ", lines[i]):
                    print()
                if lines[i].strip():
                    print(' ' + lines[i].strip(), end="")
                    separator = " " # space for subsequent lines
        i +=1
