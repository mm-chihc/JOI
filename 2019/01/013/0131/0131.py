IN_FILEPATH = "in\\01-"
OUT_FILEPATH = "out\\01-"
FILETYPE = "txt"
FILE_NUM = 20

for num in range(1, FILE_NUM + 1):

	path = IN_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path) as f:
		data = f.read()

	data = data.strip("\n").split(" ")
	data = [ int(s) for s in data ]

	l = list(range(data[1], data[2] + 1))
	l = [ - ( s - data[0] ) if ( s - data[0] ) < 0 else ( s - data[0] ) for s in l ]

	m = min(l)
	result = str(l.index(m) + data[1])

	path = OUT_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path, mode="w") as f:
		f.write(result + "\n")
