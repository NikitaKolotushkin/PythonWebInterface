#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import eel


eel.init("web")  # EEL initialization


@eel.expose
def binary(number):
    """This function converts the entered number from the decimal system to binary"""
    return f"{int(number):b}"


@eel.expose
def octal(number):
    """This function converts the entered number from the decimal system to octal"""
    return f"{int(number):o}"


@eel.expose
def hexadecimal(number):
    """This function converts the entered number from the decimal system to hexadecimal"""
    return f"{int(number):x}"


eel.start("main.html", size=(700, 400))  # Starting the App
