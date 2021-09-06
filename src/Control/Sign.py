from tkinter.font import BOLD
from PIL import ImageTk
from tkinter import*
from PIL import Image
from tkinter import messagebox
from Tools.log_db import*

class Sign:
    def __init__(self, root):
        self.root  = root

        ## Init frame and button for sign in part

        Frame_sign = Frame(self.root, bg="#f0f0f0")
        Frame_sign.place(x = 500,y = 140, height = 450, width=500)

        self.title = Label(Frame_sign, text = "Sign up", font= ("Georgia", 35, "bold"),fg="#6e6aba",bg="#f0f0f0").place(x = 65, y = 30)
        self.desc = Label(Frame_sign, text = "Join us with", font = ("UTM-Avo",12,"bold"),fg="#6e6aba",bg="#f0f0f0").place(x = 70, y = 100)
        
        self.lab_name = Label(Frame_sign, text = "Full name*", font = ("Times New Roman",12,"bold"),fg="#000000",bg="#f0f0f0").place(x = 70, y = 145)
        self.txt_name = Entry(Frame_sign, font=("Times New Roman",15),bg="white",cursor="hand2")
        self.txt_name.place(x = 70, y = 170, height= 35, width= 350)    

        self.lab_username = Label(Frame_sign, text = "Username*", font = ("Times New Roman",12,"bold"),fg="#000000",bg="#f0f0f0").place(x = 70, y = 205)
        self.txt_username = Entry(Frame_sign, font=("Times New Roman",15),bg="white",cursor="hand2")
        self.txt_username.place(x = 70, y = 230, height= 35, width= 350)

        self.lab_password = Label(Frame_sign, text = "Password*", font = ("Times New Roman",12,"bold"),fg="#000000",bg="#f0f0f0").place(x = 70, y = 265)
        self.txt_password = Entry(Frame_sign, font=("Times New Roman",15), bg="white",cursor="hand2")
        self.txt_password.place(x = 70, y = 290, height= 35, width= 350)

        self.lab_password_comfirm = Label(Frame_sign, text = "Confirm Password*", font = ("Times New Roman",12,"bold"),fg="#000000",bg="#f0f0f0").place(x = 70, y = 325)
        self.txt_password_comfirm = Entry(Frame_sign, font=("Times New Roman",15), bg="white",cursor="hand2")
        self.txt_password_comfirm.place(x = 70, y = 350, height= 35, width= 350)
    
        ## Make sign in button

        self.sign_btn = Button(self.root, command=self.sign, text = "   Sign up here   ", font = ("Times New Roman",12,"bold"),fg="#f0f0f0",bg="#6e6aba",relief="flat",cursor="hand2",borderwidth=0).place(x = 800, y = 530)
        
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
    
    