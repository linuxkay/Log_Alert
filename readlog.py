#!/usr/bin/env/python
#this python program read log file. Notify when specific word found n time

infile = r"/tmp/access.log"

important = []
keep_phrases = ["POST /wp-login.php",
              "important",
              "keep me"]

with open(infile) as f:
    f = f.readlines()
seen = set()
dups = set()
for line in f:
    #for phrase in keep_phrases:
    for word in f:
        #if phrase in line:
        if word in seen:
            if word not in dups:
                print(word)
                dups.add(word)
        else:
            seen.add(word)
            
           # important.append(line)
           # break

#print(important, "n")
