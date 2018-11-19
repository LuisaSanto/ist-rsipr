from pynput.keyboard import Key, KeyCode, Listener, Controller
import cozmo as cozmo

class teleop:
    def __init__(self, robot):
        self.robot = robot
        self.keyboard = Controller()
        self.lastKeyPress = None

    def stopListener(self):
        self.listener.stop()

    def on_key_release(self, key):
        self.lastKeyPress = None
        self.robot.stop_all_motors()
        if key == Key.esc:
            return False

    def on_key_press(self, key):
        self.listener.stop()
        if self.lastKeyPress == key:
            return
        self.lastKeyPress = key
        #drive_wheel_motors(l_wheel_sporwarded, r_wheelspeed, l_wheel_acc=None, r_wheel_acc=None)
        if key == Key.up:
            self.robot.drive_wheels(50.0, 50.0)  #drive forwards
        elif key == Key.right:
            self.robot.drive_wheels(50.0, -50.0)  #turn right
        elif key == Key.left:
            self.robot.drive_wheels(-50.0, 50.0)  #turn left
        elif key == Key.down:
            self.robot.drive_wheels(-50.0, -50.0)  #go backwards
        elif key== KeyCode.from_char('r'):
            self.robot.move_lift(1.0) #raise lift
        elif key == KeyCode.from_char('t'):
            self.robot.move_lift(-1.0) #lower lift

    def Controller(robot: cozmo.robot.Robot):
        teleop = teleop(robot)
        print("press esc to exit")
        print("use arrow keys to control the robot")
        print("R will raise the lift and T lower raise it")
        print("Happy Driving!")
        with Listener(on_release = on_key_release, on_press = on_key_press) as listener:
           listener.join()
