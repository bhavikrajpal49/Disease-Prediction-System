from tkinter import *
from turtle import color
from typing_extensions import Self
from PIL import ImageTk
from tkinter import messagebox
import pymysql
from PIL import Image,ImageDraw,ImageFont
from controller import*
from tkinter.font import BOLD
from turtle import width
import numpy as np
import pandas as pd
import webbrowser

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
                  bd=0,width=15,height=1)#orangered
      btn2.place(x=300,y=90)

      btn2=Button(frame_input,text="Search Hospital",cursor="hand2",
                  font=("times new roman",16,"bold"),fg="white",bg="#00B7EB",
                  bd=0,width=15,height=1)#orangered
      btn2.place(x=550,y=90)

      btn2=Button(frame_input,text="About Us",cursor="hand2",
                  font=("times new roman",16,"bold"),fg="white",bg="#00B7EB",
                  bd=0,width=15,height=1,command=lambda:abtus())#orangered
      btn2.place(x=780,y=90)

      btn2=Button(frame_input,text="Contact Us",cursor="hand2",
                  font=("times new roman",16,"bold"),fg="white",bg="#00B7EB",
                  bd=0,width=15,height=1)#orangered
      btn2.place(x=1000,y=90)

def abtus():
    Frame_login=Frame(root,bg="white")
    Frame_login.place(x=0,y=0,height=1050,width=1550)
      
    img=ImageTk.PhotoImage(file="bg1500.png")
    img=Label(Frame_login,image=img).place(x=0,y=0,width=1500,height=1050)

    frame_input=Frame(root,bg='white')
    frame_input.place(x=0,y=20,height=70,width=1470)

    label1=Label(frame_input,text="About Us",font=('impact',32),fg="#00B7EB",bg='white')#black
    label1.place(x=700,y=10)

    back=Button(frame_input,text="Home",cursor="hand2",
                  font=("times new roman",18,"bold"),fg="white",bg="#00B7EB",
                  bd=0,width=10,height=1)#orangered
    back.place(x=1200,y=12)


    frame_input1=Frame(root,bg='white')
    frame_input1.place(x=750,y=190,height=500,width=600)
    label3=Label(frame_input1,text="The general disease prediction system predicts chance of presence of a disease present in a patient on the basis of their symptoms. It will also recommend necessary precautionary measures required to treat the predicted disease.",font=("Impact",24),
                   fg='#00B7EB',bg='white',wraplength=500,)#orangered
    label3.place(x=50,y=80)




root=Tk()
ob=Home(root)
root.mainloop() 