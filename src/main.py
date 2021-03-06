import os
import sys

# check if running under python3
if sys.version_info < (3, 0):
    sys.stdout.write("DENIED: requires Python 3.x\n")
    sys.exit(1)
else:
    from lists import *
    from display import *
    from teleop import *
    from manage_emotions import *


def tic_tac_toe():
    print("In tic tac toe")


def controller():
    cozmo.run_program(cozmo_controller)


def display_emotions():
    cozmo.run_program(cozmo_manage_emotion)


execution_modes = {
    "1": [tic_tac_toe, "Play game"],
    "2": [controller, "Controller"],
    "3": [display_emotions, "Display Emotions"],
}


def main():
    global cmd
    os.system("tput reset")

    while True:
        print("\nExecution mode:")
        print_numbered_list(execution_modes)
        try:
            in_cmd = input("\n-> ")
            cmd = in_cmd
            execution_modes[cmd][0]()

        except IndexError:
            continue

        except KeyError:
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
