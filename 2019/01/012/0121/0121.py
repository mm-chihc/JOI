IN_FILEPATH = "in\\01-"
OUT_FILEPATH = "out\\01-"
FILETYPE = "txt"
FILE_NUM = 10

for num in range(1, FILE_NUM + 1):

	path = IN_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path) as f:
		data = f.read().replace("\n", "").split(' ')

	data = [ int(s) for s in data ]
	data.sort()

	result = str(data[1] + data[2])

	path = OUT_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path, mode="w") as f:
		f.write(result + "\n")
