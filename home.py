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
                  bd=0,width=15,height=1,command=About)#orangered
      btn2.place(x=780,y=90)

      btn2=Button(frame_input,text="Contact Us",cursor="hand2",
                  font=("times new roman",16,"bold"),fg="white",bg="#00B7EB",
                  bd=0,width=15,height=1)#orangered
      btn2.place(x=1000,y=90)

      
def abtus():
  root.destroy()
  import aboutus

def getdisease():
  root.destroy()
  import login


#======working
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from turtle import width
from PIL import ImageTk
import numpy as np
import pandas as pd
import webbrowser



l1=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
    'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue',
    'weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat',
    'irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion',
    'headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation',
    'abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload',
    'swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps',
    'bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain',
    'muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side',
    'loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches',
    'watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances',
    'receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

# TRAINING DATA
df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)

def message():
    if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
        messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
    else :
        NaiveBayes()

def NaiveBayes():
    from sklearn.naive_bayes import MultinomialNB
    gnb = MultinomialNB()
    gnb=gnb.fit(X,np.ravel(y))
    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(disease[predicted] == disease[a]):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "No Disease")

def precaution():
    val=t3.get(1.0, "end-1c")
    if(val=="Common Cold"):
        messagebox.showinfo("Get well soon!!", "Take a steam, Drink hot water, Wash your hands ")
        #demo.insert(END, "Precaution: Take a steam, Drink hot water")
    elif(val=="Hypertension"):
        messagebox.showinfo("Get well soon!!", " Take a head massage, Get enough sleep, Eat healthy diet")
        #demo.insert(END, "Precaution: Take a steam, take a head massage")
    elif(val=="Malaria"):
        messagebox.showinfo("Get well soon!!", "  Eat fruits, Do not ignore early symptoms")    
    elif(val=="Chicken pox"):
        messagebox.showinfo("Get well soon!!", " Wash your clothes, Keep youself clean, Take rest")
    elif(val=="Allergy"):
        messagebox.showinfo("Get well soon!!", " Apply lotions to treat reactions, Keep allergic area clean")
    else:
        messagebox.showinfo("opps!!", "No precaution found")
        #demo.insert(END, "No disease found")
        


root = Tk()
root.title(" Disease Prediction From Symptoms")
root.geometry('1500x700')



root.bg = PhotoImage(file="bg1500.png")
root.bg_image=Label(root,image=root.bg).place(x=0,y=0,relwidth=1,relheight=1)
    
Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)

Frame_main=Frame(root,bg="white")
Frame_main.place(x=150,y=100,height=600,width=1200)

w2 = Label(root,text=" Disease Prediction System ",font=("Impact",28,"bold"),fg="#00B7EB",bg="white").place(x=500,y=15)

#NameLb1 = Label(root, text="")
#NameLb1.config(font=("Elephant", 20))
#NameLb1.grid(row=5, column=1, pady=10,  sticky=W)

S1Lb = Label(root, text="Symptom 1",font=("Impact",20),fg="#00B7EB",bg="white").place(x=300,y=120)
S2Lb = Label(root, text="Symptom 2",font=("Impact",20),fg="#00B7EB",bg="white").place(x=300,y=220)
S3Lb = Label(root, text="Symptom 3",font=("Impact",20),fg="#00B7EB",bg="white").place(x=300,y=320)
S4Lb = Label(root, text="Symptom 4",font=("Impact",20),fg="#00B7EB",bg="white").place(x=300,y=420)
S5Lb = Label(root, text="Symptom 5",font=("Impact",20),fg="#00B7EB",bg="white").place(x=300,y=520)
suffer = Label(root, text="You are Suffering from :",font=("Impact",20),fg="#00B7EB",bg="white").place(x=250,y=600)

demo=Text(root,height=2, width=30,fg="blue",font=('Arial',18,"bold"))
demo.place(relx=0.35,rely=0.85)


"""S2Lb = Label(root,  text="Symptom 2")

S3Lb = Label(root,  text="Symptom 3")
S3Lb.config(font=("Elephant", 15))
S3Lb.grid(row=9, column=1, pady=10, sticky=W)

S4Lb = Label(root,  text="Symptom 4")
S4Lb.config(font=("Elephant", 15))
S4Lb.grid(row=10, column=1, pady=10, sticky=W)

S5Lb = Label(root,  text="Symptom 5")
S5Lb.config(font=("Elephant", 15))
S5Lb.grid(row=11, column=1, pady=10, sticky=W)"""

