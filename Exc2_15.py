num = [0,0,0]
sort = [0,0,0]
print 'input three numbers :'
num[0] = float(raw_input())
num[1] = float(raw_input())
num[2] = float(raw_input())
print '1.descending order\n2.rising order\n3.quit'
key = int(raw_input())
while key != 3:
	if key == 1:
		if num[0] > num[1]:
			if num[0] > num[2]:
				if num[1] > num[2]:
					sort[0] = num[0]
					sort[1] = num[1]
					sort[2] = num[2]
				else:
					sort[0] = num[0]
					sort[1] = num[2]
					sort[2] = num[1]
			else:
				sort[0] = num[2]
				sort[1] = num[0]
				sort[2] = num[1]
		elif num[0] > num[2]:
			sort[0] = num[1]
			sort[1] = num[0]
			sort[2] = num[2]
		elif num[1] > num[2]:
			sort[0] = num[1]
			sort[1] = num[2]
			sort[2] = num[0]
		else:
			sort[0] = num[2]
			sort[1] = num[1]
			sort[2] = num[0]
		print sort
	elif key == 2:
		if num[0] > num[1]:
			if num[0] > num[2]:
				if num[1] > num[2]:
					sort[0] = num[0]
					sort[1] = num[1]
					sort[2] = num[2]
				else:
					sort[0] = num[0]
					sort[1] = num[2]
					sort[2] = num[1]
			else:
				sort[0] = num[2]
				sort[1] = num[0]
				sort[2] = num[1]
		elif num[0] > num[2]:
			sort[0] = num[1]
			sort[1] = num[0]
			sort[2] = num[2]
		elif num[1] > num[2]:
			sort[0] = num[1]
			sort[1] = num[2]
			sort[2] = num[0]
		else:
			sort[0] = num[2]
			sort[1] = num[1]
			sort[2] = num[0]
		sort[0], sort[1], sort[2] = sort[2], sort[1], sort[0]
		print sort
	else:
		print 'quit...'
	print '1.descending order\n2.rising order\n3.quit'
	key = int(raw_input())
