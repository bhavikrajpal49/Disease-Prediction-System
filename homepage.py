from tkinter import *
from turtle import color
from PIL import ImageTk
from tkinter import messagebox
import pymysql
from PIL import Image,ImageDraw,ImageFont
from controller import*

class Home:
    def __init__(self,root):
      self.root=root
      self.root.title("Home Page")
      self.root.geometry("1466x800+20+0")
      self.root.resizable(False,False)
      self.HomePage()

    def HomePage(self):
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=1050,width=1550)
      
      self.img=ImageTk.PhotoImage(file="bg1500.png")
      img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1500,height=1050)

      frame_input=Frame(self.root,bg='white')
      frame_input.place(x=0,y=20,height=150,width=1470)

      label1=Label(frame_input,text="Disease  Prediction  System",font=('impact',32),fg="#00B7EB",bg='white')#black
      label1.place(x=510,y=20)

      btn2=Button(frame_input,text="Predict Disease",cursor="hand2",
                  font=("times new roman",16,"bold"),fg="white",bg="#00B7EB",
                  bd=0,width=15,height=1,command=getdisease)#orangered
      btn2.place(x=300,y=90)

      btn2=Button(frame_input,text="Search Hospital",cursor="hand2",
                  font=("times new roman",16,"bold"),fg="white",bg="#00B7EB",
                  bd=0,width=15,height=1)#orangered
      btn2.place(x=550,y=90)

      btn2=Button(frame_input,text="About Us",cursor="hand2",
                  font=("times new roman",16,"bold"),fg="white",bg="#00B7EB",
                  bd=0,width=15,height=1,command=abtus)#orangered
      btn2.place(x=780,y=90)

      btn2=Button(frame_input,text="Feedback",cursor="hand2",
                  font=("times new roman",16,"bold"),fg="white",bg="#00B7EB",
                  bd=0,width=15,height=1,command=fdbk)#orangered
      btn2.place(x=1000,y=90)

      
def abtus():
  root.destroy()
  import aboutus

def getdisease():
  root.destroy()
  import login

def fdbk():
  root.destroy()
  import feedback


root=Tk()
ob=Home(root)
root.mainloop()    