# script for finding intersting stuff out of the anagrams

import csv
import os
import itertools

# takes a given word, alphabetizes its characters, and returns it
def alphabetize(word):
	alphz_word = ""
	alphz_char_list = sorted(word)
	for i in alphz_char_list:
		alphz_word += i
	return alphz_word

# writes a list into a file:
def csvMaker(list, filename):
	if os.path.exists(filename + ".csv"):
		os.remove(filename + ".csv")
	# create and open new file
	file = open(filename + ".csv",'w+')
	# create csv writer object
	wr = csv.writer(file, dialect='excel')
	# writes it in:
	for item in list:
		wr.writerow(item)

#reverses a word, suprisingly useful
def reWord(word):
	reversed_word = ""
	for i in range(len(word)):
		reversed_word += word[-1*(i + 1)]
	return reversed_word

# finds semordnilaps in a given set of words that are anagrams
# of each other, returns the semordnilaps as a list of tuples
# i.e. palindrome and semordnilap
# ...apparently there are none...
def semordnilapFinder (anagram_set):
	list_of_semordnilaps = [] # we need a list in case there's two

	for i in range(len(anagram_set)):
		word = anagram_set[i]

		# creates the semordnilap of the 'i'th word, named
		# 'reversed_word'
		reversed_word = reWord(word)

		# initiates a counting variable that starts the index
		# after i
		j = i+1
		# checks if every word after word 'i' is the same as
		# the reversed word (that would indicate a semordnilap)
		while j < len(anagram_set):
			if anagram_set[j] == reversed_word:
				list_of_semordnilaps.append((word, reversed_word))
			j += 1

	return list_of_semordnilaps


# given two anagrams, returns whether they are backwards compounds
# i.e. castoff and offcast
# makes sure it is not just the first 3  and last letters 3
def backCompWord(a1, a2):
	for i in range(len(a1)):
		beg1 = a1[:i]
		j = -(i)
		end2 = a2[j:]
		if beg1 == end2 and i >= 3:
			return True


# receives a string and sorts alphabetically
# BASICALLY outputs sorted string without duplicate characters
def woDup(word):
	word = str(word)
	a = sorted(word)
	b = ""
	next_letter = a[0]
	for letter in range(len(a)):
		j = letter
		try:
			if next_letter == a[j]:
				while a[j] == a[j+1]:
					j = j+1
				next_letter = a[j+1]
				b += a[letter]
		except:
			if a[letter] != a[letter - 1]:
				b += a[letter]
	return(b)

def rhymesto(anagram_list):
	rhymes_l = []
	x = 0
	# will index every single list 
	for anagram in anagram_list:
		nums = anagram[-1]
		rhymes = 0
		# will go through every single word in the list and position will run through and not
		# include the int part of the list
		for position in range(len(anagram)-1):
		# this will set last three to be equal to the last three leters in each word
			last_three = anagram[position][-3:]
			counter = 0	
			for i in range(len(anagram)-1):
				# checks to see if j is not a integer, while it is not then 
				# it will check the last three letters this will then print 
				# the list that has words that rhyme	
				if anagram[i][-3:] == last_three:
					counter += 1
					# this will essentially count the number of occurences 
					# that the anagram at position [i][-3] is equal to the last three in the next word.
			if counter > 1:
				rhymes += 1
				
		if rhymes > 0:
			rhymes_l.append(anagram)
	return rhymes_l


#finds anagram set that has largest amount of consonants
#by subtracting amount of vowels from amount of characters in the word
def biggest_consonants(anagrams):
	biggest_consonants = []
	for i in anagrams:
		word = i[0]
		count = 0
		for letter in word:
			if letter == 'a':
				count += 1
			elif letter == 'e':
				count += 1
			elif letter == 'i':
				count += 1
			elif letter == 'o':
				count += 1
			elif letter == 'u':
				count += 1
		letters = len(i[0])
		consonant_amount = letters - count
		if consonant_amount > 9:
			biggest_consonants.append(i)
	return biggest_consonants


#finds anagram set that has largest amount of vowels
def biggest_vowels(anagrams):
	biggest_vowels = []
	for i in anagrams:
		word = i[0]
		count = 0
		for letter in word:
			if letter == 'a':
				count += 1
			elif letter == 'e':
				count += 1
			elif letter == 'i':
				count += 1
			elif letter == 'o':
				count += 1
			elif letter == 'u':
				count += 1
		if count > 9:
			biggest_vowels.append(i)
	return biggest_vowels


# main function, runs everything
def intAna (anagrams):
	prn = input("\nWould you like the results of the programs to print? Some are quite large.\nEither way a csv in the results folder will be created / updated. (y/n) > ")
	
	sem = input("\ndo you want to find SEMORDNILAPS? y/n > ")
	if sem == 'y':
		print("SEMORDNILAPS:")
		sem_list = []
		for i in anagrams:
			if semordnilapFinder(i[:-1]) != []:
				sem_list.append(semordnilapFinder(i[:-1]))
				if prn == 'y':
					print(semordnilapFinder(i[:-1]))
		csvMaker(sem_list, "results/sems")
		print("file created / updated")

	bc = input("\ndo you want to find BACKWARDS COMPOUNDS? y/n > ")
	if bc == 'y':
		print("BACKWARDS COMPOUNDS:")
		bc_list = []
		for i in anagrams:
			for combo in itertools.combinations(i[:-1], 2):
				if backCompWord(combo[0], combo[1]) == True:
					bc_list.append(combo)
					if prn == 'y':
						print(combo)
		csvMaker(bc_list, "results/back-comp")
		print("file created / updated")

	wd = input("\ndo you want to find WORDS WITH NO REPEATS? y/n > ")
	if wd == 'y':
		print("WORDS WITH NO REPEATS:")
		wd_list = []
		for i in anagrams:
			s_i = alphabetize(i[0])
			if woDup(i[0]) == s_i:
				wd_list.append(i[0:-1])
				if prn == 'y':
					print(i[0:-1])
		csvMaker(wd_list, "results/no-repeats")
		print("file created / updated")

	rh = input("\ndo you want to find RHYMES? y/n > ")
	if rh == 'y':
		print("RHYMES:")
		rh_list	= rhymesto(anagrams)
		if prn == 'y':
			print(rh_list)
		csvMaker(rh_list, "results/rhymes")
		print("file created / updated")

	cn = input("\ndo you want to find WORDS WITH MANY CONSONANTS? > ")
	if cn == 'y':
		print("WORDS WITH MANY CONSONANTS:")
		cn_list = biggest_consonants(anagrams)
		if prn == 'y':
			print(cn_list)
		csvMaker(cn_list, "results/big-consonants")
		print("file created / updated")
		
	vw = input("\ndo you want to find WORDS WITH MANY VOWELS? > ")
	if vw == 'y':
		print("WORDS WITH MANY VOWELS:")
		vw_list = biggest_vowels(anagrams)
		if prn == 'y':
			print(vw_list)
		csvMaker(vw_list, "results/big-vowels")
		print("file created / updated")