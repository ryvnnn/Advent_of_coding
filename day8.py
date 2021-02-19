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

gamefile = importTextFile('day8.txt')


def find_acc_value(gamefile):
	currentval, index, accumulator, visited, counter = 0, 0, 0, [], 0
	while counter == 0:
		print(index)
		action, value = gamefile[index].split(' ')
		if visited.count(index) > 1:
		# 	# print('1')
			print('REPEATED acc:', accumulator)
			return accumulator, visited
		if action == 'jmp':
			# print('2')
			index = index + int(value)
			# print('changed index jmp:', index)
			print('acc jump', accumulator)
		elif action == 'acc':
			# print('3')
			accumulator = accumulator + int(value)
			index += 1
			# print('changed index acc:', index)
			print('acc acc', accumulator)
		elif action == 'nop':
			# print('4')
			index += 1
			# print('changed index nop:', index)
		visited.append(index)

#part 2 
def find_acc_value(gamefile):
	currentval, index, accumulator, visited, counter = 0, 0, 0, [], 0
	while counter == 0:
		print('INDEX', index)
		if index == 628:
		# if index == 9:
			print("ENDED ACC", acc)
			return accumulator, visited, 0
		# if index == 628:
		# 	print('acc', accumulator)
		# 	return accumulator, visited
		# print(index, '|', gamefile[index])
		action, value = gamefile[index].split(' ')
		if visited.count(index) > 1:
		# 	# print('1')
			print('REPEATED ACC:', accumulator)
			return accumulator, visited, 1
		if action == 'jmp':
			# print('2')
			index = index + int(value)
			# print('changed index jmp:', index)
			# print('acc jump', accumulator)
		elif action == 'acc':
			# print('3')
			accumulator = accumulator + int(value)
			index += 1
			# print('changed index acc:', index)
			# print('acc acc', accumulator)
		elif action == 'nop':
			# print('4')
			index += 1
			# print('changed index nop:', index)
		visited.append(index)


file1 = importTextFile('day8.txt')
# file1 = importTextFile('d8t.txt')
# file2 = importTextFile('d8t.txt')

total = 0
for index in range(len(file1)):
	action, value = file1[index].split(' ')
	print('ACTION:', action, '| VALUE:', value)
	if action == 'jmp':
		file1[index] = 'nop '+value
		acc, v, repeated = find_acc_value(file1)
		if repeated == 0:
			print('GOOD ACC:', acc)
			break
		else:
			file1 = importTextFile('day8.txt')
	if action == 'nop':
		file1[index] = 'jmp '+value
		acc, v, repeated = find_acc_value(file1)
		if repeated == 0:
			print('GOOD ACC:', acc)
			break
		else:
			file1 = importTextFile('day8.txt')

