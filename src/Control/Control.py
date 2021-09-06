from Control.Application import*
from Control.Login import*
from Control.Sign import*
from Control.About import*
from Control.Home import*
from Tools.CenterDisplay import*

class Control:
    def __init__(self, root):
        self.root  = root
        
        ## Init Frame (display) and title

        self.root.title("De Uteri")
        self.root.iconbitmap('images/icon.ico')
        self.root.geometry("1280x720")
        self.root.resizable(True,True)
        makecenter(self.root)

        ## Background
        
        self.bg = ImageTk.PhotoImage(file="images/background.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        ## Init Frame for managing button - control

        Frame_control = Frame(self.root, bg="#6e6aba")
        Frame_control.place(x = 300,y = 215, height = 350, width=170)

        self.home_btn = Button(Frame_control, command=self.return_home, text = "Home", font = ("Microsoft Sans Serif",20,"bold"),fg="white",bg="#6e6aba",activebackground="#6e6aba",relief="flat",cursor="hand2",borderwidth=0)
        self.home_btn.place(x = 0, y = 36)

        self.login_btn = Button(Frame_control, command=self.login, text = "Login", font = ("Microsoft Sans Serif",20,"bold"),fg="white",bg="#6e6aba",activebackground="#6e6aba",relief="flat",cursor="hand2",borderwidth=0)
        self.login_btn.place(x = 0, y = 87)

        self.sign_btn = Button(Frame_control, command=self.sign_up, text = "Sign up", font = ("Microsoft Sans Serif",20,"bold"),fg="white",bg="#6e6aba",activebackground="#6e6aba",relief="flat",cursor="hand2",borderwidth=0)
        self.sign_btn.place(x = 0, y = 138)

        self.app_btn = Button(Frame_control, command=self.App, text = "Application", font = ("Microsoft Sans Serif",20,"bold"),fg="white",bg="#6e6aba",activebackground="#6e6aba",relief="flat",cursor="hand2",borderwidth=0)
        self.app_btn.place(x = 0, y = 188)

        self.about_btn = Button(Frame_control, command=self.about_me, text = "About me", font = ("Microsoft Sans Serif",20,"bold"),fg="white",bg="#6e6aba",activebackground="#6e6aba",relief="flat",cursor="hand2",borderwidth=0)
        self.about_btn.place(x = 0, y = 239)

        self.by_btn = Button(Frame_control, command=self.sign_up, text = "by De.Uteri", font = ("Microsoft Sans Serif",10,"bold"),fg="white",bg="#6e6aba",activebackground="#6e6aba",relief="flat",cursor="hand2",borderwidth=0)
        self.by_btn.place(x = 20, y = 325)
         
    ## Init action for button - control

    def login(self):
        self = Login(self.root)
        
    def sign_up(self):
        self = Sign(self.root)
       
    def about_me(self):
        self = AboutMe(self.root)

    def return_home(self):
        self = Home(self.root)
    def App(self):
        self = Application(self.root)
    
        