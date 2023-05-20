import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import PIL
from PIL import Image

class MyImage(object):

    def __init__(self, img_array):
        self.img_array = img_array

    def turn_area_black(self, upper_left, bottom_right):
        image_copy = self.img_array
        image_copy[upper_left[0]:bottom_right[0], upper_left[1]:bottom_right[1]] = [0, 0, 0]
        MyImage.present_image(image_copy)


    def adding_squared_smiley_face(self, upper_left, bottom_right, smiley_color):
        # this is noam changing things
        pass

    def blur_certain_area(self, upper_left, bottom_right):

        pass

    def present_image(self, array_data):
        plt.imshow(array_data, interpolation='nearest')
        plt.show()

    # def preset_image(self, path_img):
    #     img_var = img.imread(path_img)
    #     plt.imshow(img_var)
    #     plt.show()

def image_hist(img_array):
    pass

if __name__ == "__main__":

    path = "C:\\devl\\work\\6130 Python\\course_6130\\EX4\\low_resu_flower.jpg"
    image = Image.open(path)
    im_copy = image.copy()
    image_array = np.asarray(im_copy)
    image_array.setflags(write=1)

    img_class = MyImage(image_array)
    img_class.turn_area_black([10, 100], [100, 10])
    # img_class.present_image(path)


