def check_format(name: str) -> bool:
	try:
		if  name.rfind('_') == -1 or\
			name.rfind('.') == -1 or\
			name.rfind(' ') != -1 or\
			(name[name.rfind('_') + 1 : name.rfind('.')]).isalpha() or\
			name[len(name) - 3: len(name)] != 'pdf':
			return False
		else:
			name = name.strip()
			lab_number = int(name[name.rfind('_') + 1 : name.rfind('.')])
			if lab_number in [i for i in range(6, 13)]:
				return True
			else:
				return False
	except:
		return False
