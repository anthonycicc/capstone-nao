# Stubs for "beginner" top level functions

import low_level as ll
import naoqi
import math
from functools import wraps

def connection_intact(f):
    @wraps(f)
    def wrapped(self, *args, **kwargs):
        if self.connected:
            return f(self, *args, **kwargs)
        else:
            raise RuntimeError("Make sure to connect to the robot first!")         
    return wrapped

class Beginner_Functions(ll.Low_Level):

    __ip_address = None
    __port = 9559
    connected = False

    # Proxy listing
    __speechProxy = None
    __motionProxy = None
    __postureProxy = None
    __photoCaptureProxy = None

    # list of strings representing what function names we'll be exporting
    def exported_methods(self):
        return []

    # Utility functions

    def __init__(self, ipaddress, port=9559):
        self.connect_to_robot(ipaddress,port)

    def connect_to_robot(self, IPAddress, port=9559):
        """ Connects to the robot over TCP/IP (wifi or ethernet connection), as well as passes

        :param ip_address: the IP Address of the robot
        :param argv: any extra arguments that need to be provided
        :return: 0 on success, something else on failure
        """
        self.__ip_address = IPAddress
        self.__port = port

        # Proxy setup
        try:
            self.__speechProxy = naoqi.ALProxy("ALTextToSpeech", self.__ip_address, self.__port)
            self.__motionProxy = naoqi.ALProxy("ALMotion", self.__ip_address, self.__port)
            self.__postureProxy = naoqi.ALProxy("ALRobotPosture", self.__ip_address, self.__port)
            # self.__photoCaptureProxy = naoqi.ALProxy("ALPhotoCapture", self.__ip_address, self.__port)
            self.__motionProxy.wakeUp()
            self.connected = True
        except:
            raise("Something failed. Please check the IP Address and port of the robot, and try again")

    def disconnect_from_robot(self):
        """ Cleanly disconnects from the robot

        :return: 0 on success, something else on failure
        """
        pass

    @connection_intact
    def reset_to_neutral(self):
        """ Returns the robot to a neutral, standing state

        :return: 0 on success, something else on failure
        """
        self.__postureProxy.goToPosture("StandInit", 0.5)

    # General use functions
    @connection_intact
    def move_forward(self, time):
        """ Moves the robot forward for a certain amount of time (in seconds)

        :param time: the length of time (in seconds) for NAO to move forward
        :return: 0 if action completed successfully, something else on failure
        """
        self.__motionProxy.moveInit()

        self.__motionProxy.moveToward(1, 0,0)
        time.sleep(time)
        self.__motionProxy.stopMove()

    @connection_intact
    def move_backward(self, time):
        """ Moves the robot backward for a certain amount of time (in seconds)

        :param time: the length of time (in seconds) for NAO to move backward
        :return: 0 if action completed successfully, something else on failure
        """
        self.__motionProxy.moveInit()

        self.__motionProxy.moveToward(-1, 0,0)
        time.sleep(time)
        self.__motionProxy.stopMove()

    @connection_intact
    def say(self, inputString):
        """ Instructs the robot to speak aloud

        :param inputString: The string that the robot should speak
        :return: 0 if action completed successfully, something else on failure
        """

        #TODO: Add censorship functions
        self.__speechProxy.say(inputString)

    @connection_intact
    def turn_right(self, angle):
        """ Turns the robot a given angle to the right.

        :param angle: The angle the robot should end up facing
        :return: 0 if action completed successfully, something else on failure
        """
        self.__motionProxy.moveInit()

        self.__motionProxy.moveTo(0, 0, ((-1)*(angle/180)*math.pi))
 
    @connection_intact
    def turn_left(self, angle):
        """ Turns the robot a given angle to the left.

        :param angle: The angle the robot should end up facing
        :return: 0 if action completed successfully, something else on failure
        """
        self.__motionProxy.moveInit()

        self.__motionProxy.moveTo(0, 0, ((angle/180)*math.pi))

    @connection_intact
    def raise_right_arm(self, position):
        """ Raises the right arm of the robot to a given position.

        :param position: The number of the position
        :return: 0 if action completed successfully, something else on failure
        """
        #TODO: Dave 
        self.__motionProxy.moveInit()

    @connection_intact
    def raise_left_arm(self, position):
        """ Raises the left arm of the robot to a given position. Locked to four positions

        :param position: The number of the position
        :return: 0 if action completed successfully, something else on failure
        """
        #TODO: Dave 
        pass
    
    @connection_intact
    def kick(self, leg):
        """ Instructs the robot to kick with either leg

        :param leg: The leg (left or right) to kick with
        :return: 0 if action completed successfully, something else on failure
        """
        #TODO: Dave 
        pass
    
    @connection_intact
    def extend_arm(self, arm):
        """ Extends the arm of the robot to be perpendicular to the robot

        :param arm: The arm (left or right) to extend
        :return: 0 if action completed successfully, something else on failure
        """
        #TODO: Dave 
        pass
    
    @connection_intact
    def take_picture(self, fileName):
        """ Takes a picture with the camera mounted on the robot's head

        :param fileName: The name of the file to send back to the user
        :return: An image file with the given name
        """

        #TODO: Consider allowing user to set picture format as well

        self.__photoCaptureProxy.SetPictureFormat("png")
        self.__photoCaptureProxy.TakePicture(fileName)

    @connection_intact
    def play_audio(self, filePath):
        """ Plays an audio file from the user's computer

        :param filePath: The path to the audio file
        :return: 0 if action completed successfully, something else on failure
        """
        pass
    
    @connection_intact
    def sit(self):
        """ Instructs the robot to sit down on the floor

        :return: 0 if action completed successfully, something else on failure
        """
        self.__postureProxy.goToPosture("Sit", 0.5)

        
    @connection_intact
    def stand(self):
        """ Instructs the robot to stand at neutral position

        :return: 0 if action completed successfully, something else on failure
        """

        self.__postureProxy.goToPosture("Stand", 0.5)

    @connection_intact
    def lay_down(self):
        """ Instructs the robot to lay down

        :return: 0 if action completed successfully, something else on failure
        """
        self.__postureProxy.goToPosture("LyingBack", 0.5)

