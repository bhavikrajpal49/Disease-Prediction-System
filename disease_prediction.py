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

#demo=Text(root,height=2, width=30,fg="blue",font=('Arial',18,"bold"))
#demo.place(relx=0.35,rely=0.85)


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
lo = Button(root, text="Logout",height=1, width=6,bg="white",fg="blue",font=("Impact",18)).place(x=1400,y=20)
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
