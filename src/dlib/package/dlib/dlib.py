##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
# Since: v1.0.0
##

import dlib


##
# Dlib class
# This class is a wrapper for Digital Library (Dlib)
#
# @see: http://dlib.net/
##
class Dlib:

    def __init__(self):
        print('[INFO] Dlib - Initialising frontal face detector...')
        self._frontal_face_detector = dlib.get_frontal_face_detector()

    ##
    # Method frontal_face_detector()
    # Method to return Dlib frontal_face_detector
    #
    # @param frame - image frame
    # @param up_sample - enlarge image for better capture (0-1)
    #
    # @return Array of detection(s)
    ##
    def frontal_face_detector(self, frame, up_sample):
        return self._frontal_face_detector(frame, up_sample)
