#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import eel


eel.init("web")  # EEL initialization


@eel.expose
def binary(number):
    return bin(int(number)).replace("0b", "")


@eel.expose
def octal(number):
    return oct(int(number)).replace("0o", "")


@eel.expose
def hexadecimal(number):
    return str(hex(int(number)).replace("0x", "")).upper()


eel.start("main.html", size=(700, 400))  # Starting the App