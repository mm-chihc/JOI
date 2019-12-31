IN_FILEPATH = "in\\01-"
OUT_FILEPATH = "out\\01-"
FILETYPE = "txt"
FILE_NUM = 20

for num in range(1, FILE_NUM + 1):

	path = IN_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path) as f:
		data = f.readlines()

	data = [ line.replace("\n", "") for line in data ][1]
	result = data.replace("joi", "JOI")

	path = OUT_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path, mode="w") as f:
		f.write(result + "\n")
