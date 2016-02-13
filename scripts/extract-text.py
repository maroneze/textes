#!/usr/bin/env python

# Strips timing information and concatenates the lines of a same subtitle,
# but does not concatenate lines from different subtitles.

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
                if lines[i].strip():
                    print(separator + lines[i].strip(), end="")
                    separator = " " # space for subsequent lines
            print()
        i +=1
