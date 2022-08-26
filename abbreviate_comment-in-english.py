# This python code is to replace full journal names in a bibtex database file (.bib) into abbreviated names.
# journal_list.txt contains abbreviated names of nearly all journals.
# If one journal is not included, its abbreviated name can be found at http://www.ncbi.nlm.nih.gov/nlmcatalog/journals.

import os
import re
import sys

try:
    # input the whole content of a bib file as a very long string
    bibtexdb = ''.join(open(sys.argv[1], 'r', errors='ignore').readlines())
#    print (bibtexdb)
except IndexError:
    print("Error: Specify the file to be processed!")
    exit(1)
except FileNotFoundError:
    print("Error: Provided filename could not be loaded!")
    exit(1)

fr = open('journal_list.txt', 'r', errors='ignore')
line = fr.readline()

# go over journal names in journal_list.txt one by one, and replace the full name in bibtexdb with its abbreviated counterpart. 
while(line):
    patterns = line[:-1].split(" = ")[:2]
    pattern1, pattern2 = map(lambda pattern: "{%s}" % pattern, patterns)
    
    # avoid mere abbreviations
    if pattern1 != pattern1.upper() and (' ' in pattern1):
        repl = re.compile(re.escape(pattern1), re.IGNORECASE)
        (bibtexdb, num_subs) = repl.subn(pattern2, bibtexdb)
        
        # print the number of replacements
        if num_subs > 0:
            print("Replaced (%ix) '%s' FOR '%s'" % (num_subs, *patterns))
    
    # go to the next journal name
    line = fr.readline()

# write the updated content into a new file
with open('library_abbreviated.bib', 'w') as outfile:
    outfile.write(bibtexdb)
    print("Bibtex database with abbreviated files saved into 'library_abbreviated.bib'")