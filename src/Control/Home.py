from tkinter.ttk import Style
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
from Tools.Button import*
from Tools.get_info import*
from threading import  Thread

class Home:
    def __init__(self, root):
        self.root  = root
        
        ## Frame for CPU

        Frame_home = Frame(self.root, bg="#120b26")
        Frame_home.place(x = 300,y = 0, height = 540, width=660)
        
        global image_default_home
        image_default_home = ImageTk.PhotoImage(file = 'images/interfaces/home.png')
        logo_default = Label(Frame_home, image = image_default_home )
        logo_default.place( x = 0, y = 0, relheight = 1, relwidth = 1 )
    
        self.label_cpu = Label(Frame_home, text = ' M E M O R Y ', font = ("Georgia",20,"bold"), bg="#1c1734", fg = "#c9b9e3", width=12).place(x = 65, y = 335)
        
        ## Display

        self.label_hours = Label(Frame_home, text = "", bg = "#1c1734", fg = "#c9b9e3", font = ("Georgia",40,"bold"))
        self.label_hours.place(x = 270, y = 70)
        self.label_minutes = Label(Frame_home, text = "", bg = "#1c1734", fg = "#c9b9e3", font = ("Georgia",40,"bold"))
        self.label_minutes.place(x = 410, y = 70)
        self.label_seconds = Label(Frame_home, text = "", bg = "#1c1734", fg = "#c9b9e3", font = ("Georgia",40,"bold"))
        self.label_seconds.place(x = 535, y = 70)

        self.label_date = Label(Frame_home, text = "", bg = "#120b26", fg = "#c9b9e3", font = ("Microsoft Sans Serif",40,"bold"))
        self.label_date.place(x = 105, y = 80)
        self.label_month = Label(Frame_home, text = "", bg = "#120b26", fg = "#c9b9e3", font = ("Microsoft Sans Serif",40,"bold"))
        self.label_month.place(x = 105, y = 140)
        self.label_year = Label(Frame_home, text = "", bg = "#120b26", fg = "#c9b9e3", font = ("Microsoft Sans Serif",40,"bold"))
        self.label_year.place(x = 105, y = 200)

        t_1 = Thread(target = self.getClock)
        t_1.start()

        ## Battery

        self.label_battery = Label(Frame_home, text = "", bg = "#1c1734", fg = "#c9b9e3", font = ("Microsoft Sans Serif",25,"bold"))
        self.label_battery.place(x = 450, y = 395)
        t_2 = Thread(target = self.getBattery)
        t_2.start()

        ## CPU

        self.label_cpu = Label(Frame_home, text = "", bg = "#120b26", fg = "#c9b9e3", font = ("Microsoft Sans Serif", 15,"bold"))
        self.label_cpu.place(x = 75, y = 380)
        t_3 = Thread(target = self.getCPU)
        t_3.start()

        
    def getClock(self):
        h = str(strftime("%H"))
        m = str(strftime("%M"))
        s = str(strftime("%S"))

        dd = str(strftime("%d")) 
        mm = str(strftime("%m"))
        yy = str(strftime("%y"))  

        self.label_hours.config(text = h)
        self.label_minutes.config(text = m)
        self.label_seconds.config(text = s)
        self.label_date.config(text = dd)
        self.label_month.config(text = mm)
        self.label_year.config(text = yy)
        self.label_hours.after(100,self.getClock)
    
    def getCPU(self):
        _info_ = psutil.virtual_memory()
        total = get_size(_info_.total)
        avail = get_size(_info_.available)
        used = get_size(_info_.used)
        per = get_size(_info_.percent)
        self.label_cpu.config(text = f"Total: {total}B\nAvailable: {avail}B\nUsed: {used}B\nPercentage: {per}%")
        self.root.after(20,self.getCPU)
    
    def getBattery(self):
        battery = psutil.sensors_battery()
        per = battery.percent
        self.label_battery.config(text = str(per) + '%')
        self.label_battery.after(100,self.getBattery)
    
     

        
        