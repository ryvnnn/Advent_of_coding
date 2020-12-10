####################### Functions for Part 1 #########################

def importTextFile(textFile):
	firstList = []
	f = open(textFile)
	for each in f:
		firstList.append(each)
	workingList = []
	for each in firstList:
		workingList.append(each.rstrip())
	return workingList

def checkEachPass(password):
	splitPass = password.split(':')
	beforeColon = splitPass[0]
	afterColon = splitPass[1]
	letterToCheck = beforeColon[-1] #finds the letter to check
	numRange = findNumberRange(beforeColon) 	#finds the range of numbers 
	matchesLetterList = []
	for each in afterColon:
		if each == letterToCheck:
			matchesLetterList.append(each)
	numOfMatches = len(matchesLetterList)
	numberCheck =[]
	for eachNum in numRange:
		if eachNum == numOfMatches:
			numberCheck.append(eachNum)
	if len(numberCheck) > 0:
		return True
	else:
		return False

#Returns a list with the range of numbers to check how many times the letter appears 
def findNumberRange(password):
	rangeList = []
	firstNum = int(password.split('-')[0])
	secondNum = int(password.split('-')[1].split(' ')[0])
	rangeList.append(firstNum)
	rangeList.append(secondNum)
	rangeNum = firstNum
	while rangeNum < secondNum-1: 
		rangeList.append(rangeNum+1)
		rangeNum+=1
	rangeList.sort()
	return rangeList


#####################Code to run for Part 1###################
allPasses = importTextFile("day2.txt")

numberOfGoodPasswords=0
goodPasswordList = []
for eachPass in allPasses:
	if checkEachPass(eachPass) == True:
		goodPasswordList.append(eachPass)

numberOfGoodPasswords = len(goodPasswordList)










####################################################################################################
############################### PART 2 OF DAY 2 ##################################################### 
#############################################################################################

numberOfGoodPasswords=0
goodPasswordList2 = []
for eachPass in allPasses:
	if checkEachPass2(eachPass) == True:
		goodPasswordList2.append(eachPass)

numberOfGoodPasswords = len(goodPasswordList2)

def checkEachPass2(password):
	splitPass = password.split(':')
	beforeColon = splitPass[0]
	afterColon = splitPass[1]
	letterToCheck = beforeColon[-1] #finds the letter to check
	placementOfNums = findSpecificNumbers(beforeColon) #finds the location of numbers 
	firstNum = placementOfNums[0]
	secondNum = placementOfNums[1]
	if afterColon[firstNum] == letterToCheck:
		if afterColon[secondNum] == letterToCheck:
			return False
		else:
			return True	
	if afterColon[secondNum] == letterToCheck:
		return True

#Returns locations
def findSpecificNumbers(password):
	rangeList = []
	firstNum = int(password.split('-')[0])
	secondNum = int(password.split('-')[1].split(' ')[0])
	rangeList.append(firstNum)
	rangeList.append(secondNum)
	return rangeList


#test Cases
pass1=allPasses[0]
pass2=allPasses[1]
pass3=allPasses[2]
pass4=allPasses[3]
pass5=allPasses[4]

checkEachPass2(pass1)
checkEachPass2(pass2)
checkEachPass2(pass3)
checkEachPass2(pass4)
checkEachPass2(pass5)































