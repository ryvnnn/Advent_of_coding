import math

if __name__ == "__main__":
	opened_file = open("day5.txt", "r")
	lines = opened_file.readlines()
	new_lines = []
	for line in new_lines:
		new_lines.append(str(line.strip()))
	new_lines.sort()


def importTextFile(textFile):
	firstList = []
	f = open(textFile)
	for each in f:
		firstList.append(each)
	workingList = []
	for each in firstList:
		workingList.append(each.rstrip())
	return workingList

seatFile = importTextFile("day5.txt")

def getSeatFile(eachSeat):
	current_fb_low = 0
	current_fb_high = 128
	current_rl_low = 0
	current_rl_high = 8
	fb_range = list(range(0,128))
	rl_range = list(range(0,8))
	check = []
	to_rtn = []
	FB = list(eachSeat[0:7])
	RL = list(eachSeat[7:10])
	for letter in FB: 
		if str(letter) == "F":
			if len(fb_range) == 2:
				check.append(letter)
				check.append(fb_range)
				to_rtn.append(fb_range[0])
				break
			else:
				current_fb_high = math.ceil((current_fb_high + current_fb_low)/2)
		if str(letter) == "B":
			if len(fb_range) == 2:
				check.append(letter)
				check.append(fb_range)
				to_rtn.append(fb_range[1])
				break
			else:
				current_fb_low = math.ceil((current_fb_high + current_fb_low)/2)
		fb_range = list(range(current_fb_low, current_fb_high))
	for lett in RL:
		if str(lett) == "R":
			if (len(rl_range)) == 2:
				check.append(lett)
				check.append(rl_range)
				to_rtn.append(rl_range[1])
				break
			else:
				current_rl_low = math.ceil((current_rl_high + current_rl_low)/2)
		if str(lett) == "L":
			if len(rl_range) == 2:
				check.append(lett)
				check.append(rl_range)
				to_rtn.append(rl_range[0])
				break
			else:
				current_rl_high = math.ceil((current_rl_high + current_rl_low)/2)
		rl_range = list(range(current_rl_low, current_rl_high))
	return to_rtn

every = []
for eachSeat in seatFile:
	[row, column] = getSeatFile(eachSeat)
	total = (row * 8) + column
	every.append(total)

print("this is every:", every)
maxid = max(every)
maxid

count = 0
for index in range(len(every)):
	currentValue = every[index]
	nextValue = every[index+1]
	if nextValue - currentValue != 1:
		toRtn = currentValue + 1
		break

print(toRtn)

