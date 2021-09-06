from PIL import ImageTk
from tkinter import*
from PIL import Image
from tkinter import messagebox
from tkinter.ttk import Checkbutton
from Tools.web import*
from tkhtmlview import HTMLLabel
from Tools.log_db import*

class Login:
    def __init__(self, root):
        self.root  = root
        self.username = StringVar().set("xxxxxx")
        self.password = StringVar().set("xxxxxx")
        
        ## Init frame and button for login part

        Frame_login = Frame(self.root, bg="#f0f0f0")
        Frame_login.place(x = 500,y = 140, height = 450, width=500)

        self.title = Label(Frame_login, text = "Login", font= ("Georgia", 35, "bold"),fg="#6e6aba",bg="#f0f0f0").place(x = 65, y = 30)
        self.desc = Label(Frame_login, text = "Join us with", font = ("UTM-Avo",12,"bold"),fg="#6e6aba",bg="#f0f0f0").place(x = 70, y = 100)
        
        
        self.lab_username = Label(Frame_login, text = "Username*", font = ("Times New Roman",12,"bold"),fg="#000000",bg="#f0f0f0").place(x = 70, y = 145)
        self.txt_username = Entry(Frame_login, font=("Times New Roman",15),bg="white",cursor="hand2")
        self.txt_username.place(x = 70, y = 170, height= 35, width= 350)

        self.lab_password = Label(Frame_login, text = "Password*", font = ("Times New Roman",12,"bold"),fg="#000000",bg="#f0f0f0").place(x = 70, y = 205)
        self.txt_password = Entry(Frame_login, font=("Times New Roman",15), bg="white",cursor="hand2",fg= "#000000")
        self.txt_password.place(x = 70, y = 230, height= 35, width= 350)

        self.lab_password_forgot = HTMLLabel(Frame_login, html="<h6> <a style='text-decoration: none' href='mailto:someone@example.com'>Forgot password?</a> </h6>").place(x = 305, y = 210, height=20, width=200)
        self.lab_ques = Label(Frame_login, text = "Join with ", font = ("Times New Roman",12,"bold"),fg="#000000",bg="#f0f0f0").place(x = 70, y = 270)
        
        ## Make logo and action when you click

        self.fb_img = PhotoImage(file="images/fb.png")
        self.github_img = PhotoImage(file="images/github.png")
        self.gg_img = PhotoImage(file="images/google.png")
        
        self.github_btn = Button(Frame_login,relief="flat",cursor="hand2",borderwidth=0,image=self.github_img,command=openGH)
        self.github_btn.place(x = 70, y = 300)

        self.fb_btn = Button(Frame_login,relief="flat",cursor="hand2",borderwidth=0,image=self.fb_img,command=openFB)
        self.fb_btn.place(x = 105, y = 300)

        self.gg_btn = Button(Frame_login,relief="flat",cursor="hand2",borderwidth=0,image=self.gg_img, command=openGG)
        self.gg_btn.place(x = 140, y = 300)

        ## Make button login

        self.login_btn = Button(self.root, command=self.login, text = "    Login here    ", font = ("Times New Roman",12,"bold"),fg="#f0f0f0",bg="#6e6aba",relief="flat",cursor="hand2",borderwidth=0).place(x = 800, y = 530)
        

        ## Check login
        
    ## Action for login

    def login(self):
        if self.txt_username.get() == "" or self.txt_password.get() == "":
            if self.txt_username.get() == "":
                messagebox.showerror("Error","Please, enter your username!", parent = self.root)
            else:
                messagebox.showerror("Error","Please, enter your password!", parent = self.root)
        
        else:
            s1 = self.txt_username.get()
            s2 = encode(self.txt_password.get())
            a = [s1, s2]
            if checkDB_Login(a) == True:
                messagebox.showinfo("Welcome","Logged in successfully!",parent = self.root)
            else:
                messagebox.showerror("Error","Invalid username/password!", parent = self.root)

    def display(self):
        s =""
        if self.txt_password !="":
            for i in self.txt_password:
                s += "+"
        return s
