import numpy as np

class MyImage(object):

    def __init__(self, img_array):
        self.img_array = img_array

    def turn_area_black(self, upper_left, bottom_right):
        """
        :param upper_left:
        :param bottom_right:
        :return:
        """
        image_copy = MyImage.get()
        image_copy[upper_left[0]:bottom_right[0], bottom_right[1]:[1]] = [0, 0, 0, ]  # Place to continue!

        pass

    def adding_squared_smiley_face(self, upper_left, bottom_right, smiley_color):
        # this is noam changing things
        pass

    def blur_certain_area(self, upper_left, bottom_right):
        pass

    def get_img(self):
        return self.img_array
        pass


def image_hist(img_array):
    pass


