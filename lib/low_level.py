# Stubs for "lower level" functionality
from naoqi import ALProxy
import almath

class Low_Level():
    ACTION_TIME = 0.6
    
    @staticmethod
    def new(robotIP, port=9559):
        tts = ALProxy("ALTextToSpeech", robotIP, port)
        motionProxy  = ALProxy("ALMotion", robotIP, port)
        postureProxy = ALProxy("ALRobotPosture", robotIP, port)
        Low_Level(motionProxy, postureProxy, tts)

    def __init__(self, motionProxy, postureProxy, tts):
        self.motionProxy = motionProxy
        self.postureProxy = postureProxy
        self.tts = tts
   

    def step_right_leg(self):
        """ Instructs the robot to step with its right leg

        :return: 0 if action completed successfully, something else on failure
        """
        return step_leg("right")

    def step_left_leg(self):
        """ Instructs the robot to step with its left leg

        :return: 0 if action completed successfully, something else on failure
        """
        return step_leg("left")
       

    def step_leg(self, leg):
        if leg == "left":
            legName = "LLeg"
        else:
            legName = "RLEG"
        x = 0.04
        y = 0.1
        theta = 0
        clearExisting = False
        timeList = [ACTION_TIME]
        self.motionProxy.setFootSteps([legName], footSteps, timeList, clearExisting)
        return 0

    def censor_text(self, inputString):
        """ Utility function to censor any text given to the robot, such that it will self-censor 'bad' words

        :param inputString: The string to censor
        :return: The censored string
        """
        # TODO actually implement this
        return inputString

    def speak(self, text):
        """ A direct text-to-speech function

        :param text: The text to speack aloud
        :return: 0 if action completed successfully, something else on failure
        """

        self.tts.say(text)
        return 0

    def move_shoulder(self, side, pitch, roll):
        """ Moves the shoulder of the robot to the given pitch and roll

        :param pitch: a number, X-XX, that describes the pitch of the robot's shoulder
        :param roll: a number, X-XX, that describes the roll of the robot's shoulder
        :return: 0 if action completed successfully, something else on failure
        """
        joints = ["ShoulderPitch", "ShoulderRoll"]
        return move_joints(side, joints, [pitch], [roll])
     

    def move_joints(self, side, joints, angleList):
        """ Moves a list of joints on a given side of the body to the given angles

        :param side: What side of the body to move
        :param joints: List of joints with side prefix
        :param angleList: A list of angles to set a given joint to, must be the same
        length as joints
        :return: 0

        """
        if side == "left":
            sidePrefix = "L"
        else:
            sidePrefix = "R"
        jointNames = [sidePrefix + joint for joint in joints]
        angleLists = [[angle] for angle in angleList]
        timeLists = [[ACTION_TIME] for _ in joints]
        isAbsolute = True
        self.motionProxy.angleInterpolation(jointNames, angleLists, timeLists, isAbsolute)
        return 0

    def move_elbow(self, side, yaw, roll):
        """ Moves the elbow of the robot to the given yaw

        :param yaw: a number, X-XX, that describes the yaw of the robot's elbow
        :return: 0 if action completed successfully, something else on failure
        """
        joints = ["ElbowYaw", "ElbowRoll"]
        return move_joints(side, joints, [[yaw], [roll]])

    def move_wrist(self, side, yaw):
        """ Moves the wrist of the robot

        :param movementThing: a number, X-XX, that describes
        :return: 0 if action completed successfully, something else on failure
        """
        return move_joints(side, ["WriteYaw"], [[yaw]])

    def kick_leg(self, side):
        joints = ["HipPitch", "KneePitch", "AnklePitch"]
        angles = [[almath.TO_RADS(deg)] for deg in [-80, -4, 0]]
    
        return move_joints(side, joints, angles)
    

    def kick_right_leg(self):
        """ Instructs the robot to kick with its right leg

        :return: 0 if action completed successfully, something else on failure
        """
        return kick_leg("right")
        pass

    def kick_left_leg(self):
        """ Instructs the robot to kick with its left leg

        :return: 0 if action completed successfully, something else on failure
        """
        return kick_leg("left")


    def speech_to_text(self, waitPeriod):
        """ A potentially useful function for transcribing speech to text

        :param waitPeriod: how long the robot should wait before starting transcription
        :return: the generated text
        """
        # http://doc.aldebaran.com/2-1/naoqi/audio/alspeechrecognition.html
        # Seems to imply we can't just...listen for arbitrary speech and convert it to text
        
        pass

    def change_behavior(self, behaviorName):
        """ A function to change to one of the built in behaviors of the robot

        :param behaviorName: The name of the behavior
        :return: 0 if action completed successfully, something else on failure
        """
        pass
