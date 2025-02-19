from tkinter import * 
from PIL import Image,ImageTk #FOR SETTING IMAGES.
from tkinter import ttk
class ummtracker:
    def __init__(self,root):#WINDOW NAME
        self.root=root
        self.root.title("UMMtrackER") #TITLE OF MANAGEMENT SYSTEM
        self.root.geometry("1550x800+0+0") #SIZE OF WINDOW I.E WIDTH and HEIGHT,0,0 =ORIGIN FROM WHERE SCREEN SHOULD START.
             #MAKING OF TITLE AND POSITIONING IT:-
        lbtitle=Label(self.root,text="UMMtrackER",bd=20,relief=RIDGE,bg='white',
                      fg="darkred",font=("times new roman",50,"bold"),padx=2,pady=4) #LABEL NAME,BORDER(bd),
        #BACKGROUND(bg),FONT FAMILY(TUPLE),PADDING,BORDER STYLE(relif),FORGROUNDCOLOR(fg).
        lbtitle.pack(side=TOP,fill=X) #SHOWING OF LABEL ON SCREEN(position=top,fill whole x axis)
        #PUTTING LOGO :-
        logo=Image.open("C:\\Users\\X1 Yoga\\OneDrive\\Desktop\\PYTHON LAB\\logo2.jpeg")
        #RESIZING OF LOGO IMAGE AND CHANGING QUALITY(format):-
        logo=logo.resize((80, 80),Image.LANCZOS)
        self.imagelogo=ImageTk.PhotoImage(logo)
        button1=Button(self.root,image=self.imagelogo,borderwidth=0)        #position of image
        button1.place(x=100,y=21)
        logo1=Image.open("C:\\Users\\X1 Yoga\\OneDrive\\Desktop\\PYTHON LAB\\logo2.jpeg")
        #RESIZING OF LOGO IMAGE AND CHANGING QUALITY(format):-
        logo1=logo1.resize((80, 80),Image.LANCZOS)
        self.imagelogo1=ImageTk.PhotoImage(logo1)
        button2=Button(self.root,image=self.imagelogo1,borderwidth=0)        #position of image
        button2.place(x=1060,y=21)
           #MAKING OF DATA FRAME:-
        dataframe=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        dataframe.place(x=0,y=120,width=1265,height=350)
        dataframeleft=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=20,text="MEDICINE INFORMATION",
                                 fg="darkred",font=("aerial",12,"bold"))
        dataframeleft.place(x=0,y=5,width=690,height=310)
        dataframeright=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=20,text="NEW SUPPLIES HERE",
                                 fg="darkred",font=("aerial",12,"bold"))
        dataframeright.place(x=700,y=5,width=500,height=310)
            #MAKING BUTTON FRAME:-
        buttonframe=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        buttonframe.place(x=0,y=470,width=1265,height=65)
            #MAKING MAIN BUTTONS:-
        button=Button(buttonframe,text=" ADD MEDICINE ",
                      font=("arial",12,"bold"),bg="darkred",fg="white")
        button.grid(row=0,column=0,padx=0,pady=5)
        button=Button(buttonframe,text="  UPDATE  ",
                      font=("arial",12,"bold"),bg="darkred",fg="white")
        button.grid(row=0,column=1,padx=2,pady=5)
        button=Button(buttonframe,text="  DELETE  ",
                      font=("arial",12,"bold"),bg="darkred",fg="white")
        button.grid(row=0,column=2,padx=3,pady=5)
        button=Button(buttonframe,text="  RESET  ",
                      font=("arial",12,"bold"),bg="darkred",fg="white")
        button.grid(row=0,column=3,padx=4,pady=5)
        button=Button(buttonframe,text="  EXIT  ",
                      font=("arial",12,"bold"),bg="darkred",fg="white")
        button.grid(row=0,column=4,padx=5,pady=5)
             #SEARCH BY OPTION:-
        Iblsearch=Label(buttonframe,font=("ariel",17,"bold"),
                        text="  SEARCH BY  ",
                        padx=2,bg="darkred",fg="white",)
        Iblsearch.grid(row=0,column=5,padx=6,pady=5,sticky=W)
        serch_combo=ttk.Combobox(buttonframe,width=12,font=("arial",13,"bold"),state="readonly")
        serch_combo["value"]=("Ref","Lot","Medname")
        serch_combo.grid(row=0,column=6,padx=7,pady=5)
        serch_combo.current(0)

        txtserch=Entry(buttonframe,bd=3,relief=RIDGE,width=12,font=("ariel",12,"bold"))
        txtserch.grid(row=0,column=8,padx=8,pady=5)
        button=Button(buttonframe,text=" SEARCH  ",
                      font=("arial",12,"bold"),bg="darkred",fg="white")
        button.grid(row=0,column=9,padx=9,pady=5)
        button=Button(buttonframe,text="  SHOW ALL  ",
                      font=("arial",12,"bold"),bg="darkred",fg="white")
        button.grid(row=0,column=10,padx=10,pady=5)
        #*****************************************************label and entry:-************************************************************
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="REFERENCE NO", padx=0)
        refno.grid(row=0,column=0,sticky=W)
        ref_combo=ttk.Combobox(dataframeleft, width=20, font=("arial", 12, "bold"), state="readonly")
        ref_combo["values"]=("Ref", "Medname", "Lot")
        ref_combo.current(0)
        ref_combo.grid(row=0,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="COMPANY NAME", padx=2)
        refno.grid(row=1,column=0,sticky=W)
        ref_combo=Entry(dataframeleft, width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=1,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="TYPE OF MEDICINE", padx=2)
        refno.grid(row=2,column=0,sticky=W)
        ref_combo=ttk.Combobox(dataframeleft, width=20, font=("arial", 12, "bold"), state="readonly")
        ref_combo["values"]=("TABLET", "LIQUID", "CAPSULE","DROPS","INJECTION","INHALER")
        ref_combo.current(0)
        ref_combo.grid(row=2,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="MEDICINE NAME", padx=2)
        refno.grid(row=3,column=0,sticky=W)
        ref_combo=ttk.Combobox(dataframeleft, width=20, font=("arial", 12, "bold"), state="readonly")
        ref_combo["values"]=("pqr", "mno", "jkl","ghi","def","abc")
        ref_combo.current(0)
        ref_combo.grid(row=3,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="LOT NO", padx=2)
        refno.grid(row=4,column=0,sticky=W)
        ref_combo=Entry(dataframeleft,font=("arial", 12, "bold"),background="white",width=22)
        ref_combo.grid(row=4,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="ISSUE DATE", padx=2)
        refno.grid(row=5,column=0,sticky=W)
        ref_combo=Entry(dataframeleft, width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=5,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="EXP DATE", padx=2)
        refno.grid(row=6,column=0,sticky=W)
        ref_combo=Entry(dataframeleft, width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=6,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="USES", padx=2)
        refno.grid(row=7,column=0,sticky=W)
        ref_combo=Entry(dataframeleft, width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=7,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="SIDE EFFECT", padx=2)
        refno.grid(row=8,column=0,sticky=W)
        ref_combo=Entry(dataframeleft, width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=8,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="WARNINGS", padx=2)
        refno.grid(row=9,column=0,sticky=W)
        ref_combo=Entry(dataframeleft, width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=9,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="DOSAGE", padx=2)
        refno.grid(row=10,column=0,sticky=W)
        ref_combo=Entry(dataframeleft, width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=10,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="MED PRICE", padx=2)
        refno.grid(row=0,column=2,sticky=W)
        ref_combo=Entry(dataframeleft, width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=0,column=3)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="PRODUCT QTY")
        refno.grid(row=1,column=2,sticky=W)
        ref_combo=Entry(dataframeleft, width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=1,column=3,sticky=W)
        #************************************xuv auer jaha auer tag********************************************
        refno=Label(dataframeleft,font=("arial", 15, "bold"), text="ZUV AUER---JAHA AUER", padx=2,pady=6,background="white",foreground="darkred")
        refno.place(x=370,y=55)
        








if __name__ =="__main__":
    root=Tk()
    obj=ummtracker(root)
    root.mainloop() #CLOSING OF ROOT
        
