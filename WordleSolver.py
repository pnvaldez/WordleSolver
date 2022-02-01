import random

class Wordle:
	def __init__(self, word_info, included_letters, wrong_letters, dictionary):
		self.word_info = word_info
		self.included_letters = included_letters
		self.wrong_letters = wrong_letters
		self.dictionary = dictionary

	#checks the curr_word against word_info to see if it is valid
	def is_valid(self, curr_word):
		for i in range (0, 5):
			if self.word_info[i][0] != "": #case for if the letter is known
				if self.word_info[i][0] != curr_word[i]:
					return False
			elif curr_word[i] in self.word_info[i][1]: #case for if the letter is yellow
				return False
			elif curr_word[i] in self.wrong_letters: #case for all grey letters
				return False
		for i in range(0, len(self.included_letters)): #checks if the yellow letters are included
			if self.included_letters[0] not in curr_word:
				return False
		return True

	def next_guess(self):
		temp_dict = []
		for i in range (0, len(self.dictionary)):
			if self.is_valid(self.dictionary[i]):
				temp_dict.append(self.dictionary[i])
		self.dictionary = temp_dict
		return random.choice(self.dictionary)

	def update_info(self, guess):
		for i in range(0, 5):
			if self.word_info[i][0] != "":
				pass
			else:
				info = input("Current Letter: " + guess[i] + " (F: False, T: True, W: Wrong Place): ")
				if info == "T":
					self.word_info[i][0] = guess[i]
				elif info == "W":
					self.included_letters.append(guess[i])
					self.word_info[i][1].append(guess[i])
				elif info == "F":
					self.wrong_letters.append(guess[i])
				



word_info = [] #5x2 array, word_info[i][0] = the correct letter, word_info[i][1] = incorrect letters
included_letters = [] #any yellow letters go here
wrong_letters = []
wordle_dictionary = []

for i in range(0, 5):
	word_info.append(["",[]])

with open("Wordle Dictionary.txt") as f:
	temp_dictionary = f.readlines()
	for i in range(0, len(temp_dictionary)):
		wordle_dictionary.append(temp_dictionary[i][0:5])

wordle = Wordle(word_info, included_letters, wrong_letters, wordle_dictionary)
first_guess = input("First Guess: ")
wordle.update_info(first_guess)

counter = 2
while True:
	next_guess = wordle.next_guess()
	print("Try: " + next_guess)
	correct_word = input(" Did " + next_guess + " work? (Y:Yes, N:No) ")
	if correct_word == "Y":
		print("Congrats! WordleSolver solved today's Wordle in " + str(counter) + " tries")
		break
	else:
		wordle.update_info(next_guess)
		counter += 1

