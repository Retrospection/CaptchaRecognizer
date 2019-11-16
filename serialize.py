# coding: utf-8

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import cv2
import numpy as np


def serialize_image(image: np.ndarray) -> bytes:
    img_encode = cv2.imencode('.jpg', image)[1]

    data_encode = np.array(img_encode)
    return data_encode.tostring()


def deserialize_image(string: bytes) -> np.ndarray:
    image = np.asarray(bytearray(string), dtype="uint8")
    return cv2.imdecode(image, cv2.IMREAD_COLOR)
