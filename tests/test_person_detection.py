import unittest
from person_detection import detect_person_from_files
from settings import temp_data_dir
from os import path
from keras.preprocessing.image import list_pictures
from time import time


class PersonDetectionSuite(unittest.TestCase):
    """ Tests. """

    def test_detect_from_files_no_exc(self):
        """ Should run without exceptions with two valid file paths. """
        self.detect_in_images()

    def test_detect_from_files_quick(self):
        """ Should run under 1/10th of a second per image. """
        print('\nSpeed test: ', end='')
        n_images = len(self.images) - 1
        start_time = time()

        self.detect_in_images()

        taken_per_image = (time() - start_time) / n_images
        print('{} seconds per image for {} images'.format(taken_per_image, n_images))
        assert taken_per_image < 0.1

    def test_detect_from_files_recall(self):
        """ Should have at least 90% recall. """
        print('\nRecall test: ', end='')
        results = self.detect_in_images()

        retrieved = 0
        total_positive = 0

        for i in range(len(results)):
            annotation = self.annotations[i]
            result = results[i]
            if annotation == self.positive_annotation:
                total_positive += 1

                if result:
                    retrieved += 1

        recall = retrieved / total_positive
        print('Retrieved {} of {} positives ({} recall)'.format(retrieved, total_positive, recall))
        assert recall > 0.9

    def test_detect_from_files_precision(self):
        """ Should have at least 50% precision. """
        print('\nPrecision test: ', end='')
        results = self.detect_in_images()

        true_positive = 0
        total_positive = 0

        for i in range(len(results)):
            annotation = self.annotations[i]
            result = results[i]
            if result:
                total_positive += 1

                if annotation == self.positive_annotation:
                    true_positive += 1

        precision = true_positive / total_positive
        print('True positive {} of {} positives ({} precision)'.format(true_positive, total_positive, precision))
        assert precision > 0.5

    def detect_in_images(self):
        """ Run detection method over all images and return the results. """
        results = []
        for i, image in enumerate(self.images):
            if i == 0:
                continue

            previous_image = self.images[i - 1]
            results.append(detect_person_from_files(previous_image, image))
        return results

    def setUp(self):
        self.motion_detection_test_dir = path.join(temp_data_dir, 'motion_detection')
        self.images = list_pictures(self.motion_detection_test_dir)
        with open(path.join(self.motion_detection_test_dir, 'annotations')) as f:
            self.annotations = [line.split(' ')[1].strip('\n') for line in f]
        self.positive_annotation = 'person_visible'
        self.negative_annotation = 'no_person_visible'
