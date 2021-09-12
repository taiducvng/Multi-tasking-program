from tkinter import *


def makecenter(root):
    """Because each monitor has different resolutions, we cannot set static values ​​for the display of our dialog box.
    the program is in the middle of the screen, so it is necessary to get the height and width of the screen on each machine, and what we need
    do is take half the screen length minus half the geometry length of the program that is displayed. """
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width,height,x,y))