lr = Button(root, text="Predict !",height=1, width=10,bg="#00B7EB",fg="white",font=("Impact",20),command=message).place(x=1000,y=600)
lo = Button(root, text="Logout",height=1, width=6,bg="white",fg="blue",font=("Impact",18) ).place(x=1400,y=20)
pre = Button(root, text="Precautions",height=1, width=10,bg="#00B7EB",fg="white",font=("Impact",20),command=lambda:precaution()).place(x=1150,y=600)


my_link=Label(root, text='Want to consult a Doctor ?',fg='blue',bg="white",
cursor='hand2',font=('Times',20,'underline'))
my_link.bind('<Button-1>',
    lambda x:webbrowser.open_new("https://www.apollospectra.com/lp/tele-consult/?utm_source=SEM&utm_medium=Search&utm_campaign=Apollospectra_Teleconsult&mobile=7292004096&utm_term=doctor%20help%20online&gclid=CjwKCAjw9qiTBhBbEiwAp-GE0Xj3sRtJnDDOfX8OVpv4kjXO2d8NpzF1k1t4qfgLJ16gEJatC9oZJBoCfHcQAvD_BwE"))
my_link.place(x=1000,y=730)
OPTIONS = sorted(l1)

S1En = OptionMenu(root, Symptom1,*OPTIONS).place(x=1000,y=120)
S2En = OptionMenu(root, Symptom2,*OPTIONS).place(x=1000,y=220)
S3En = OptionMenu(root, Symptom3,*OPTIONS).place(x=1000,y=320)
S4En = OptionMenu(root, Symptom4,*OPTIONS).place(x=1000,y=420)
S5En = OptionMenu(root, Symptom5,*OPTIONS).place(x=1000,y=520)

#NameLb = Label(root, text="")
#NameLb.config(font=("Elephant", 20))
#NameLb.grid(row=13, column=1, pady=10,  sticky=W)

#NameLb = Label(root, text="")
#NameLb.config(font=("Elepqhant", 15))
#NameLb.grid(row=18, column=1, pady=10,  sticky=W)

t3=Text(root,height=2, width=30,fg="blue",font=('Arial',18,"bold"))
t3.place(relx=0.35,rely=0.75)

#t3 = Text(root, height=2, width=30)
#t3.config(font=("Elephant", 20))
#t3.grid(row=20,column=4)

root.mainloop()

#=========login
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

