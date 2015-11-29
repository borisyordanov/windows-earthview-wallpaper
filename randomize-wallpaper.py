import os, random
from change_wallpaper import change_wallpaper 

file = random.choice(os.listdir(os.path.normpath(os.getcwd() + "\\images\\")))

change_wallpaper(file)