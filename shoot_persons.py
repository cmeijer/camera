import random
import string
import time
from os import path, remove

import camera_supplier
from person_detection import detect_person_from_files
from settings import is_test_mode, test_data_dir


def make_shots(number, interval=1):
    random_word = generate_random_word(8)
    shots_taken = 0
    next_shot_time = time.time()
    camera = camera_supplier.get_camera(is_test_mode)
    previous_path = None
    previous_is_detected = None
    is_detected = None
    while number > shots_taken:
        print('shots taken is {}'.format(shots_taken))
        if time.time() > next_shot_time:
            next_shot_time += interval
            current_path = path.join(test_data_dir, '{}{:0>6}.jpg'.format(random_word, shots_taken))
            camera.capture(current_path)
            shots_taken += 1

            if not previous_path is None:
                is_detected = detect_person_from_files(previous_path, current_path)
                if is_detected:
                    print('detected... {}'.format(current_path))

            remove_undetected_image(is_detected, previous_is_detected, previous_path)

            previous_path = current_path
            previous_is_detected = is_detected


def generate_random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def remove_undetected_image(is_detected, previous_is_detected, previous_path):
    if is_detected is None or previous_is_detected is None or previous_path is None:
        return

    if (not is_detected) and (not previous_is_detected):
        print('removing {}'.format(previous_path))
        remove(previous_path)


if __name__ == '__main__':
    make_shots(10000)
