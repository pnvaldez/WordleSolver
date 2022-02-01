scrabble_dictionary = "Collins Scrabble Words (2019).txt"
wordle_dictionary = "Wordle Dictionary.txt"

five_letter_words = []

with open(scrabble_dictionary) as f:
	lines = f.readlines()
	for i in range(3, len(lines)):
		curr_word = lines[i][:-1]
		if len(curr_word) == 5:
			five_letter_words.append(curr_word)

with open(wordle_dictionary, 'w') as f:
	for word in five_letter_words:
		f.write(word + '\n')
