import os
import ctypes

def change_wallpaper(filename):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.normpath(os.getcwd() + "\\images\\" + filename) , 0)