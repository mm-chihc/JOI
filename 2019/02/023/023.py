IN_FILEPATH = "in\\sample-"
OUT_FILEPATH = "out\\sample-"
FILETYPE = "txt"
FILE_NUM = 3

def getData():
	path = IN_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE
	with open(path) as f:
		data = f.read()
	data = int(data.replace("\n", ""))
	return data

def output():
	path = OUT_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE
	with open(path, mode="w") as f:
		f.write( + "\n")

for num in range(1, FILE_NUM + 1):

	n = getData()
	print(n)

	# output()
