#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
    print("usage: %s file.srt" % sys.argv[0])
    sys.exit(1)

warnings = 0
with open(sys.argv[1]) as f:
    lines = f.readlines()
    prev_time = 0
    prev_time_str = "<NONE>"
    for line in lines:
        words = line.split()
        for word in words:
            if ':' in word and len(word) > 1 :
                (hours_str, mins_str, secs_str) = word.split(':')
                hours = int(hours_str)
                mins = int(mins_str)
                secs_str, milli_str = secs_str.split(',')
                secs = int(secs_str)
                milli = int(milli_str)
                time = milli + secs * 1000 + mins * 60*1000 + hours * 60*60*1000
                if time < prev_time:
                    print("WARNING: %s < %s !" % (word, prev_time_str))
                    warnings += 1
                else:
                    prev_time = time
                    prev_time_str = word

print("%d problem(s) found." % warnings)
