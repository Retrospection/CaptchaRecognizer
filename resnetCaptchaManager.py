#coding: utf-8

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from keras.models import load_model
from keras.preprocessing.image import img_to_array
import numpy as np

from serialize import deserialize_image


CLASSES_LIST = [chr(ord('a')+x) for x in range(26)] + [str(x) for x in range(10)]

REVERSE_CLASSES_DICT = {index: v for index, v in enumerate(CLASSES_LIST)}

NUM_CLASSES = len(CLASSES_LIST)

CHAR_NUMBERS = 5


class CaptchaManager:

    def __init__(self, model_file, label_file=None):
        self.model_file = model_file
        self.model = load_model(self.model_file)

    def _recognize(self, image):
        image = img_to_array(image) / 255.0
        image = image[np.newaxis, :]
        label = self.model.predict(image)
        label = np.squeeze(label)
        return ''.join([REVERSE_CLASSES_DICT[np.argmax(label[pos * NUM_CLASSES:(pos + 1) * NUM_CLASSES])] for pos in range(CHAR_NUMBERS)])

    def recognize(self, image_array):
        try:
            image = deserialize_image(image_array.data)
            result = self._recognize(image)
        except Exception as e:
            print(e)
        return result