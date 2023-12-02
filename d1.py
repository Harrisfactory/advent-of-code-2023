
def parseNums(lines):
	results = []
	for i in range(len(lines)):
		cur_line = lines[i]
		left, right = 0, len(cur_line)-1
		while left <= right:
			if cur_line[left].isnumeric() and cur_line[right].isnumeric():
				s_nums = str(cur_line[left] + cur_line[right])
				i_nums = int(s_nums)
				results.append(i_nums)
				break
			if not cur_line[left].isnumeric():
				left+=1
			if not cur_line[right].isnumeric():
				right-=1
	return results
				
def p1():
	file = open("d1p1.txt", "r")
	lines = file.readlines()
	parsed_nums = parseNums(lines)
	#print(parsed_nums)
	print(sum(parsed_nums))
	

def main():
	p1()

main()
