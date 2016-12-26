import unittest
from person_detection import detect_person_from_files
from settings import test_data_dir
from os import path
from keras.preprocessing.image import list_pictures

class PersonDetectionSuite(unittest.TestCase):
    """ Tests. """
    def test_detect_from_files(self):
        """ It should at least run without exceptions with two valid file paths. """
        motion_detection_test_dir = path.join(test_data_dir, 'motion_detection')
        images = list_pictures(motion_detection_test_dir)
        for i, image in enumerate(images):
            if i == 0:
                continue

            previous_image = images[i-1]
            detect_person_from_files(previous_image, image)

