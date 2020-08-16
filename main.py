#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import eel


@eel.expose
def Converter(number):

    binary = bin(number).replace("0b", "")
    octal = oct(number).replace("0o", "")
    hexadecimal = str(hex(number).replace("0x", "")).upper()

    return number

    # print("Bin system: ", binary)
    # print("Oct system: ", octal)
    # print("Hex system: ", hexadecimal)

eel.init("web")
eel.start("main.html", size=(700, 700))