# anagrams.py
#
# Looks through a a file and finds the sets with the most anagrams
#
# Usage:
#      % python anagrams.py <filename>
#
# Daniel Serrano August 6, 2018

import sys
import time
start = time.time()
def find_anagrams(fileName):
    with open(fileName, 'rt') as f:
        d = {}
        lst = []
        i = 0
        # Each line or word in the file is stripped and turned to lowercase
        for line in f:
            if len(line) > 8:
                line = line.strip()
                line = line.lower()
                # Extracts the characters from each word and alphabetizes them into a new string named chars
                chars = ''.join(sorted(line))
                if chars in d: 
                    # Checks to see if a word is already in the list to prevent from having the same word appear twice
                    duplicate = False
                    for word in d[chars]:
                        if line == word:
                            duplicate = True
                    if not duplicate:
                        # Appends the current word to the list of word(s) in the dictionary value for the key chars 
                        d[chars].append(line)
                else:
                    # Assigns chars as the dictionary key and the orginal word as a dictionary value within a list
                    d[chars] = [line]

        # Appends each dictionary item to a list
        lst = [item for item in d.items()]
        lst.sort()
        # For each dictionary item in lst it changes into a list with the a list
        # (number words that are anagrams, list of words that are anagrams)
        for i in range(len(lst)):
            lst[i] = [len(lst[i][1]), lst[i][1]]
            i += 1
        # Prints the 50 sets of words with the most anagram
        for set in lst[:50]:
            print(set)
        #return lst
end = time.time()
# Prints the total time it takes the program to run for
print(end - start)
if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "<filename>")
else:
    find_anagrams(sys.argv[1])