IN_FILEPATH = "in\\01-"
OUT_FILEPATH = "out\\01-"
FILETYPE = "txt"
FILE_NUM = 17
import pdb

def getData():
	path = IN_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE
	with open(path) as f:
		data = f.read()
	data = int(data.replace("\n", ""))
	return data

def output(result):
	path = OUT_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE
	with open(path, mode="w") as f:
		f.write(result + "\n")

for num in range(1, FILE_NUM + 1):

	n = getData()

	d = [0] * (n + 1)
	d[n] = 1

	for i in range(n, -1, -1):
		s = sum(list(map(int, str(i))))
		if (i + s) <= n and d[i + s]:
			d[i] += 1

	result = sum(d)
	print(result)

	output(str(result))
