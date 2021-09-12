from PIL import ImageTk
from tkinter import*
from PIL import Image
from tkinter import messagebox
from tkinter.ttk import Checkbutton
from Tools.web import*
from tkhtmlview import HTMLLabel
from Tools.log_db import*

global check
check = False

class Login:
    def __init__(self, root):
        self.root  = root
       
        ## Init frame and button 

        Frame_login = Frame(self.root, bg="#120b26")
        Frame_login.place(x = 300,y = 0, height = 540, width=660)
        
        global image_default_login
        image_default_login = ImageTk.PhotoImage(file = 'images/interfaces/login.png')
        
        logo_default = Label(Frame_login, image = image_default_login )
        logo_default.place( x = 0, y = 0, relheight = 1, relwidth = 1 )

        self.txt_username = Entry(Frame_login, font=("Times New Roman",15), fg = "#8078c4", bg="#120b26",cursor="hand2", highlightcolor = "#b0bde0", highlightbackground = "red", bd = 0)
        self.txt_username.place(x = 180, y = 175, height= 34, width= 326)

        self.txt_password = Entry(Frame_login, font=("Times New Roman",15),fg = "#8078c4", bg="#120b26",cursor="hand2", bd = 0, show = "*")
        self.txt_password.place(x = 180, y = 248, height= 34, width= 326)

        self.forgot_pw = Button(Frame_login, relief = "flat", cursor = "hand2", borderwidth = 0, text = "Forgot your passwork ?", font = ("Times New Roman",12,"bold"), command = contactGmail, fg="#823af7",bg="#120b26", activeforeground = "white", activebackground = "#120b26")
        self.forgot_pw.place(x = 345, y = 285)
        
        # self.abc = HTMLLabel(Frame_login, html = "<h6> <a style='text-decoration: none' href='mailto:someone@example.com' class = 'swapButton'>Forgot password?</a> </h6>")
        # self.abc.place(x = 290, y = 210, height=20, width=200)

        ## Make button login

        self.login_btn = Button(Frame_login, activeforeground = "white", activebackground = "#823af7",command=self.login, text = "Login to your Account", font = ("Times New Roman",12,"bold"),fg="#211c49",bg="#823af7",relief="flat",cursor="hand2",borderwidth=0,width=30)
        self.login_btn.place(x = 190, y = 323)

        self.login_btn = Button(Frame_login, activeforeground = "white", activebackground = "#4d98e1",command=openFB, text = "Login with Facebook", font = ("Times New Roman",12,"bold"),fg="#211c49",bg="#4d98e1",relief="flat",cursor="hand2",borderwidth=0,width=30)
        self.login_btn.place(x = 190, y = 396)

        self.login_btn = Button(Frame_login, activeforeground = "white", activebackground = "#c4acec",command=openGG, text = "Login with Google", font = ("Times New Roman",12,"bold"),fg="#211c49",bg="#c4acec",relief="flat",cursor="hand2",borderwidth=0,width=30)
        self.login_btn.place(x = 190, y = 470)
        
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
                global check
                check = True
                messagebox.showinfo("Welcome","Logged in successfully!",parent = self.root)
            else:
                messagebox.showerror("Error","Invalid username/password!", parent = self.root)

    def display(self):
        s =""
        if self.txt_password !="":
            for i in self.txt_password:
                s += "+"
        return s
def isLoginSuccessfully():
    return check