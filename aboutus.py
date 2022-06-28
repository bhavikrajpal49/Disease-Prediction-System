from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

class About:
   def __init__(self,root):
      self.root=root
      self.root.title("About Us")
      self.root.geometry("1466x800+20+0")
      self.root.resizable(False,False)
      self.abtus()

   def abtus(self):
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=1050,width=1550)
      
      self.img=ImageTk.PhotoImage(file="bg1500.png")
      img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1500,height=1050)

      frame_input=Frame(self.root,bg='white')
      frame_input.place(x=0,y=20,height=70,width=1470)

      label1=Label(frame_input,text="About Us",font=('impact',32),fg="#00B7EB",bg='white')#black
      label1.place(x=700,y=10)

      back=Button(frame_input,text="Home",cursor="hand2",
                  font=("times new roman",18,"bold"),fg="white",bg="#00B7EB",
                  bd=0,width=10,height=1,command=goback)#orangered
      back.place(x=1200,y=12)


      frame_input1=Frame(self.root,bg='white')
      frame_input1.place(x=750,y=190,height=500,width=600)
      label3=Label(frame_input1,text="The general disease prediction system predicts chance of presence of a disease present in a patient on the basis of their symptoms. It will also recommend necessary precautionary measures required to treat the predicted disease.",font=("Impact",24),
                   fg='#00B7EB',bg='white',wraplength=500,)#orangered
      label3.place(x=50,y=80)




      #frame_input2=Frame(self.root,bg='white')
      #frame_input2.place(x=50,y=190,height=500,width=600)
      #bg = PhotoImage(file="abt_icon.png")
      #bg_image=Label(frame_input2,image=bg).place(x=50,y=190,relwidth=0.4,relheight=0.4)
      #img=ImageTk.PhotoImage(Image.open("icon_about.jpg"))
      #label=Label(frame_input2,image=img)
      #label.pack()

def goback():
   root.destroy()
   import homepage


root=Tk()
ob=About(root)
root.mainloop() 