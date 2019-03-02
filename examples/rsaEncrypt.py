#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rsa

def doEncrypt(plainMessage):
    # rsa.encrypt(plainMessage, )
    pass

def doDecrypt():

    pass


if __name__ == "__main__":

    message = "hello world"

    pubkey = ""
    # 加密
    cipherMessage = rsa.encrypt(message.encode(), pubkey)
    print cipherMessage

