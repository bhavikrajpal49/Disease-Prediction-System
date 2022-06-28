from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

class Feedback:
   def __init__(self,root):
      self.root=root
      self.root.title("Login and registration form")
      self.root.geometry("1366x700+0+0")
      self.root.resizable(False,False)
      self.Register()
   
   def Register(self):
      Frame_login1=Frame(self.root,bg="white")
      Frame_login1.place(x=0,y=0,height=700,width=1366)

      self.img=ImageTk.PhotoImage(file="bg1500.png")
      img=Label(Frame_login1,image=self.img).place(x=0,y=0,width=1366,height=700)

      frame_input2=Frame(self.root,bg='white')
      frame_input2.place(x=320,y=130,height=450,width=630)

      label1=Label(frame_input2,text="Please Write Feedback Here!",font=('impact',32,'bold'),
                   fg="#00B7EB",bg='white')
      label1.place(x=45,y=20)

      label2=Label(frame_input2,text="Name",font=("Goudy old style",20,"bold"),
                   fg='#00B7EB',bg='white')
      label2.place(x=30,y=95)

      self.entry=Entry(frame_input2,font=("times new roman",15,"bold"),
                       bg='lightgray')
      self.entry.place(x=30,y=145,width=400,height=35)

      label3=Label(frame_input2,text="Feedback",font=("Goudy old style",20,"bold"),
                   fg='#00B7EB',bg='white')
      label3.place(x=30,y=195)

      self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),
                        bg='lightgray')
      self.entry2.place(x=30,y=245,width=400,height=35)

      btn2=Button(frame_input2,text="Submit"
                  ,cursor="hand2",font=("times new roman",15),fg="white",
                  bg="#00B7EB",bd=0,width=12,height=1,command=self.reg)
      btn2.place(x=90,y=340)

      btn3=Button(frame_input2,text="Cancel"
                  ,cursor="hand2",font=("times new roman",15),fg="white",
                  bg="#00B7EB",bd=0,width=12,height=1,command=goback)
      btn3.place(x=240,y=340)

   def reg(self):   
      if self.entry.get()==""or self.entry2.get()=="":
         messagebox.showerror("Error","All Fields Are Required",parent=self.root)
      else:
         try:
            con=pymysql.connect(host="localhost",user="root",password="Sql@2002",
                                database="pythongui")
            cur=con.cursor()
            
            cur.execute("insert into feedback values(%s,%s)"
                           ,(self.entry.get(),self.entry2.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success","feedback added"
                                   ,parent=self.root)
            self.regclear()
         except Exception as es:
            messagebox.showerror("Error",f"Error due to:{str(es)}"
                                 ,parent=self.root)
   def regclear(self):
      self.entry.delete(0,END)
      self.entry2.delete(0,END)

def goback():
        root.destroy()
        import homepage


      
root=Tk()
ob=Feedback(root)
root.mainloop()     