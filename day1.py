import itertools
import numpy as np

numbersArray = []
numbersFile = open("input.txt")
print(numbersFile)
for each in numbersFile:
	numbersArray.append(each)

newNumbersArray = []
for each in numbersArray:
	newNumbersArray.append(int(each.rstrip()))


target = 2020
total = []
for firstNum in newNumbersArray:
	for secondNum in newNumbersArray:
		for thirdNum in newNumbersArray:
			if firstNum + secondNum + thirdNum == target:
			# if firstNum in total:
				total.append(firstNum)
			# if secondNum in total:
				total.append(secondNum)
				total.append(thirdNum)

finalTotal =list(set(total))




target = 2020
for numbers in itertools.combinations(newNumbersArray, 2):
	if sum(numbers) == target:
		 = print([newNumbersArray.index(number) for number in numbers])

firstNum = newNumbersArray[141]
secondNum = newNumbersArray[161]

print(firstNum "+" secondNum)
total=firstNum*secondNum
print(total)




