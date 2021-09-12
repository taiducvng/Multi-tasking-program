from tkinter import*
from tkinter import Button, font
from tkinter.font import BOLD
import tkinter.ttk as ttk
from tkhtmlview import HTMLLabel
from tkhtmlview import HTMLText

def frameButton(frame, xx, yy, text, backgroundcolor, foregroundcolor, cmd, images):
        
    def IN(e):
        button['background'] = backgroundcolor 
        button['foreground']= '#120b26'  

    def OUT(e):
        button['background'] = foregroundcolor
        button['foreground']= '#120b26'

    button = Button(frame, text = text, width = 30, height = 2, fg = '#120b26', border = 0, bg = foregroundcolor, activeforeground = '#120b26', activebackground = backgroundcolor, command=(cmd), font = ("Microsoft Sans Serif", 12, "bold"), cursor="hand2", borderwidth=0, image = images )                
    button.bind("<Enter>", IN)
    button.bind("<Leave>", OUT)
    button.place(x = xx, y = yy)
