counter = 0
aList = [0, 0, 0, 0, 0]
while counter < 5:
	aList[counter] = raw_input()
	counter += 1

#aList = [1, 3, 5, 5, 6]
sum = 0
for i in aList:
	sum = sum + int(i)

print sum