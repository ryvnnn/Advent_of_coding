def importTextFile(textFile):
	firstList = []
	f = open(textFile)
	for each in f:
		firstList.append(each)
	workingList = []
	for each in firstList:
		workingList.append(each.rstrip())
	return workingList


#separates file into lists by each passport
def findEachPassport(passportFile):
	allPassports = []
	currentPassport = []
	currentPosition = 0
	for eachLine in passportFile:
		if eachLine != '':
			currentPassport.append(eachLine)
		if eachLine == '':
			allPassports.append(currentPassport)
			currentPassport = []
	return allPassports

#splits each passport into the fields available
def splitPassport(passport):
	fieldList = []
	for each in passport:
		first = each.split(' ')
		for inner in first:
			fieldList.append(inner.split(':')[0])
	return fieldList


def checkPassport(passport):
	checklist = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "cid", "hgt"]
	inList = []
	for each in passport:
		if each in checklist:
			inList.append(each)
	if len(inList) == 8:
		return True
	if len(inList) == 7:
		if "cid" not in passport:
			return True
	else:
		return False


passportFile = importTextFile("day4.txt")
goodPassports = [] 

newPassportFile = findEachPassport(passportFile)
# currentPasses = []


# for eachPass in newPassportFile:
# 	fieldsToCheck = splitPassport(eachPass)
# 	evaluated = checkPassport(fieldsToCheck)
# 	if evaluated == True:
# 		currentPasses.append(evaluated)

# len(currentPasses)

#test cases
# checkPassport(passport)


def valuePassport(passport):
	fieldList = []
	for each in passport:
		first = each.split(' ')
		for inner in first:
			fieldList.append(inner.split(':')[1])
	return fieldList
# valuePassport(pass1[0])

def makeRealPass(passport):
	myList = []
	newList = []
	for each in passport:
		first = each.split(' ')
		myList.append(first)
	for eachItem in myList:
		for innerItem in eachItem:
			newList.append(innerItem)
	return newList

# makeRealPass(pass1[0])

def valueGrabber(passport, index):
	field = passport[index]
	value = field.split(':')[1]
	return value


def indexGrabber(passport, string1):
	index = 0
	for each in passport: 
		if string1 in each:
			return index
		index+=1


def valueChecker(passport):
	goodPassportValues = []
	for each in passport:
		title, value = each.split(":")
		if title == "byr":
			if len(value) == 4:
				if int(value) > 1919 and int(value) < 2003:
					goodPassportValues.append(each)
		if title == "iyr":
			if len(value) == 4:
				if int(value) > 2009 and int(value) < 2021:
					goodPassportValues.append(each)
		if title == "eyr":
			if len(value) == 4:
				if int(value) > 2019 and int(value) < 2031:
					goodPassportValues.append(each)
		if title == "hgt":
			if value[-1] == "m":
				cmHeight = list(range(150,194))
				if value[2] == "c":
					height = value[0] + value[1]
				else:
					height = value[0] + value[1] + value[2]
				if int(height) in cmHeight:
					goodPassportValues.append(each)
			if value[-1] == "n":
				inHeight = list(range(59, 77))
				height = value[0]+value[1]
				if int(height) in inHeight: 
					goodPassportValues.append(each)
		if title == "hcl": #hcl:#c0946f
			checkVals = []
			numbers = ['0', '1', '2', '3', '4', '5', '6','7','8','9']
			letters = ['a', 'b', 'c', 'd', 'e', 'f']
			if value[0] == "#":
				for eachItem in value:
					if eachItem in numbers or eachItem in letters:
						checkVals.append(each)
			if len(checkVals) == 6 and len(value) == 7:
				goodPassportValues.append(each)
		if title == "ecl":
			if value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth":
				goodPassportValues.append(each)
		if title == "pid":
			if len(value) == 9:
				goodPassportValues.append(each)
		if title == "cid":
			goodPassportValues.append(each)
	return goodPassportValues

# valueChecker(p11, "pid")

#check valid

newPassportFile = findEachPassport(passportFile)

validatedPassports = []
evaluated = []
for eachPass in newPassportFile: 
	realPass = makeRealPass(eachPass)
	evaluated = valueChecker(realPass)
	if len(evaluated) == len(realPass):
		if int(len(evaluated)) == 8:
			validatedPassports.append(evaluated)
		if int(len(evaluated)) == 7:
			s = splitPassport(evaluated)
			if "cid" not in s:
				validatedPassports.append(evaluated)
				print(evaluated)
		# validatedPassports.append(evaluated)
	# print(len(validatedPassports[-1]))
	# if len(evaluated) < 7 and evaluated in validatedPassports:
	# 	validatedPassports.remove(evaluated)

print(len(validatedPassports))

for elem in validatedPassports:
	print(elem, len(elem))









