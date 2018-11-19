
def print_numbered_list(bag):	
	if isinstance(bag, dict):
		for k, v in sorted(bag.items()):
			print(" " + str(k).rjust(3) + "  " + v[1])
		
	elif isinstance(bag, list):
		for t in range(len(bag)):
			print(" " + str(t).rjust(3) + "  " + bag[t])

