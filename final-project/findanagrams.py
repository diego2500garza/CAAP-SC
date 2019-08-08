# script for finding anagrams out of a big text file

import csv
import os

# function takes the words from the text file as individual strings,
# and stores some of them in a returned list
def Dict_Reader():
	dictionary_list = []
	fileName = input("\nWhat dictionary do you want to run? (file name w/o .txt)\nIf nothing is entered, the given dictionary 'eng-dict.txt' will be used. > ")
	if fileName == '':
		fileName = "eng-dict"
	with open (fileName+".txt", "r") as dictionary:
		for line in dictionary:
			if len(line) > 8:
				line = line.lower()
				dictionary_list.append(line[:-1])
		# removing duplicates:
		dictionary_list = list(set(dictionary_list))
		dcitionary_list = dictionary_list.sort()
	return dictionary_list


# takes a given word, alphabetizes its characters, and returns it
def alphabetize(word):
	alphz_word = ""
	alphz_char_list = sorted(word)
	for i in alphz_char_list:
		alphz_word += i
	return alphz_word


# returns the last index (number of letters) for sort
def takeLast(elem):
	return elem[-1]


# main function, runs everything
def findAnagrams():

	# reads the dictionary into a list and initializes a dictionary
	word_list = Dict_Reader()
	possible_anagram_dict = {}
	anagram_dict = {}

	# alphabetizes each word, creates or finds that as a key in
	# anagram_dict, then stores any words with those letters under it
	for i in word_list:
		key = alphabetize(i)
		possible_anagram_dict.setdefault(key, [])
		possible_anagram_dict[key].append(i)

	# deletes non-anagrams from the dictionary
	# adds an extra index at the end of each anagram indicating the length
	# of the anagrams, and another one indicating the number of anagrams
	# of the words
	for key in possible_anagram_dict:
		words = possible_anagram_dict[key]
		num_anagrams = len(words)
		word_length = len(words[0])
		if num_anagrams > 1:
			anagram_dict.update({key : words})
			anagram_dict[key].append(word_length)

	# turns the dictionary into a list
	anagram_list = []
	for i in anagram_dict.values():
		anagram_list.append(i)

	# sorts that list
	# first by the number of letters in each word
	anagram_list.sort(key=takeLast)
	# then by number of words, python keeps previous order if ties
	anagram_list.sort(key=len)

	# writes the newly sorted list into a csv
	# deletes an old version of the csv if it exits, so it will not
	# add on to the bottom of that file
	if os.path.exists("results/sorted-anagrams.csv"):
		os.remove("results/sorted-anagrams.csv")
	# create and open new file
	anagram_file = open("results/sorted-anagrams.csv",'w+')
	# create csv writer object
	wr = csv.writer(anagram_file, dialect='excel')

	for item in anagram_list:
		wr.writerow(item)

	# returns the list of anagrams to be used in other functions
	return anagram_list
