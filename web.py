#coding: utf-8

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from flask import Flask, request
from xmlrpc.client import ServerProxy
from serialize import serialize_image
import cv2
import json


app = Flask(__name__)
server = ServerProxy("http://localhost:5310")

@app.route("/recognize", methods=['POST'])
def recognize():
    files = request.files["image"]
    files.save("temp.png")
    words = server.recognize(serialize_image(cv2.imread("temp.png")))
    return json.dumps({
        "code": 200,
        "msg": "OK",
        "data": words
    })






if __name__ == "__main__":
    app.run()



