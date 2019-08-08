# script for running all the shit

from findanagrams import findAnagrams
from interestinganagrams import intAna

def main():

	print("               ANAGRAMS!               ")
	print("=======================================")
	print("This program takes a dictionary of words from a text file,\nmatches them together as anagrams, and returns interesting pieces of information about them.\nAll results are stored int the 'results' folder, and can be optionally printed to screen.\n(except the total list of anagrams, its WAY too long!)")
	input("\nENTER TO CONTINUE: ")
	anagram_list = findAnagrams()
	print("\n...anagrams found, sorted, and stored in csv file...")
	print("\nThis next step of the process finds interesting bids of info about the anagrams, such as:\n")
	print("\t1)\tSEMORDNILAPS, or pairs of words that spell each other backwards")
	print("\t2)\tBACKWARDS COMPOUNDS, i.e. castoff and offcast")
	print("\t3)\tWORDS WITH NO REPEATS, words with none of the same letters twice")
	print("\t4)\tRHYMES, words that end with the same 3 characters")
	print("\t5)\tWORDS WITH MANY CONSONANTS, (at least 9!)")
	print("\t6)\tWORDS WITH MANY VOWELS, (again, at least 9.)")
	input("\nENTER TO CONTINUE: ")
	intAna(anagram_list)
	print("ALL DONE!\nUpdated results in 'results' folder!")
	input("\nENTER TO QUIT")

main()
