from PIL import ImageTk
from tkinter import*
from PIL import Image
from Tools.Button import*
from Tools.web import*

class AboutMe:
    def __init__(self, root):
        self.root  = root
      
        ## Init Frame and button 
       
        Frame_about = Frame(self.root, bg="#120b26")
        Frame_about.place(x = 300, y = 0, height = 540, width=660)

        global background
        global bt1_img, bt_two_img, bt3_img, bt4_img
        background = PhotoImage(file=f"images/interfaces/About.png")
        self.background = Label(Frame_about, image = background).place(x = 0, y = 0, relheight = 1, relwidth = 1 )

        self.facebook = Button(Frame_about,relief="flat",cursor="hand2",borderwidth=0,command=contactFB, bg = "#561d98", text = "facebook", font = ("Georgia",18,"bold"), activebackground="#561d98")
        self.facebook.place(x = 80, y =190)

        self.github = Button(Frame_about,height = 1,relief="flat",cursor="hand2",borderwidth=0,command=contactGithub, bg = "#b488fd", text = "github", activebackground="#b488fd", font = ("Georgia", 30, "bold"))
        self.github.place(x = 130, y = 415)

        self.gmail = Button(Frame_about,height = 1,relief="flat",cursor="hand2",borderwidth=0, bg = "#eb78bb", text = "Google Mail", activebackground="#eb78bb", font = ("Georgia", 25, "bold"))
        self.gmail.place(x = 325, y = 190)

        self.LinkIn = Button(Frame_about,height = 1,relief="flat",cursor="hand2",borderwidth=0,command=contactLinkIn, bg = "#43289e", text = "LinkedIn", activebackground="#43289e", font = ("Georgia", 25, "bold"))
        self.LinkIn.place(x = 420, y = 430)

        
