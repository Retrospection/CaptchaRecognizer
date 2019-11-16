# coding: utf-8

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from xmlrpc.server import SimpleXMLRPCServer
from resnetCaptchaManager import CaptchaManager


def main():
    captcha_helper = CaptchaManager("ResNet-epoch-060.hdf5")
    print("tensorflow initialized!")
    server = SimpleXMLRPCServer(("localhost", 5310))
    server.register_instance(captcha_helper)
    server.serve_forever()


if __name__ == '__main__':
    main()
