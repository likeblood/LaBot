def check_format(name: str) -> bool:
	try:
		# check text and file format
		if  name.rfind('_') == -1 or\
			name.rfind('.') == -1 or\
			name.rfind(' ') != -1 or\
			(name[name.rfind('_') + 1 : name.rfind('.')]).isalpha() or\
			not(len(name[len(name) - 3: len(name)])):
			return False
		else:
			name = name.strip()
			# check lab number
			lab_number = int(name[name.rfind('_') + 1 : name.rfind('.')])
			if lab_number in [i for i in range(6, 13)]:
				return True
			else:
				return False
	except:
		return False
