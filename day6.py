##### SETUP #####

def importTextFile(textFile):
	firstList = []
	f = open(textFile)
	for each in f:
		firstList.append(each)
	workingList = []
	for each in firstList:
		workingList.append(each.rstrip())
	return workingList

def separateAnswers(answersWithLines):
	allAnswers, currentAnswers = [], []
	for index in range(len(answersWithLines)):
		if answersWithLines[index] == answersWithLines[-1]:
			currentAnswers.append(answersWithLines[index])
			allAnswers.append(currentAnswers)
			return allAnswers
		if answersWithLines[index] != '':
			currentAnswers.append(answersWithLines[index])
		if answersWithLines[index] == '':
			allAnswers.append(currentAnswers)
			currentAnswers = []
		

##### Part 1 #####

def combine(answerFile):
	allLetters = []
	for word in answerFile:
		for letter in word:
			allLetters.append(letter)
	return allLetters

def find(answerFile):
	allNums = []
	for group in answerFile:
		allNums.append(len(set(combine(group))))
	return allNums


answersFile = importTextFile("day6.txt")
a = separateAnswers(answersFile)
a
b = [['bzny', 'nyozb', 'ybzn']]
c = [['uacsj', 'scu', 'cseu', 'qbumsc'], ['gwo', 'wo', 'yow']]

sum(find(a))

##### PART 2 #####

def find_common(answerFile):
	allNums = []
	for group in answerFile:
		common_dict = {}
		for word in group:
			for letter in word:
				if letter in common_dict:
					common_dict[letter] = common_dict[letter]+1
				else:
					common_dict[letter] = 1
		for each in common_dict:
			if common_dict[each] == len(group):
				allNums.append(each)
	return allNums

find_common(c)