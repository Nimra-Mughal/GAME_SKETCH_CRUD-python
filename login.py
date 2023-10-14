from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from PIL import Image,ImageTk

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Form")
        self.root.geometry("350x700+0+0")
        self.bg=ImageTk.PhotoImage(file="images/bigger.png")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)


        frame1=Frame(self.root,background="white")
        frame1.place(x=700,y=130,width=640,height=500)
        Label(frame1, text="Register Here", font=("Impact",25,"bold"), bg="white", fg="#d77337").place(x=50,y=20)

        self.img = ImageTk.PhotoImage(file="images/reg.png")
        Label(frame1, image=self.img, bg="white").place(x=280, y=10)

        email=Label(frame1, text="Email", font=("Roboto", 12, "bold"), bg="white", fg="black").place(x=50, y=150)
        self.txt_email = Entry(frame1, font=("Roboto", 12,), bg="light grey")
        self.txt_email.place(x=50, y=180, width=250,height=35)

        password = Label(frame1, text="Password", font=("Roboto", 12, "bold"), bg="white", fg="black").place(x=50, y=290)
        self.txt_password = Entry(frame1, font=("Roboto", 12,), bg="light grey")
        self.txt_password.place(x=50, y=320, width=250,height=35)

        btn=Button(frame1,text="Sign In",font=("Roboto",10,"bold"),foreground="white", command=self.loginData,bg="#d77337",bd=0,cursor="hand2").place(x=50,y=430,width=100,height=40)
        btn1=Button(frame1,text="Sign Up",font=("Roboto",10,"bold"),foreground="white", command=self.regredirect,bg="#d77337",bd=0,cursor="hand2").place(x=200,y=430,width=100,height=40)

    def loginData(self):
       if self.txt_email.get()=="" or self.txt_password.get()=="":
           messagebox.showerror("Error","All fields are mendtory",parent=self.root)
       else:
           try:
               con = pymysql.connect(host="localhost", user="root", password="", database="regdb")
               cursor = con.cursor()
               cursor.execute("select * from employee where email%s and password%s",(self.txt_email.get(),self.txt_password.get()))
               row=cursor.fetchone()
               if row==None:
                   messagebox.showerror("Error","Invalid username or Password",parent=self.root)
               else:
                   messagebox.showinfo("Sucesss","Sucessfully Login",parent=self.root)
                   self.root.destroy()
                   import calculator
                   con.close()
               # print(row)
           except Exception as ex:
               messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)



    def regredirect(self):
        self.root.destroy()
        import reg_img
    def ClearData(self):
        self.txt_email.delete(0, END),
        self.txt_password.delete(0, END),

root=Tk()
object=Login(root)
root.mainloop()






#
# root=Tk()
# object=Registration(root)
# root.mainloop()

