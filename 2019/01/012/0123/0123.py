IN_FILEPATH = "in\\01-"
OUT_FILEPATH = "out\\01-"
FILETYPE = "txt"
FILE_NUM = 10

for num in range(1, FILE_NUM + 1):

	path = IN_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path) as f:
		data = f.readlines()

	data = [ data[i].strip("\n").split(" ") for i in range(len(data)) if i != 0 ][0]

	mode = {}

	for s in data:
		if s in mode:
			mode[s] += 1
		else:
			mode[s] = 1

	result = str(max(mode.values()))

	path = OUT_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path, mode="w") as f:
		f.write(result + "\n")
