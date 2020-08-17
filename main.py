#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import eel
eel.init("web")

# @eel.expose
def Converter(number):

    binary = bin(int(number)).replace("0b", "")
    octal = oct(int(number)).replace("0o", "")
    hexadecimal = str(hex(int(number)).replace("0x", "")).upper()

    return number

    # print("Bin system: ", binary)
    # print("Oct system: ", octal)
    # print("Hex system: ", hexadecimal)

@eel.expose
def binary(number):
    return bin(int(number)).replace("0b", "")

@eel.expose
def Octalf(number):
    return oct(int(number)).replace("0o", "")

@eel.expose
def hexadecimal(number):
    return str(hex(int(number)).replace("0x", "")).upper()


eel.start("main.html", size=(700, 700))