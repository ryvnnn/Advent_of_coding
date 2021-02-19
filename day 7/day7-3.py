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


### FOR PART 1 ####
# def split_rules(rule): #splits into carrier then named bags in a list
# 	value_dict = {}
# 	eachlist = rule.split("bags contain")
# 	color = eachlist[0][0:-1]
# 	values = eachlist[1].split(',')
# 	values[-1] = values[-1].split('.')[0]
# 	for index in range(len(values)):
# 		if values[index][-1] == "g":
# 			values[index] = values[index][3:]
# 		else:
# 			values[index] = values[index][3:-1]
# 	return color, values

### FOR PART 2 ###
def split_rules(rule): #splits into carrier then named bags in a list
	value_dict = {}
	eachlist = rule.split("bags contain")
	color = eachlist[0][0:-1]
	values = eachlist[1].split(',')
	values[-1] = values[-1].split('.')[0]
	for index in range(len(values)):
		if values[index][-1] == "g":
			values[index] = values[index][1:]
		else:
			values[index] = values[index][1:-1]
	return color, values

def make_dictionary_from_file(file):
	dictionary = {}
	for each in file:
		color, values = split_rules(each)
		dictionary[color] = values
	return dictionary


##### USED FUNCTIONS #####
def find_carriers(string, dictionary):
	carrier_list = []
	string1, string2 = (string+" bag"), (string+" bags")
	for each in dictionary:
		if string1 in dictionary[each] or string2 in dictionary[each]:
			carrier_list.append(each)
	return carrier_list

def r(string, dictionary, run_list):
	item = find_carriers(string, dictionary) #find the bags that can carry current bag
	if item == []: #checking to see if current has no carriers 
		run_list.append(item) 
	else:
		for each in item: #otherwise go through each item 
			if r(str(each), dictionary, run_list) != []: #check to see next bag has any carriers. if no carriers, add to list
				run_list.append(each) 
			else:
				r(str(each), dictionary, run_list) #if has carriers, continue on
	return run_list

rules = importTextFile("day7.txt")
dictionary = make_dictionary_from_file(rules)

# r("light red", test_dict, [])
# r("bright white", test_dict, [])
# s = r("shiny gold", test_dict, [])
s = r("shiny gold", dictionary, [])
for each in s:
	if each == []:
		s.remove(each)

t = list(dict.fromkeys(s))
len(t)

tgs = ['shiny gold bags contain 1 dull lime bag, 2 pale coral bags, 1 wavy silver bag, 5 muted black bags.']
tdgs = make_dictionary_from_file(tgs)


### FOR PART 2 ###
def getBags(string, dictionary, total):
	if 'no other bag' in dictionary[string] or 'no other bags' in dictionary[string]:
		return 0
	else:
		for each in dictionary[string]:
			color = each[2:-4]
			count = int(each[0])
			total = count + count*int(getBags(color, dictionary, 0)) + total
	return total


getBags('shiny gold', t, 0)



for each in t2['shiny gold']:
	color = each[2:-4]
	count = each[0]
	print(color, count, each)

getBags("shiny gold", t2, 0)






####### old stuff not working ###########




# def r(string, dictionary, total):
# 	# print(dictionary[string], "dic string value")
# 	if 'no other bag' in dictionary[string] or 'no other bags' in dictionary[string]:
# 		return 0
# 	# if str(dictionary[string]) == "no other bag" or str(dictionary[string]) == "no other bags":
# 	# 	return 0
# 	else:
# 		for each_color in dictionary[string]:
# 			outer_num = int(each_color[0])
# 			color = each_color[2:-4]
# 			inner_num = (int(r(str(color), dictionary, total)))
# 			print('EACH COLOR:', each_color,'| OUTER NUM:', outer_num, '| INNER NUM:', inner_num, '| color:', color)
# 			mult = outer_num*inner_num
# 			print('MULT:', mult)
# 			print('TOTAL1',total) 
# 			new = outer_num + mult
# 			print('NEW', new)
# 			total = new + int(total)
# 			print('TOTAL2',total)
# 	return total


# r("shiny gold", t2, 0)

# dictionary = make_dictionary_from_file(importTextFile('day7.txt'))
# t2 = make_dictionary_from_file(importTextFile('t2.txt'))
# t = make_dictionary_from_file(importTextFile('test.txt'))
# r('shiny gold', dictionary, 0)
# r('shiny gold', t2, 0)
# r("shiny gold", t, 0)

# shiny gold bags contain 1 dull lime bag, 2 pale coral bags, 1 wavy silver bag, 5 muted black bags.
# dull lime bags contain no other bags.
# pale coral bags contain 5 dim gold bags, 1 vibrant bronze bag.
# dim gold bags contain no other bags.
# vibrant bronze bags contain no other bags.
# wavy silver bags contain no other bags.
# muted black bags contain no other bags.



