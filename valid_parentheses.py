def valid_parentheses(string):
	flag = False
	string  = list(string)
	if len(string) % 2 != 0:
		return False
	if string.count('(') != string.count(')'):
		return False
	else:
		while not flag:
			for i in range(len(string)):
				if string[i] == '(' and string[i+1] == ')':
					del string[i+1]
					del string[i]
					break
			if len(string) == 0:
				return True
			elif string.count('(') != string.count(')'):
				return False
