import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, width, height, color):
        self. width = width
        self.height = height
        self.color = color

        # Create a 3d numpy array of zeros, the replace the zeros(black pixels) with yellow pixels
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        # replace zeros within the array with different values
        self.data[:] = self.color

    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)