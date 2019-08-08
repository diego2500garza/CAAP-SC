+==========================+
|                          |
|      ANAGRAM FINDER      |
|                          |
+==========================+


GROUP MEMBERS:
============================

- Charlie Mayville: cmayville@uchicago.edu
- Daniel Serrano: dserrano@uchicago.edu
- Diego Garza: diego2500garza@uchicago.edu
- Nichole Avila: navila@uchicago.edu

WHAT EVERBODY WORKED ON:
============================

DANIEL:
- Wrote a version of the main.py but ultimately the group decided to use Charlie’s version
  for the program as it took advantage of using os and csv. My main.py takes any dictionary 
  (text file) from the command line and returns a list of anagram lists. 
- File can be found under 'anagrams_daniels.py'

CHARLIE:
- wrote findanagrams.py 
  (file that uses the dictionary to find, sort, return, and store anagrams as csv)
- wrote core of interestinganagrams.py 
  (namely the intAna() function that calls and displays all the unique information
  and the little supporting bits like csvMaker() and alphabetize())
- wrote the semordnilaps function 'semordnilapFinder()'
- wrote the backwards compound function 'backCompWord()'
- wrote main.py and created user interface

DIEGO:
- wrote vowels fucntion 'biggest_vowels()'
- wrote constants function 'biggest_consonants()'
- wrote the no duplicate letters function 'woDup()'

NICHOLE:
- wrote rhyme finder function 'rhymesto()'


INSTRUCTIONS:
============================

Really just run 'main.py' -- it has instructions as you go.

'main.py' runs 'anagramfinder.py' and 'interestinganagrams.py' from it without prompt
- anagramfinder uses either a prompted .txt file or eng-dict.txt, which can be found in the main folder
- interestinganagrams asks the user whether or not to print the results, and which results are desired

the results of both scripts processes are stored in csv files in /results:
- 'sorted-anagrams.csv' -- all 7,000 some anagrams found in the dictionary sorted by number of grams,
  then by word length, and then alphabetically
- 'sems.csv' -- "all" the semordnilap pairs
- 'back-comp.csv' --  all the backwards compound word pairs
- 'rhymes.csv' -- all the pairs of rhymes
- 'no-repeats.csv' -- all the anagrams that have no repeated letters, sorted by anagram sets
- 'big-consonants.csv' -- all the anagrams with more than 9 consonants
- 'bit-vowels.csv' -- all the anagram with more than 9 vowels

.csv files are updated everytime you run the program, but nothing really changes because the input 
does not change