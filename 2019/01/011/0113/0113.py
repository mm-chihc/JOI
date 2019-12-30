IN_FILEPATH = "in\\01-"
OUT_FILEPATH = "out\\01-"
FILETYPE = "txt"
FILE_NUM = 10

for num in range(1, FILE_NUM + 1):

	path = IN_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path) as f:
		data = f.readlines()

	data = [ data[i].strip("\n").split(" ") for i in range(len(data)) if i != 0 ]
	data = [ [ int(s) for s in line ] for line in data ]

	a = data[0]
	b = data[1]

	x = 0
	a_num = 0
	b_num = 0
	result = []

	while x < len(a) + len(b):
		if a_num == len(a):
			result.append(str(b[b_num]))
			b_num += 1
		elif b_num == len(b):
			result.append(str(a[a_num]))
			a_num += 1
		else:
			if b[b_num] < a[a_num]:
				result.append(str(b[b_num]))
				b_num += 1
			else:
				result.append(str(a[a_num]))
				a_num += 1

		x += 1

	path = OUT_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path, mode="w") as f:
		f.write("\n".join(result) + "\n")
