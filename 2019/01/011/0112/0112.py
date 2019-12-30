IN_FILEPATH = "in\\01-"
OUT_FILEPATH = "out\\01-"
FILETYPE = "txt"
FILE_NUM = 6

PATTERN = {"a", "i", "u", "e", "o"}

for num in range(1, FILE_NUM + 1):

	path = IN_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path) as f:
		s = f.read()

	s = s.replace("\n", "")

	r_num = 0

	for c in s:
		if c in PATTERN:
			r_num += 1

	path = OUT_FILEPATH + '{:0>2}'.format(num) + "." + FILETYPE

	with open(path, mode="w") as f:
		f.write(str(r_num) + "\n")
