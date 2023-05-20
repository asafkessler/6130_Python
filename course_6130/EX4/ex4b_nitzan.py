# 315535518, 316539196
# 10

import numpy as np
import matplotlib.pyplot as screen
import matplotlib.image as img
from scipy import misc
from scipy import ndimage

class MyImage(object):

    def __init__(self, img_array):
        """
        This is the constractor function.
        :param img_array: gets an image array and sets it as a local variable.
        :type img_array: numpy N dim Array.
        """
        self.img_array = img_array

    def turn_area_black(self, upper_left, bottom_right):
        """
        This function turns an area in the image black.
        :param upper_left: A point (x,y) representing the upper left corner of the black area
        :type upper_left: List
        :param bottom_right: A point (x,y) representing the upper right corner of the black area
        :type bottom_right: List
        :return: (pass)
        :rtype: (pass)
        """
        self.img_array = self.img_array.copy()
        self.img_array[upper_left[1]:bottom_right[1],upper_left[0]:bottom_right[0]] = [0,0,0]

        'Just Trying to show the image after modification '
        screen.imshow(self.img_array)
        screen.show()

    def adding_squared_smiley_face(self, upper_left, bottom_right, smiley_color):
        """
        This function create a smily face. It does it my coloring an area in a given colour
        and turns the other pixels black to create the smiley face.

        :param smiley_color: colour of the smiley face.
        :param upper_left: upper left point of the smiley.
        :type upper_left: List (x,y).
        :param bottom_right: bottom right point of the smiley.
        :type bottom_right: List (x,y).
        :param smiley_color: colour of the smiley face.
        :type smiley_color: RGB value List
        :return: (pass)
        :rtype: (pass)
        """
        self.img_array = self.img_array.copy()
        self.img_array[upper_left[1]:bottom_right[1], upper_left[0]:bottom_right[0]] = smiley_color

        # mouth: mul(mouth bottom left),mbr(mouth bottom right)

        mul = [int(upper_left[0] + 0.25 * (bottom_right[0] - upper_left[0])),
               int(upper_left[1] + 0.65 * (bottom_right[1] - upper_left[1]))]
        mbr = [int(bottom_right[0] - 0.25 * (bottom_right[0] - upper_left[0])),
               int(upper_left[1] + 0.75 * (bottom_right[1] - upper_left[1]))]
        self.im[mul[1]:mbr[1], mul[0]:mbr[0]] = [0, 0, 0]

        # eyes: elul(left upper corner),elbr(right bottom corner), for each eye
        elul = [int(upper_left[0] + 0.25 * (bottom_right[0] - upper_left[0])),
                int(upper_left[1] + 0.2 * (bottom_right[1] - upper_left[1]))]
        elbr = [int(bottom_right[0] - 0.6 * (bottom_right[0] - upper_left[0])),
                int(upper_left[1] + 0.3 * (bottom_right[1] - upper_left[1]))]
        self.im[elul[1]:elbr[1], elul[0]:elbr[0]] = [0, 0, 0]
        elul = [int(upper_left[0] + 0.6 * (bottom_right[0] - upper_left[0])),
                int(upper_left[1] + 0.2 * (bottom_right[1] - upper_left[1]))]
        elbr = [int(bottom_right[0] - 0.25 * (bottom_right[0] - upper_left[0])),
                int(upper_left[1] + 0.3 * (bottom_right[1] - upper_left[1]))]
        self.im[elul[1]:elbr[1], elul[0]:elbr[0]] = [0, 0, 0]

    def blur_certain_area(self, upper_left, bottom_right):
        """
        This function blurs an area in the image
        :param upper_left: upper left point of the blurred area
        :type upper_left: List (x,y)
        :param bottom_right:
        :type bottom_right: List (x,y)
        :return: (pass)
        :rtype: (pass)
        """
        self.img_array = self.img_array.copy()

        spliced_area = self.img_array[upper_left[1]:bottom_right[1], upper_left[0]:bottom_right[0]]

        blurred_area = ndimage.uniform_filter(spliced_area, size=(1000, 1000, 1))

        self.img_array[upper_left[1]:bottom_right[1], upper_left[0]:bottom_right[0]] = blurred_area

    def get_img(self):
        """
        This function returns the array of the current image after modifications.
        :return: image array.
        :rtype: numpy N Dim Array
        """
        return self.img_array

def image_hist(img_array):
    """
    This function counts the amount of appearances of each colour in the
    RGB spectrum. Red Green Blue amounts in a given image array.
    :param img_array: a given image data array
    :type img_array: numpy N Dim Array
    :return: it returns a histogram for each colour(rgb value) in the given image.
    :rtype: Array
    """

    R = [0 for i in range(0, 256)]
    G = [0 for i in range(0, 256)]
    B = [0 for i in range(0, 256)]
    for list in img_array:
        for sublist in list:
            R[sublist[0]] += 1
            G[sublist[1]] += 1
            B[sublist[2]] += 1
    return np.array(R), np.array(G), np.array(B)


if __name__ == "__main__":
    np_img_array = img.imread(R".\low_resu_flower.jpg")
    # screen.imshow(np_img_array)
    # screen.show()
    # img = misc.face()
    # image_sizes = np_img_array.shape
    # image_copy_class = MyImage(np_img_array)
    # image_copy_class.turn_area_black([10, 300], [300, 10])
    print(image_hist(np_img_array))
