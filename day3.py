def importTextFile(textFile):
	firstList = []
	f = open(textFile)
	for each in f:
		firstList.append(each)
	workingList = []
	for each in firstList:
		workingList.append(each.rstrip())
	return workingList


treesFile = importTextFile("day3.txt")
hitTree = []

#right 3, down 1
currentRow = 0
currentRight = 0
count = 0

while count < 323:
	print(currentRight, "start")
	if currentRight+3 >= 31:
		currentRight = currentRight - 31
	if treesFile[currentRow+1][currentRight+3] == "#":
		hitTree.append(treesFile[currentRow+1][currentRight+3])
	currentRow+=1
	currentRight+=3
	count+=1
	print(currentRight, "end")


#right 1, down 1 = 90
#right 3, down 1 = 278
#right 5, down 1 = 88
#right 7, down 1 = 98
#right 1, down 2 = 45

hitTree = []
currentRow = 0
currentRight = 0
count = 0
rightMove = 1
downMove = 2

while count < 323:
	print(currentRight, "start")
	if currentRight+rightMove >= 31:
		currentRight = currentRight - 31
	if treesFile[currentRow+downMove][currentRight+rightMove] == "#":
		hitTree.append(treesFile[currentRow+downMove][currentRight+rightMove])
	currentRow+=downMove
	currentRight+=rightMove
	count+=1
	print(currentRight, "end")


len(hitTree)


