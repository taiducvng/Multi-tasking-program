from Tools import*
from tkinter import*
from tkinter import messagebox

from Tools.Button import*
from Tools.CPU import*

class Home:
    def __init__(self, root):
        self.root  = root
        
        Frame_home = Frame(self.root, bg="#f0f0f0")
        Frame_home.place(x = 500,y = 140, height = 450, width=500)

        ## Frame for CPU
        
        _info_ = psutil.virtual_memory()
        FrameButton_styleOne(Frame_home, 0, 50, text_in_labe="Virtual Memory", text_in_box=f"Total: {get_size(_info_.total)} \nAvailable: {get_size(_info_.available)}\nUsed: {get_size(_info_.used)}\nPercentage: {get_size(_info_.percent)}%", color="#9d70ff")
           
 