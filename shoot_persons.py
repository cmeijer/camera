#!/usr/bin/python3
import time

# Wait for the system to finish booting before importing other packages.
time.sleep(10)

import random
import string
from os import path, remove
from shutil import copyfile
import images_dao
import detections_dao

import camera_supplier
from person_detection import detect_person_from_files
from settings import is_test_mode, temp_data_dir, detected_data_dir


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
        now = time.time()
        if now > next_shot_time:
            next_shot_time += interval
            file_name = '{}{:0>10}.jpg'.format(random_word, shots_taken)
            current_path = path.join(temp_data_dir, file_name)
            camera.capture(current_path)
            images_dao.save_or_update(file_name, now)
            shots_taken += 1

            if not previous_path is None:
                is_detected = detect_person_from_files(previous_path, current_path)
                if is_detected:
                    print('detected... {}'.format(current_path))
                    detected_path = path.join(detected_data_dir, file_name)
                    copyfile(current_path, detected_path)
                    detections_dao.save_or_update(file_name, 'movement')

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
    make_shots(10 ** 10)
