import cv2

class image_utils:
    def __init__(self):
        pass

    def to_grayscale(self, image_path):
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray_image

    def resize(self, image_path, width, height):
        image = cv2.imread(image_path)
        resized_image = cv2.resize(image, (width, height))
        return resized_image

    def rotate(self, image_path, angle):
        image = cv2.imread(image_path)
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated_image = cv2.warpAffine(image, M, (w, h))
        return rotated_image

if __name__ == "__main__":
    image_utils() 