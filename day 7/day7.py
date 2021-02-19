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



rules = importTextFile("day7.txt")

def split_rules(rule): #splits into carrier then named bags in a list
	value_dict = {}
	eachlist = rule.split("bags contain")
	color = eachlist[0][0:-1]
	values = eachlist[1].split(',')
	values[-1] = values[-1].split('.')[0]
	for index in range(len(values)):
		if values[index][-1] == "g":
			values[index] = values[index][3:]
		else:
			values[index] = values[index][3:-1]
	return color, values

# def split_rules(rule):
# 	value_dict = {}
# 	eachlist = rule.split("bags contain")
# 	color = eachlist[0][0:-1]
# 	values = eachlist[1].split(',')
# 	values[-1] = values[-1].split('.')[0]
# 	for index in range(len(values)):
# 		values[index] = values[index][1:-1]
# 	return color, values


dictionary = {}
for each in rules:
	color, values = split_rules(each)
	dictionary[color] = values

print(dictionary)

test




#find carriers 
def recurse1(left, dictionary):
	# if len(v) == 0:
	# 	return v
	my_list = []
	for each in dictionary:
		if str(left) in dictionary[each]:
			my_list.append(each)
	return my_list

recurse1("shiny gold bag", t)
recurse1("bright white bag", t)
recurse1("muted yellow bag", t)

initial_list = recurse1("shiny gold bag", dictionary)
new_list = []
for item in initial_list:
	new_list.append(initial_list)

print(initial_list)

for index in range(len(initial_list)):
	print(index)
	i = str(initial_list[index])+" bag"
	print(i)
	r_list = recurse1(i, dictionary)
	print(r_list, "rlist")
	for each in r_list:
		if each not in new_list:
			new_list.append(each)

x,y = [],[]
for a in new_list:
	if a not in x:
		x.append(a)

for q in x:
	if isinstance(q, list):
		for w in q:
			y.append(w)
	else:
		y.append(q)

print(y)
print(len(y))


		

recurse("shiny gold bag", dictionary)
	for each_key in dictionary:
		if shiny gold bag in dictionary[each_key]:
			numsum = recurse()
		else:
			sum = 1

	for k, v in dictionary.items():
		print(k)
		print(v)
		if left not in dictionary[k]:
			print('3')
			my_list.append(left)
		else:
			print('4')
			my_list += recurse1(k, dictionary)
	return my_list


recurse1("gold shiny bag", dictionary)


	v = []
	for each in dictionary:
		print(carrier+" bag")
		if (carrier+" bag") in dictionary[each]:
			v.append(each)
	return v

a = []
a = recurse1(v[0], dictionary)
a

for each in a:
	b = recurse1(each, dictionary)


# def recurse1(carrier, dictionary, list):
# 	sumnum = 0
# 	print(carrier + " ba ### OR ### ", carrier + " bag")
# 	if (carrier + " ba") not in dictionary.values() or (carrier + " bag") not in dictionary.values():
# 		print("2")
# 		sumnum = 1
# 	for each in dictionary:
# 		if "shiny gold bag" in dictionary[each]:
# 			v.append(each)
# 			recurse1(each, dictionary, v)
# 			sumnum += 1
# 	return sumnum









