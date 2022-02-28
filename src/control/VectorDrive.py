import numpy as np


class VectorDrive
    '''
    This class implements vector drive for the MATE ROV based on the convention
    seen in the markdown file available in this directory
    '''
    def __init__(self,motors):
        '''
        Inputs:
            - motors: motor objects to inport
        '''
        self.motors = motors
    def vectorDrive(input_vector):
        '''
        Converts an input vector of the following values to a vector drive vector
        Inputs:
            - input_vector:
                vector with the following magnitude info
                    - Forward/backward (backward as negative)
                    - Left/Right
                    - Up/Down
                    - Pitch
                    - Roll
                    - Yaw
                All of these magnitudes are drfined from -1 to 1. For more
                information on the actual meaning of roll,pitch,and yaw please
                see the markdown file
        '''
        A = np.array(
            [[1, -1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1], [1, -1, 0, 1, 0, -1], [1, 1, 0, 0, 0, -1], [0, 0, 1, 1, -1, 0],
             [0, 0, 1, 1, 1, 0]])
        t = A @ input_vector

        W = 0  # now normalize by finding maximum component
        for i in range(len(t)):
            W = max(W, abs(t[i]))

        if W > 1:  # normalization needed
            print('normalizing')
            for i in range(len(t)):
                t[i] = t[i] / W

        return t
    def setMotorValues(self,vectorDrive):
        '''
        This will set the values of the motors in the ROV and move it in that
        direction
        '''
        #TODO: Implement this method
