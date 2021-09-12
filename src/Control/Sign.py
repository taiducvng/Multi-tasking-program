from tkinter.font import BOLD
from PIL import ImageTk
from tkinter import*
from PIL import Image
from tkinter import messagebox
from Tools.log_db import*

class Sign:
    def __init__(self, root):
        self.root  = root

        ## Init frame and button

        Frame_sign = Frame(self.root, bg="#120b26")
        Frame_sign.place(x = 300,y = 0, height = 540, width=660)

        global image_default_signup
        image_default_signup = ImageTk.PhotoImage(file = 'images/interfaces/signup.png')
        logo_default = Label(Frame_sign, image = image_default_signup )
        logo_default.place( x = 0, y = 0, relheight = 1, relwidth = 1 )

        self.txt_name = Entry(Frame_sign, font=("Times New Roman",15), fg = "#8078c4", bg = "#120b26", cursor="hand2", bd = 0, width = 10)
        self.txt_name.place(x = 180, y = 175, height= 34, width= 326)    

        self.txt_username = Entry(Frame_sign, font=("Times New Roman", 15), fg = "#8078c4", bg = "#120b26", cursor = "hand2", bd = 0)
        self.txt_username.place(x = 180, y = 248, height= 34, width= 326)

        self.txt_password = Entry(Frame_sign, font=("Times New Roman",15), fg = "#8078c4",bg = "#120b26", cursor = "hand2", show = "*", bd = 0, highlightbackground = "#b0bde0")
        self.txt_password.place(x = 180, y = 321, height= 34, width= 326)

        self.txt_password_comfirm = Entry(Frame_sign, font = ("Times New Roman",15), fg = "#8078c4",bg = "#120b26", cursor = "hand2", show = "*", bd = 0)
        self.txt_password_comfirm.place(x = 180, y = 394, height= 34, width= 326)
    
        ## Make sign in button
        
        self.sign_btn = Button(Frame_sign, activebackground="#823af7", activeforeground="white",command=self.sign, text = "Submit", font = ("Times New Roman",12,"bold"), fg = "#211c49", bg = "#823af7", relief = "flat", cursor = "hand2", borderwidth = 0, width = 38)
        self.sign_btn.place(x = 156, y = 470)
        
    ## Action for Sign in

    def sign(self):

        if self.txt_name.get() != "" and self.txt_username.get() != "" and self.txt_password.get() != "" and self.txt_password_comfirm !="":
            if self.txt_password.get() != self.txt_password_comfirm.get():
                messagebox.showerror("Error","Your password didn't get match!", parent = self.root)
            else:
                ## Add username and password in file log.txt, Dont see username and password you just entered in database, add it
                username = self.txt_username.get()
                password = encode(self.txt_password.get())
                arr = [username, password]
                if checkDB_Sign(arr) == False:
                    file = open("src/Documents/log_sign.txt","a", encoding= "utf-8")
                    file.writelines(f"name-username-password: {self.txt_name.get()}; {username}; {password}\n")
                    messagebox.showinfo("Welcome","You are registered successfully!", parent = self.root)
                    file.close()
                else:
                    messagebox.showerror("Error","Account already exists!", parent = self.root)
                
        else:
            if self.txt_name.get() == "":
                messagebox.showerror("Error","Please, enter your full name!", parent = self.root)
            elif self.txt_username.get() == "":
                messagebox.showerror("Error","Please, enter your username!", parent = self.root)
            elif self.txt_password.get() == "":
                messagebox.showerror("Error","Please, enter your password!", parent = self.root)
            elif self.txt_password_comfirm.get() == "":
                messagebox.showerror("Error","Please, enter your password comfirm!", parent = self.root)
    
    