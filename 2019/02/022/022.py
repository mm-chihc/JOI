import numpy as np

IN_FILEPATH = "in\\01-"
OUT_FILEPATH = "out\\01-"
FILETYPE = "txt"
FILE_NUM = 43

def getData():

	path = IN_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path) as f:
		data = f.readlines()

	data = [ line.replace("\n", "").split(" ") for line in data ]
	data = [ [ int(c) for c in line ] for line in data ]

	n = data[0][0]
	data = sorted(data[1:])
	a = np.array([ line[0] for line in data ])
	t = np.array([ line[1] for line in data ])

	return n, a, t

def searchTargetPoint(n, a, t, get_nums):

	masked = [a >= t][0]
	target_nums = masked * get_nums
	target_nums = np.array(np.where(target_nums))[0]

	return target_nums

def getTargetNum(target_num, target_nums):

	follow = target_nums[target_nums > target_num]

	if len(follow) > 0:
		result = follow.min()
	else:
		back = target_nums[target_nums < target_num]
		result = back.max()

	return result

def move(a, t, now_point, target_point):

	time_delta = abs(target_point - now_point)

	a = np.abs(a - target_point)
	t = t - time_delta

	return a, t

def getWait(n, a, t, get_nums, target_num):

	loss = 0

	target_nums = searchTargetPoint(n, a, t, get_nums)

	if len(target_nums) == 0:
		m = t[t > 0].min()
		index = np.array(np.where(t == m))[0]
		target_num = getTargetNum(target_num, index)
		target_nums = np.array([target_num])
		loss = m - a[target_num]
		t = t - loss

	return loss, t, target_nums

for num in range(1, FILE_NUM + 1):

	#	print("\n-*-*-*-*-*- " + "{:0>2}".format(num) + " -*-*-*-*-*-")

	n, a, t = getData()

	now_point = 0
	target_num = -1
	loss = 0
	get_nums = np.full(n, True)

	# per = -1
	# if len(str(n)) - 4 < 0:
	# 	d = 0
	# else:
	# 	d = len(str(n)) - 4

	a_ed = a

	for i in range(n):

		# now_per = round((i / n) * 100, d)
		#
		# if now_per != per:
		# 	per = now_per
		# 	print("\rcalculating... " +  str(per) + "%  ", end="")

		wait_time, t, target_nums = getWait(n, a_ed, t, get_nums, target_num)
		loss += wait_time

		target_num = getTargetNum(target_num, target_nums)

		get_nums[target_num] = False
		target_point = a[target_num]

		point_delta = target_point - now_point

		if point_delta > 0:
			loss += point_delta
		else:
			loss += - point_delta

		a_ed, t = move(a, t, now_point, target_point)

		now_point = target_point

	loss += now_point

	# print("\rcalculating... 100%  ")
	# print("\n" + str(loss))

	path = OUT_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path, mode="w") as f:
		f.write(str(loss) + "\n")
