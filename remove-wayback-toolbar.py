#!/usr/bin/env python3

from sys import argv

begin = "<!-- BEGIN WAYBACK TOOLBAR INSERT -->"
end = "<!-- END WAYBACK TOOLBAR INSERT -->"

args = argv[1:]

for path in args:
    with open(path, "r") as f:
        newcontent = ""
        content = f.readlines()
        skipping = False
        for line in content:

            testline = line.strip()

            if testline == begin:
                skipping = True

            elif skipping and testline == end:
                skipping = False
                continue

            if skipping:
                continue

            #print(line)
            newcontent += line

    with open(path, "w") as f:
        print("Removing from {}".format(path))
        f.write(newcontent)
        #print(newcontent)

