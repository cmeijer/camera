def get_camera(is_test_mode=False):
    if is_test_mode:
        import dummy_camera as picamera
    else:
        import picamera

    return picamera.PiCamera()
