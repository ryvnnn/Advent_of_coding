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

def make_dictionary_from_file(file):
	dictionary = {}
	for each in file:
		color, values = split_rules(each)
		dictionary[color] = values
	return dictionary

def find_carriers(string, dictionary):
	carrier_list = []
	string1, string2 = (string+" bag"), (string+" bags")
	for each in dictionary:
		if string1 in dictionary[each] or string2 in dictionary[each]:
			carrier_list.append(each)
	return carrier_list

test = importTextFile("test.txt")
test_dict = make_dictionary_from_file(test)

find_carriers("shiny gold", test_dict)
find_carriers("bright white", test_dict)
find_carriers("muted yellow", test_dict)

run_list = [] #list that is added to 
init_list2 = [] #list of every carrier that is found 
rtn_list = [] #list of carriers to return
init_list = find_carriers("shiny gold", test_dict) #initial list of carriers 

#add answers to list to return
for each1 in init_list:
	rtn_list.append(each1)


while len(init_list) != 0:#while initial list has more than one entry
	for each in init_list: #initlist = [bright white, muted yellow]
		item = find_carriers(each, test_dict) #item = [light red, dark orange], [] 
		if item == []:
			run_list.append(each)
		else: 
			

print(run_list)
		# run_list.append(find_carriers(each, test_dict))

print(run_list)

		run_list.append(each)
		init_list2.append(each)
		init_list.remove(each)


