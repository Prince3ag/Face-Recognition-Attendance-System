from tkinter import*
from tkinter import messagebox
import os
from PIL import ImageTk,Image


def run(self):
    os.system('attendance.py')


class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        img=Image.open("images/quantumback.jpg")
        img = img.resize((1300, 700), Image.ANTIALIAS)
        self.bg_icon=ImageTk.PhotoImage(img)

        img1=Image.open("images/man-user.png")
        img1 = img1.resize((50,50), Image.ANTIALIAS)
        self.user_icon=ImageTk.PhotoImage(img1)

        img2 = Image.open("images/password.png")
        img2 = img2.resize((50, 50), Image.ANTIALIAS)
        self.pass_icon = ImageTk.PhotoImage(img2)

        img3 = Image.open("images/user-icon.png")
        img3 = img3.resize((150, 150), Image.ANTIALIAS)
        self.logo_icon = ImageTk.PhotoImage(img3)

        self.uname=StringVar()
        self.pass_=StringVar()


        bg_lbl = Label(self.root, image=self.bg_icon).pack()


        title=Label(self.root,text="Login System",font=("times new roman",40,"bold"),bg="aqua",fg="navyblue",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=400,y=150)

        logolbl=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

        lbluser=Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)



        lblpass=Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
        txtpass = Entry(Login_Frame, bd=5,textvariable=self.pass_,show="*", relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=20)


        btn_log=Button(Login_Frame,text="Login",command=self.login,width=15,font=("times new roman",14,"bold"),bg="aqua",fg="navyblue").grid(row=3,column=1,pady=10)

    def login(self):
        if self.uname.get() == "" or self.pass_.get() == "":
             messagebox.showerror("Error", "All fields are required")
        elif self.uname.get() == "Prince" and self.pass_.get() == "123456":
            run(self)
            root.destroy()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")
            self.uname.set("")
            self.pass_.set("")






root=Tk()
obj=Login_System(root)
root.mainloop()
