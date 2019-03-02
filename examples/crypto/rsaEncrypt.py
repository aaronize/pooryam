#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rsa


def do_encrypt(plain_data):
    # rsa.encrypt(plainMessage, )
    pass


def do_decrypt(cipher_data):

    pass


if __name__ == "__main__":

    message = "hello world"

    pubkey = ""
    # 加密
    cipherMessage = rsa.encrypt(message.encode(), pubkey)
    print cipherMessage

