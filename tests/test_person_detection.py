import unittest
from person_detection import detect_person_from_files
from settings import test_data_dir
from os import path
from keras.preprocessing.image import list_pictures


class PersonDetectionSuite(unittest.TestCase):
    """ Tests. """

    def test_detect_from_files(self):
        """ Should run without exceptions with two valid file paths. """
        for i, image in enumerate(self.images):
            if i == 0:
                continue

            previous_image = self.images[i - 1]
            detect_person_from_files(previous_image, image)

    def setUp(self):
        self.motion_detection_test_dir = path.join(test_data_dir, 'motion_detection')
        self.images = list_pictures(self.motion_detection_test_dir)
        with open(path.join(self.motion_detection_test_dir, 'annotations')) as f:
            self.annotations = [line.split(' ')[1] for line in f]
