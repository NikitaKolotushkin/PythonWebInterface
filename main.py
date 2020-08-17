#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import eel


eel.init("web")  # EEL initialization


@eel.expose
def binary(number):
    """This function converts the entered number from the decimal system to binary"""
    return bin(int(number)).replace("0b", "")


@eel.expose
def octal(number):
    """This function converts the entered number from the decimal system to octal"""
    return oct(int(number)).replace("0o", "")


@eel.expose
def hexadecimal(number):
    """This function converts the entered number from the decimal system to hexadecimal"""
    return str(hex(int(number)).replace("0x", "")).upper()


eel.start("main.html", size=(700, 400))  # Starting the App