class Login:
   def __init__(self,root):
      self.root=root
      self.root.title("Login and registration form")
      self.root.geometry("1466x800+0+0")
      self.root.resizable(False,False)
      self.loginform()

   def loginform(self):
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=1050,width=1550)

      self.img=ImageTk.PhotoImage(file="bg1500.png")
      img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1500,height=1050)

      frame_input=Frame(self.root,bg='white')
      frame_input.place(x=320,y=130,height=450,width=350)

      label1=Label(frame_input,text="Login Here",font=('impact',32),
                   fg="#00B7EB",bg='white')#black

      label1.place(x=75,y=20)

      label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),
                   fg='#00B7EB',bg='white')#orangered
      label2.place(x=30,y=95)

      self.email_txt=Entry(frame_input,font=("times new roman",15,"bold"),
                       bg='white')
      self.email_txt.place(x=30,y=145,width=270,height=35)

      label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),
                   fg='#00B7EB',bg='white')#orangered
      label3.place(x=30,y=195)

      self.password=Entry(frame_input,font=("times new roman",15,"bold"),
                        bg='white')
      self.password.place(x=30,y=245,width=270,height=35)

      #btn1=Button(frame_input,text="forgot password?",cursor='hand2',
      #            font=('calibri',10,'underline'),bg='white',fg='blue',bd=0)
      #btn1.place(x=125,y=305)

      btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",
                  font=("times new roman",18,"bold"),fg="white",bg="#00B7EB",
                  bd=0,width=15,height=1)#orangered
      btn2.place(x=60,y=340)

      btn3=Button(frame_input,command=self.Register,text="Not Registered?register"
                  ,cursor="hand2",font=("calibri",10,'underline'),bg='white',fg="blue",bd=0)
      btn3.place(x=110,y=390)

      Frame_back=Frame(self.root,bg="white")
      Frame_back.place(x=1200,y=50,height=45,width=140)

      back=Button(Frame_back,text="Home",cursor="hand2",
                  font=("times new roman",18,"bold"),fg="white",bg="#00B7EB",
                  bd=0,width=10,height=1,command=goback)#orangered
      back.place(x=0,y=2)
   
   def login(self):
      if self.email_txt.get()=="" or self.password.get()=="":
         messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
         try:
            con=pymysql.connect(host='localhost',user='root',password='Sql@2002',
                                database='pythongui')
            cur=con.cursor()

            cur.execute('select * from register where emailid=%s and password=%s'
                        ,(self.email_txt.get(),self.password.get()))
            row=cur.fetchone()

            if row==None:
               messagebox.showerror('Error','Invalid Username And Password'
                                    ,parent=self.root)
               self.loginclear()
               self.email_txt.focus()
            else:
               self.appscreen()
               con.close()

         except Exception as es:
            messagebox.showerror('Error',f'Error Due to : {str(es)}'
                                 ,parent=self.root)   
   def Register(self):
      Frame_login1=Frame(self.root,bg="white")
      Frame_login1.place(x=0,y=0,height=700,width=1366)

      

      self.img=ImageTk.PhotoImage(file="bg2.png")
      img=Label(Frame_login1,image=self.img).place(x=0,y=0,width=1366,height=700)

      frame_input2=Frame(self.root,bg='white')
      frame_input2.place(x=320,y=130,height=450,width=630)

      label1=Label(frame_input2,text="Register Here",font=('impact',32,'bold'),
                   fg="black",bg='white')
      label1.place(x=45,y=20)

      label2=Label(frame_input2,text="Username",font=("Goudy old style",20,"bold"),
                   fg='orangered',bg='white')
      label2.place(x=30,y=95)

      self.entry=Entry(frame_input2,font=("times new roman",15,"bold"),
                       bg='lightgray')
      self.entry.place(x=30,y=145,width=270,height=35)

      label3=Label(frame_input2,text="Password",font=("Goudy old style",20,"bold"),
                   fg='orangered',bg='white')
      label3.place(x=30,y=195)

      self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),
                        bg='lightgray')
      self.entry2.place(x=30,y=245,width=270,height=35)

      label4=Label(frame_input2,text="Email-id",font=("Goudy old style",20,"bold"),
                   fg='orangered',bg='white')
      label4.place(x=330,y=95)

      self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),
                       bg='lightgray')
      self.entry3.place(x=330,y=145,width=270,height=35)

      label5=Label(frame_input2,text="Confirm Password",
                   font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
      label5.place(x=330,y=195)

      self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"),
                       bg='lightgray')
      self.entry4.place(x=330,y=245,width=270,height=35)

      btn2=Button(frame_input2,command=self.register,text="Register"
                  ,cursor="hand2",font=("times new roman",15),fg="white",
                  bg="orangered",bd=0,width=15,height=1)
      btn2.place(x=90,y=340)

      btn3=Button(frame_input2,command=self.loginform,
                  text="Already Registered?Login",cursor="hand2",
                  font=("calibri",10),bg='white',fg="black",bd=0)
      btn3.place(x=110,y=390)

   def register(self):
      if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":
         messagebox.showerror("Error","All Fields Are Required",parent=self.root)
      elif self.entry2.get()!=self.entry4.get():
         messagebox.showerror("Error","Password and Confirm Password Should Be Same"
                              ,parent=self.root)
      else:
         try:
            con=pymysql.connect(host="localhost",user="root",password="Sql@2002",
                                database="pythongui")
            cur=con.cursor()
            cur.execute("select * from register where emailid=%s"
                        ,self.entry3.get())
            row=cur.fetchone()

            if row!=None:
               messagebox.showerror("Error"
               ,"User already Exist,Please try with another Email"
                                    ,parent=self.root)
               self.regclear()
               self.entry.focus()
            else:
               cur.execute("insert into register values(%s,%s,%s,%s)"
                           ,(self.entry.get(),self.entry3.get(),
                           self.entry2.get(),
                           self.entry4.get()))
               con.commit()
               con.close()
               messagebox.showinfo("Success","Register Succesfull"
                                   ,parent=self.root)
               self.regclear()
         except Exception as es:
            messagebox.showerror("Error",f"Error due to:{str(es)}"
                                 ,parent=self.root)
   
   #homepage will change for ours
   def appscreen(self):
      root.destroy()
      import disease_prediction

   def regclear(self):
      self.entry.delete(0,END)
      self.entry2.delete(0,END)
      self.entry3.delete(0,END)
      self.entry4.delete(0,END)

   def loginclear(self):
      self.email_txt.delete(0,END)
      self.password.delete(0,END)

def goback():
   root.destroy()
   import homepage

root=Tk()
ob=Login(root)
root.mainloop()      

#============aboutus
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



root=Tk()
ob=Home(root)
root.mainloop()    


