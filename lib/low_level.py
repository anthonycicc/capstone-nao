# Stubs for "lower level" functionality

import naoqi

class Low_Level():

    __ip_address = "none"
    __port = 9559

    def exported_methods(self):
         return []

    def connect_to_robot(self, IPAddress, port=9559):
        self.__ip_address = IPAddress
        self.__port = port

    def step_right_leg(self):
        """ Instructs the robot to step with its right leg

        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def step_left_leg(self):
        """ Instructs the robot to step with its left leg

        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def censor_text(self, inputString):
        """ Utility function to censor any text given to the robot, such that it will self-censor 'bad' words

        :param inputString: The string to censor
        :return: The censored string
        """
        pass

    def speak(self, text):
        """ A direct text-to-speech function

        :param text: The text to speack aloud
        :return: 0 if action completed successfully, something else on failure
        """
        if (self.__ip_address != "none"):
            tts = naoqi.ALProxy("ALTextToSpeech", self.__ip_address, self.__port)
            tts.say(text)
        else:
            raise RuntimeError("Make sure to connect to the robot first!")

    def move_shoulder(self, pitch, roll):
        """ Moves the shoulder of the robot to the given pitch and roll

        :param pitch: a number, X-XX, that describes the pitch of the robot's shoulder
        :param roll: a number, X-XX, that describes the roll of the robot's shoulder
        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def move_elbow(self, yaw):
        """ Moves the elbow of the robot to the given yaw

        :param yaw: a number, X-XX, that describes the yaw of the robot's elbow
        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def move_wrist(self, movementThing):
        """ Moves the wrist of the robot

        :param movementThing: a number, X-XX, that describes
        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def kick_right_leg(self):
        """ Instructs the robot to kick with its right leg

        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def kick_left_leg(self):
        """ Instructs the robot to kick with its left leg

        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def speech_to_text(self, waitPeriod):
        """ A potentially useful function for transcribing speech to text

        :param waitPeriod: how long the robot should wait before starting transcription
        :return: the generated text
        """
        pass

    def change_behavior(self, behaviorName):
        """ A function to change to one of the built in behaviors of the robot

        :param behaviorName: The name of the behavior
        :return: 0 if action completed successfully, something else on failure
        """
        pass
