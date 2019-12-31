IN_FILEPATH = "in\\01-"
OUT_FILEPATH = "out\\01-"
FILETYPE = "txt"
FILE_NUM = 20

for num in range(1, FILE_NUM + 1):

	path = IN_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path) as f:
		data = f.readlines()

	data = [ line.replace("\n", "").split(" ") for line in data ][1]
	data = [ int(s) for s in data ]

	l = [data[0]]
	result = []

	for s in data[1:]:
		if s >= l[-1]:
			l.append(s)
		else:
			result.append(l)
			l = [s]
	result.append(l)

	result = [ len(line) for line in result ]
	result = str(max(result))

	path = OUT_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path, mode="w") as f:
		f.write(result + "\n")
