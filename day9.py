import itertools

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

def iterate(list, value):
	boo_list = []
	for outer in list:
		for inner in list:
			total = int(outer) + int(inner)
			boo_list.append(total)
	return value in boo_list

# nfile = importTextFile('day9.txt')

# tf = nfile[0:25]
# twentyfive = nfile[0:25]

# for index in range(25, len(nfile)):
# 	boo = iterate(twentyfive, int(nfile[index]))
# 	if boo == False:
# 		print('inside:', nfile[index])
# 		break
# 	twentyfive.append(nfile[index])
# 	twentyfive.pop(0)

bad = 2089807806

# file1 = importTextFile('day9.txt')
# file2 = importTextFile('day9.txt')


file1 = importTextFile('d9t.txt')
file2 = importTextFile('d9t.txt')
file3 = importTextFile('d9t.txt')
bad = 127

while len(file1) > 0:
	first_num = file1.pop(0)
	print('first:', first_num)
	total = 0
	while len(file2) > 0:
		count = 0
		total = int(first_num) + int(file2.pop(count))


	for each in file2:
		total = int(first_num)+int(each)
		print('total', total)
		if bad == total:
			print(first_num)
			break







for each1 in range(len(file1)):
	for each2 in range(len(file2)):
		total = each1 + each2 
		if total == bad:
			print(each1, each2)
			break




for i1 in range(len(file1)):
	outer_num = file1[i1]
	count = 0
	while count < len(file2):
		tot = 0
		for i2 in range(count, len(file2)):
			tot = int(outer_num) + int(file2[i2])
			print(outer_num, "+", file2[i2], '=', tot)
			if tot == bad:
				print(file1[i1])
				print(file2[i2])
				break
			else:
				outer_num = tot
		count += 1




curr_list = []
tot = 0
for each1 in file1:
	outer_num = each1
	for each2 in file2:
		print(outer_num, "+", each2, '=', tot)
		tot = int(outer_num) + int(each2)
		if tot == bad:
			print('2')
			print('OUTER NUM,', each1)
			print('INNER NUM:', each2)
			print(curr_list)
			break
		else:
			outer_num = tot





if __name__ == "__main__":
	nfile = importTextFile('day9.txt')
	bad = 2089807806
	rsubset(nfile, bad)


def f(v,i,s):
	if i >= len(v): return 1 if S == 0 else 0
	count = f(v, i+1, s)
	count += f(v, i+1, s - v[i])
	return count 

# f(nfile, 0, bad)

