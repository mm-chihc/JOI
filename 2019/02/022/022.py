import numpy as np

IN_FILEPATH = "in\\sample-"
OUT_FILEPATH = "out\\sample-"
FILETYPE = "txt"
FILE_NUM = 3

ANGLE_TO_NUM = {0:0, 90:1, 180:2, 270:1}

def getData():

	path = IN_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path) as f:
		data = f.readlines()

	data = [ line.replace("\n", "").split(" ") for line in data ][1:]

	print(data)

for num in range(1, FILE_NUM + 1):

	getData()

	path = OUT_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path, mode="w") as f:
		f.write(str(result) + "\n")
