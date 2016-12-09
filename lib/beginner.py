# Stubs for "beginner" top level functions

import low_level as ll
import naoqi
import math
import time
from ui_rep import UI_Func, Func_Arg, ui_from_func
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

    # Returns a list of UI_Func
    def exported_methods(self):
        x = [
            (self.reset_to_neutral, []),
            (self.move_forward, [Func_Arg('seconds',
                                     'length of time for NAO to move forward',
                                     'Natural')]), # Consider replacing these with func calls
            (self.move_backward, [Func_Arg('seconds',
                                     'length of time for NAO to move backward',
                                      'Natural')]),
            (self.say, [Func_Arg('inputString',
                            'Words for NAO to say',
                            'string')]),
            (self.move_right, [Func_Arg('seconds',
                                     'length of time for NAO to turn right',
                                      'Natural')]),
            (self.move_left, [Func_Arg('seconds',
                                     'length of time for NAO to turn left',
                                      'Natural')]),
            (self.raise_right_arm, [Func_Arg('position',
                                        'Number of the position',
                                        [1,2,3,4])]),
            (self.raise_left_arm, [Func_Arg('position',
                                            'Number of the position',
                                            [1,2,3,4])]),
            (self.kick, [Func_Arg('side',
                             'which leg to kick',
                             ['Left', 'Right'])]),
            (self.extend_arm, [Func_Arg('side',
                                   'which arm to extend',
                                   ['Left, Right'])]),
            (self.take_picture, [Func_Arg('fileName',
                                     'what to name to save the picture as',
                                     'string')]),
            (self.play_audio, [Func_Arg('filePath',
                                   'location of the audio file to play',
                                   'string')]),
            (self.sit, []),
            (self.stand, []),
            (self.lay_down, []),
        ]
        return [ui_from_func(func, args) for (func, args) in x]

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
    def move_forward(self, seconds):
        """ Moves the robot forward for a certain amount of time (in seconds)

        :param seconds: the length of time (in seconds) for NAO to move forward
        :return: 0 if action completed successfully, something else on failure
        """
        self.__motionProxy.moveInit()

        self.__motionProxy.moveToward(1, 0, 0)
        time.sleep(seconds)
        self.__motionProxy.stopMove()

    @connection_intact
    def move_backward(self, seconds):
        """ Moves the robot backward for a certain amount of time (in seconds)

        :param seconds: the length of time (in seconds) for NAO to move backward
        :return: 0 if action completed successfully, something else on failure
        """
        self.__motionProxy.moveInit()

        self.__motionProxy.moveToward(-1, 0,0)
        time.sleep(seconds)
        self.__motionProxy.stopMove()

    @connection_intact
    def say(self, inputString):
        """ Instructs the robot to speak aloud

        :param inputString: The string that the robot should speak
        :return: 0 if action completed successfully, something else on failure
        """

        censoredString = self.censor_text(inputString)
        self.__speechProxy.say(censoredString)

    @connection_intact
    def move_right(self, seconds):
        """ Turns the robot a given angle to the right.

        :param seconds: the length of time (in seconds) for NAO to move to the right
        :return: 0 if action completed successfully, something else on failure
        """
        self.__motionProxy.moveInit()

        self.__motionProxy.moveToward(0, -1,0)
        time.sleep(seconds)
        self.__motionProxy.stopMove()
 
    @connection_intact
    def move_left(self, seconds):
        """ Turns the robot a given angle to the left.

        :param seconds: the length of time (in seconds) for NAO to move to the left
        :return: 0 if action completed successfully, something else on failure
        """
        self.__motionProxy.moveInit()

        self.__motionProxy.moveToward(0, 1,0)
        time.sleep(seconds)
        self.__motionProxy.stopMove()

    @connection_intact
    def raise_right_arm(self, position):
        """ Raises the right arm of the robot to a given position.

        :param position: The number of the position (1 to 4)
        :return: 0 if action completed successfully, something else on failure
        """
        angle = ((position-3)*0.25)*math.pi
        self.__motionProxy.moveInit()

        self.__motionProxy.setAngles("RShoulderPitch", angle, 0.1)
        time.sleep(4)

    @connection_intact
    def raise_left_arm(self, position):
        """ Raises the left arm of the robot to a given position. Locked to four positions

        :param position: The number of the position
        :return: 0 if action completed successfully, something else on failure
        """
        angle = ((position-3)*0.25)*math.pi
        self.__motionProxy.moveInit()

        self.__motionProxy.setAngles("LShoulderPitch", angle, 0.1)
        time.sleep(4)

    @connection_intact
    def kick(self, leg):
        """ Instructs the robot to kick with either leg

        :param leg: The leg ('L' for left, 'R' for right) to kick with
        :return: 0 if action completed successfully, something else on failure
        """
        #TODO: Dave - This doesn't work (yet) - 10/12
        hipPitch = leg + "HipPitch"
        kneePitch = leg + "KneePitch"
        
        self.__motionProxy.setAngles(hipPitch, -0.5*math.pi, 0.5)
        self.__motionProxy.setAngles(kneePitch, 0.5*math.pi, 0.5)
        time.sleep(0.25)
        self.__motionProxy.setAngles(kneePitch, 0, 1)
        time.sleep(0.3)
        self.__motionProxy.setAngles(kneePitch, 0.5*math.pi, 1)
        time.sleep(0.25)
        self.__motionProxy.setAngles(hipPitch, 0, 0.5)
        self.__motionProxy.setAngles(kneePitch, 0, 0.5)

    @connection_intact
    def extend_arm(self, arm):
        """ Extends the arm of the robot to be perpendicular to the robot

        :param arm: The arm ('L' for left, 'R' for right) to extend
        :return: 0 if action completed successfully, something else on failure
        """
        self.__motionProxy.moveInit()
        
        self.__motionProxy.setAngles(arm + "ShoulderPitch", 0, 0.1)
        self.__motionProxy.setAngles(arm + "ShoulderRoll", 0, 0.1)
        self.__motionProxy.setAngles(arm + "ElbowRoll", 0, 0.1)

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

