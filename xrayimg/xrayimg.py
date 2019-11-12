# coding: utf-8

import fabio
import numpy as np
import os
from PIL import Image

class XimgConverter:
    PNG_MAX = 255
    def __init__(self, path_to_img):
        self.root = os.path.splitext(path_to_img)[0]
        self.img = fabio.open(path_to_img)
        self.pixel = self.img.data

    def to_csv(self):
        np.savetxt(self.root + ".csv", self.pixel, fmt="%d")

    def to_png(self):
        image = Image.fromarray(self.PNG_MAX * (1 - self.pixel/self.pixel.max()))
        image.convert("RGB").save(self.root + ".png")
