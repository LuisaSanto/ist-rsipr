from pynput.keyboard import Key, KeyCode, Listener, Controller
import cozmo as cozmo


class Teleop:
    def __init__(self, robot):
        self.robot = robot
        self.keyboard = Controller()
        self.lastKeyPress = None

    def stop_listener(self):
        self.robot.listener.stop()

    def on_key_release(self, key):
        self.lastKeyPress = None
        self.robot.stop_all_motors()
        if key == Key.esc:
            return False

    def on_key_press(self, key):
        self.robot.listener.stop()
        if self.lastKeyPress == key:
            return

        self.lastKeyPress = key

        if key == Key.up:
            self.robot.drive_wheels(50.0, 50.0)  # drive forwards

        elif key == Key.right:
            self.robot.drive_wheels(50.0, -50.0)  # turn right

        elif key == Key.left:
            self.robot.drive_wheels(-50.0, 50.0)  # turn left

        elif key == Key.down:
            self.robot.drive_wheels(-50.0, -50.0)  # go backwards

        elif key == KeyCode.from_char('r'):
            self.robot.move_lift(1.0)  # raise lift

        elif key == KeyCode.from_char('t'):
            self.robot.move_lift(-1.0)  # lower lift


def cozmo_controller(robot: cozmo.robot.Robot):
    cozmo_robot = Teleop(robot)
    print("press esc to exit")
    print("use arrow keys to control the robot")
    print("R will raise the lift and T lower raise it")
    print("Happy Driving!")
    with Listener(on_release=cozmo_robot.on_key_release, on_press=cozmo_robot.on_key_press) as cozmo_robot.listener:
        cozmo_robot.listener.join()
