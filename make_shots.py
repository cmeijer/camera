from settings import is_test_mode
import time
import camera_supplier


def make_shots(number, interval=1):
    shots_taken = 0
    next_shot_time = time.time()
    camera = camera_supplier.get_camera(is_test_mode)
    while number > shots_taken:
        if time.time() > next_shot_time:
            next_shot_time += interval
            camera.capture('im{:0>6}.jpg'.format(shots_taken))
            shots_taken += 1
