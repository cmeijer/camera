from keras.preprocessing import image
import scipy.ndimage as ndimage
import numpy as np


def detect_person_from_files(image_file1, image_file2):
    x1 = load_image(image_file1) / 255
    x2 = load_image(image_file2) / 255
    value = np.sum(compute2(x1, x2))
    return value > 3


def compute1(previous, current): #2
    """ Should get .55 precision and 0.4 recall with a threshold of 2. """
    difference = current - previous
    return np.power(difference, 4)


def compute2(previous, current):
    """ Should get .64 precision and .94 recall with a threshold of 3. """
    difference = np.power(current - previous, 2)
    return 3 * np.maximum(difference - 10*np.std(difference), np.zeros_like(difference))


def compute(previous, current):
    """ Should get .38 precision and .14 recall with a threshold of 5 :-( """
    difference = np.power(current - previous, 2)
    std = np.std(difference)
    smoothed = ndimage.gaussian_filter(difference, sigma=(5, 5, 0), order=0)
    return 3 * np.maximum(smoothed - 3*std, np.zeros_like(difference))


def load_image(image_file):
    img = image.load_img(image_file, target_size=(224, 224))
    return image.img_to_array(img)
