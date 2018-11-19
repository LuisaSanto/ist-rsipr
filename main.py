import os, sys
# check if running under python3
if sys.version_info < (3, 0):
	sys.stdout.write("DENIED: requires Python 3.x\n")
	sys.exit(1)
else:
	import numpy as np

from lists import *
from display import *

def tic_tac_toe():
	print("In tic tac toe")

def controller():
	print("In controller")

def display_emotions():
	print("In display_emotions")

def reaction():
	print("In reaction")

execution_modes = {
	"1": [tic_tac_toe,		"Play tic tac toe"],
	"2": [controller,		"Controller"],
	"3": [display_emotions,	"Display Emotions"],
	"4": [reaction,			"Reaction to speak"],
}



def main():
	
	os.system("tput reset")

	while True:
		print("\nExecution mode:")
		print_numbered_list(execution_modes)
		try:
			in_cmd = input("\n-> ")
			cmd = in_cmd
			results = execution_modes[cmd][0]()

		except IndexError as e:
			continue

		except KeyError as e:
			if cmd in quit_cmds:
				break
				
			elif cmd in exit_cmds:
				sys.exit(0)
				
			elif cmd in clear_cmds:
				os.system("tput reset")
				
			else:
				print("invalid option.")
				continue
	


if __name__ == '__main__':
	main()
