from keras.preprocessing import image


def detect_person_from_files(image_file1, image_file2):
    x1 = load_image(image_file1)
    x2 = load_image(image_file2)
    return True


def load_image(image_file):
    img = image.load_img(image_file, target_size=(224, 224))
    return image.img_to_array(img)
