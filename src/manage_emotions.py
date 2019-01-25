import os
import sys
import matplotlib.pyplot as plt
import emotion
from random import randint
import pandas as pd

from display import *
from lists import *

results_view = {
    "1": "Neutral",
    "2": "Happy",
    "3": "Sad",
    "4": "Angry",
    "5": "Shutdown",
}


def results_view_loop(robot, robot_plot):
    global cmd_emo

    while True:
        print("\nView final results:")
        print_numbered_list(results_view)

        try:
            in_cmd = input("\n-> ")
            cmd_emo = in_cmd

            if cmd_emo == "1":
                current_emotion = 'neutral'
                robot.play_anim_trigger(neutral_anims[randint(0, len(neutral_anims)-1)], loop_count=1).wait_for_completed()
                robot.add_expression(current_emotion)
                robot.set_current_emotion(current_emotion)

            elif cmd_emo == "2":
                current_emotion = 'happy'
                robot.play_anim_trigger(happy_anims[randint(0, len(happy_anims)-1)], loop_count=1).wait_for_completed()
                robot.add_expression(current_emotion)
                robot.set_current_emotion(current_emotion)

            elif cmd_emo == "3":
                current_emotion = 'sadness'
                robot.play_anim_trigger(sad_anims[randint(0, len(sad_anims)-1)], loop_count=1).wait_for_completed()
                robot.add_expression(current_emotion)
                robot.set_current_emotion(current_emotion)

            elif cmd_emo == "4":
                current_emotion = 'anger'
                robot.play_anim_trigger(angry_anims[randint(0, len(angry_anims)-1)], loop_count=1).wait_for_completed()
                robot.add_expression(current_emotion)
                robot.set_current_emotion(current_emotion)

            robot_plot = robot_plot.append(robot.emotions, ignore_index=True)

        except IndexError:
            continue

        except KeyError:
            if cmd_emo in quit_cmds:
                break

            elif cmd_emo in exit_cmds:
                sys.exit(0)

            elif cmd_emo in clear_cmds:
                os.system("tput reset")

            else:
                print("invalid option.")
                continue
    styles = ['rs-', 'go-', 'b^-', 'ro-', 'y^-']
    robot_plot(title="Current Emotions", style=styles)
    plt.show()


def cozmo_manage_emotion(robot: cozmo.robot.Robot):
    cozmo_robot = emotion.Emotion(robot)
    robot_plot = pd.DataFrame(cozmo_robot.emotions, index=[0])
    print("Welcome to the emotional manager!")
    print("Please select a emotion.")
    results_view_loop(cozmo_robot, robot_plot)
