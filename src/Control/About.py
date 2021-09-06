from tkinter.font import BOLD
from PIL import ImageTk
from tkinter import*
from PIL import Image
from tkinter import messagebox
from tkinter.ttk import Checkbutton
from Tools.Button import*
from Tools.web import*

class AboutMe:
    def __init__(self, root):
        self.root  = root
      
        ## Init Frame and button for aboutme-part
       
        Frame_about = Frame(self.root, bg="#f0f0f0")
        Frame_about.place(x = 500,y = 140, height = 450, width=500)

        self.title = Label(Frame_about, text = "Login", font= ("Georgia", 35, "bold"),fg="#6e6aba",bg="#f0f0f0").place(x = 65, y = 30)
        self.desc = Label(Frame_about, text = "Join us with", font = ("UTM-Avo",12,"bold"),fg="#6e6aba",bg="#f0f0f0").place(x = 70, y = 100)
        

        self.bt1_img = PhotoImage(file="images/buttons/bt1.png")
        self.bt_two_img = PhotoImage(file="images/bt2.png")
        self.bt3_img = PhotoImage(file="images/bt3.png")
        self.bt4_img = PhotoImage(file="images/bt4.png")

        self.bt1_btn = Button(Frame_about,image=self.bt1_img,relief="flat",cursor="hand2",borderwidth=0,command=contactFB).place(x = 55, y = 50)

        self.bt_two_btn = Button(Frame_about,relief="flat",cursor="hand2",borderwidth=0,image=self.bt_two_img,command=contactLinkIn).place(x = 295, y = 50)

        self.bt3_btn = Button(Frame_about,relief="flat",cursor="hand2",borderwidth=0,image=self.bt3_img,command=openFB).place(x = 55, y = 300)

        self.bt4_btn = Button(Frame_about,relief="flat",cursor="hand2",borderwidth=0,image=self.bt4_img,command=contactGithub).place(x = 295, y = 180)
       
 