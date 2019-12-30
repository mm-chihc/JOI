IN_FILEPATH = "in\\01-"
OUT_FILEPATH = "out\\01-"
FILETYPE = "txt"
FILE_NUM = 6

for num in range(1, FILE_NUM + 1):

	path = IN_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path) as f:
		s = f.read()

	s = s.replace("\n", "").split(' ')

	num1 = 0
	num2 = 0

	for c in s:
		if c == "1":
			num1 += 1
		if c == "2":
			num2 += 1

	if num1 > num2:
		s = "1"
	else:
		s = "2"

	path = OUT_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path, mode="w") as f:
		f.write(s + "\n")
