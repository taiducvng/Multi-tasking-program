import tkinter as tk
from tkinter import font
from tkinter.font import BOLD
import tkinter.ttk as ttk

def FrameButton_styleOne(root, size_X = 0, size_Y = 0, text_in_labe ="text", text_in_box = "text", color = "red"):
    style = ttk.Style()
    style.theme_create('appstyle', parent='alt',
                    settings={
                        'TLabelframe': {
                            'configure': {
                                'background': color,
                                'font': 'Microsoft Sans Serif'
                            }
                        },
                        'TLabelframe.Label': {
                            'configure': {
                                'background': color    # uncomment this to make even label red
                                }
                        }
                    }
                    )
    style.theme_use('appstyle')
    style.configure('Red.TLabelframe.Label',font = ('Georgia',12,'bold')) # Fix style for add font
    labelframe = ttk.LabelFrame(root, text = text_in_labe,style = "Red.TLabelframe")
    labelframe.place(x = size_X, y = size_Y)
    
    left = tk.Label(labelframe, text=text_in_box, font = ("Microsoft Sans Serif",12))
    left.pack()
   

   


