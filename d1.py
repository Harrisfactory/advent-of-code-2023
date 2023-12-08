import re

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
	#print(parsed_nums)
	#print(sum(parsed_nums))


def parseNumsTwo(lines):
	num_map = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

	for k in range(len(lines)):
		#line = re.split(r'[one]', line)
		
		lines[k] = re.split(r'(?=(0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))',lines[k])
		for i in range(len(lines[k])):
			if lines[k][i] in num_map:
				#print(part)
				lines[k][i] = num_map[lines[k][i]]
		clean = ''
		for part in lines[k]:
			clean+=str(part)
		#print(clean)
		lines[k] = clean
	
	return lines
	#print(lines)
		


	
	


def p2():
	#i probably want to create a dicitonary to match numbers, but Id have to do a lot of pointer manipulation,
	#I only need to worry about outer substrings from the original parsenums
	file = open("d1p1.txt", "r")
	lines = file.readlines()
	for i in range(len(lines)):
		lines[i] = lines[i].replace('\n','')
	converted_nums = parseNumsTwo(lines)
	
	#print(converted_nums)
	final_parsed = parseNums(converted_nums)
	print(final_parsed)
	print(sum(final_parsed))
	
	



def main():
	#p1()
	p2()

main()
