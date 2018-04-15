num = [0,0,0,0,0]
print 'input five numbers :'
num[0] = float(raw_input())
num[1] = float(raw_input())
num[2] = float(raw_input())
num[3] = float(raw_input())
num[4] = float(raw_input())
print '1.sum of five numbers\n2.average of five numbers\n3.quit'
key = int(raw_input())
while key != 3:
	if key == 1:
		sum = 0
		for i in num:
			sum += i
		print sum
	elif key == 2:
		sum = 0
		for i in num:
			sum += i
		ave = float(sum/5)
		print ave
	else:
		print 'quit...'
	print '1.sum of five numbers\n2.average of five numbers\n3.quit'
	key = int(raw_input())
