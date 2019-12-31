import numpy as np

IN_FILEPATH = "in\\01-"
OUT_FILEPATH = "out\\01-"
FILETYPE = "txt"
FILE_NUM = 17

ANGLE_TO_NUM = {0:0, 90:1, 180:2, 270:1}

def getData():

	path = IN_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path) as f:
		data = f.readlines()

	data = [ line.replace("\n", "") for line in data ]

	n = int(data[0])
	s = data[1: n + 1]
	s = [ [ c for c in line ] for line in s ]
	t = data[n+1:]
	t = [ [ c for c in line ] for line in t ]
	return n, s, t

def getMinutes(n, s, t, angle):

	arr = np.array(s)
	arr = np.rot90(arr, int(angle / 90))
	arr = arr.tolist()

	result = n*n - getMatch(arr, t) + ANGLE_TO_NUM[angle]

	return result

def getMatch(arr, t):

	result = 0

	for i in range(n):
		for j in range(n):
			if arr[i][j] == t[i][j]:
				result += 1

	return result

for num in range(1, FILE_NUM + 1):

	n, s, t = getData()

	result = [ getMinutes(n, s, t, angle) for angle in ANGLE_TO_NUM ]
	result = min(result)

	path = OUT_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path, mode="w") as f:
		f.write(str(result) + "\n")
