from webbrowser import open_new
from PIL import ImageTk,Image
from Control.Application import*
from Control.Login import*
from Control.Sign import*
from Control.About import*
from Control.Home import*
from Tools.CenterDisplay import*

root = Tk()
root.title("De Uteri")
root.iconbitmap('images/frame/icon.ico')
root.geometry("960x540")
root.background = Label(bg = "#6753c6").place(x = 0, y = 0, relwidth = 1, relheight = 1)
root.resizable(0,0)
makecenter(root)

## set background image

init_frame=Frame(root, width = 900, height = 540, bg = '#823af7')
init_frame.place(x=60,y=0)

global image_default
image_default = ImageTk.PhotoImage(file = 'images/interfaces/background_home.png')
Frame_default = Frame(init_frame, bg = "#823af7")
Frame_default.place(x = 0,y = 0, height = 540, width=900)
logo_default = Label(Frame_default, image = image_default )
logo_default.place( x = 0, y = 0, relheight = 1, relwidth = 1 )
makecenter(root)

##  Set logic for button ##

global home, login, signup, app, about

def openHome():   
    home = Home(root)

def openLogin():
    login = Login(root)
            
def openSign_up():
    signup = Sign(root)
        
def openApp():
    if isLoginSuccessfully() == True:
        app = Application(root)
    else: 
        messagebox.showerror("Error","You must login first to run the application.", parent = root)

def openAbout_me():
    about = AboutMe(root)

def control():
    def swapFrame():
        global home_bg, frame_home
        
        fist_frame=Frame(root, width = 300, height = 540, bg = '#823af7')
        fist_frame.place(x=0,y=0)
                
        ## Make button in frame "open"

        frameButton(fist_frame, -1, 80, ' H O M E ', '#7626d7', '#823af7', openHome, None)
        frameButton(fist_frame, -1, 130, ' L O G I N ', '#7626d7', '#823af7', openLogin, None)
        frameButton(fist_frame, -1, 180, ' S I G N   U P ', '#7626d7', '#823af7', openSign_up, None)
        frameButton(fist_frame, -1, 230, ' A P P L I C A T I O N S ', '#7626d7', '#823af7', openApp, None)
        frameButton(fist_frame, -1, 280, ' A B O U T   M E ', '#7626d7', '#823af7', openAbout_me, None)
        frameButton(fist_frame, -1, 460, ' b y   D e u t e r i ', '#7626d7', '#823af7', None, None)
        
        
        ## Icon
        global facebook_control, google_control, github_control, logo_image
        Frame_logo = Frame(fist_frame, bg = "#823af7")
        Frame_logo.place(x = 0,y = 350, height = 190, width=300)
        logo_image = ImageTk.PhotoImage(file = "images/interfaces/logo_anime.png")
        logo = Label(Frame_logo, image = logo_image )
        logo.place( x = 0, y = 0, relheight = 1, relwidth = 1 )

        def deleleFrame():
            fist_frame.destroy()
            
            ## Display background image again

            second_frame=Frame(root, width = 900, height = 540, bg = '#823af7')
            second_frame.place(x=60,y=0)
            global image_default 
            image_default = ImageTk.PhotoImage(file = 'images/background_home.png')
            Frame_default = Frame(second_frame, bg = "#823af7")
            Frame_default.place(x = 0,y = 0, height = 540, width=900)
            logo_default = Label(Frame_default, image = image_default )
            logo_default.place( x = 0, y = 0, relheight = 1, relwidth = 1 )
            
            

        global image_close
        image_close = ImageTk.PhotoImage(file = "images/buttons/close.png")

        Button(fist_frame, image = image_close, border = 0, command = deleleFrame, bg = '#823af7', activebackground = '#823af7').place(x = 5, y = 10)
    
    image_open = ImageTk.PhotoImage(file = "images/buttons/open.png")
    Button(root, image = image_open, command = swapFrame, border = 0, bg = '#6753c6', activebackground ='#6753c6').place(x = 5, y = 10)

    root.mainloop() 


    
            