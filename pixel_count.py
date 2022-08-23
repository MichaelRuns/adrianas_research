from PIL import Image
import numpy as np

RED_DEF = 255, 0, 0
BLACK_DEF = 0, 0, 0
GREEN_DEF = 0, 255, 0
COLORS = [RED_DEF, GREEN_DEF, BLACK_DEF]

def main():
    '''
    :return: dictionary of red, green, and black pixels
    '''
    assignments = [0, 1, 2]  # list of our choices to pick from
    inverse_assignments = {0: 'red', 1: "green", 2: 'black'} # maps from choice number to actual meaning
    image = np.array(Image.open("/Users/michaelvernau/PycharmProjects/pythonProject/Composite.jpeg").convert('RGB'))  # load image as np array
    results = {} # dictionary to store results
    for row in range(image.shape[0]):  # iterate through row, col
        for col in range(image.shape[1]):
            pixel = tuple(image[row, col, :])  # get pixel tuple(R,G,B)
            assign = min(assignments, key=lambda x: pixel_diff(pixel, COLORS[x]))  # get which color minimizes distance
            assign = inverse_assignments[assign] # formatting
            if assign in results:  # increment dictionary value
                results[assign] = results[assign] + 1
            else:
                results[assign] = 1
    print(results)  #we're done!


def pixel_diff(pixel, color):
    '''
    :param pixel: R,G,B pixel to be evaluated
    :param color: defined color
    :return: measure of difference between pixel and color
    '''
    ret = 0
    for i in [0, 1, 2]:
        ret += (pixel[i] - color[i])**2
    return ret


if __name__ == '__main__':
    main()
