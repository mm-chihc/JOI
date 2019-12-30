IN_FILEPATH = "in\\01-"
OUT_FILEPATH = "out\\01-"
FILETYPE = "txt"
FILE_NUM = 11

for num in range(1, FILE_NUM + 1):

	path = IN_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path) as f:
		data = f.readlines()

	data = [ data[i].strip("\n").split(" ") for i in range(len(data)) ]

	s = data[1][0]
	start = int(data[0][1]) - 1
	end = int(data[0][2]) - 1

	l = s[start:end + 1]
	l = l[::-1]

	result = s[:start]

	for i in range(len(l)):
		result += l[i]

	result += s[end + 1:]

	path = OUT_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path, mode="w") as f:
		f.write(result + "\n")
