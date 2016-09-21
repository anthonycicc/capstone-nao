# Stubs for "beginner" top level functions

import low_level as ll

class Beginner_Functions(ll.Low_Level):
    # This will be the magic that makes this class only return what we want
    def __dir__(self):
        return []

    # Utility functions

    def connect_to_robot(self, ip_address, argv):
        """ Connects to the robot over TCP/IP (wifi or ethernet connection), as well as passes

        :param ip_address: the IP Address of the robot
        :param argv: any extra arguments that need to be provided
        :return: 0 on success, something else on failure
        """
        pass

    def disconnect_from_robot(self):
        """ Cleanly disconnects from the robot

        :return: 0 on success, something else on failure
        """
        pass

    def reset_to_neutral(self):
        """ Returns the robot to a neutral, standing state

        :return: 0 on success, something else on failure
        """
        pass

    # General use functions

    def move_forward(self, steps):
        """ Moves the robot forward a certain number of steps

        :param steps: The number of steps to move the robot forward
        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def move_backward(self, steps):
        """ Moves the robot backward a certain number of steps

        :param steps: The number of steps to move the robot forward
        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def say(self, inputString):
        """ Instructs the robot to speak aloud

        :param inputString: The string that the robot should speak
        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def turn_right(self, angle):
        """ Turns the robot a given angle to the right. Locked to only accept angles in 45 degree increments

        :param angle: The angle the robot should end up facing
        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def turn_left(self, angle):
        """ Turns the robot a given angle to the left. Locked to only accept angles in 45 degree increments

        :param angle: The angle the robot should end up facing
        :return: 0 if action completed successfully, something else on failure
        """
        pass


    def raise_right_arm(self, position):
        """ Raises the right arm of the robot to a given position. Locked to four positions

        :param position: The number of the position
        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def raise_left_arm(self, position):
        """ Raises the left arm of the robot to a given position. Locked to four positions

        :param position: The number of the position
        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def kick(self, leg):
        """ Instructs the robot to kick with either leg

        :param leg: The leg (left or right) to kick with
        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def extend_arm(self, arm):
        """ Extends the arm of the robot to be perpendicular to the robot

        :param arm: The arm (left or right) to extend
        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def take_picture(self, fileName):
        """ Takes a picture with the camera mounted on the robot's head

        :param fileName: The name of the file to send back to the user
        :return: An image file with the given name
        """
        pass

    def play_audio(self, filePath):
        """ Plays an audio file from the user's computer

        :param filePath: The path to the audio file
        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def sit(self):
        """ Instructs the robot to sit down on the floor

        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def stand(self):
        """ Instructs the robot to stand at neutral position

        :return: 0 if action completed successfully, something else on failure
        """
        pass

    def lay_down(self):
        """ Instructs the robot to lay down

        :return: 0 if action completed successfully, something else on failure
        """
        pass