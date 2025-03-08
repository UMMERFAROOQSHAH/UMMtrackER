from tkinter import * 
from PIL import Image,ImageTk #FOR SETTING IMAGES.
from tkinter import ttk  #FOR MAKING WIDGES(COMBO-BOXES HERE)
import mysql.connector
from tkinter import messagebox          #POPUP MESSAGE
class ummtracker:
    def __init__(self,root):#WINDOW NAME
        self.root=root
        self.root.title("UMMER FAROOQ SHAH") #TITLE OF MANAGEMENT SYSTEM
        self.root.geometry("1550x800+0+0") #SIZE OF WINDOW I.E WIDTH and HEIGHT,0,0 =ORIGIN FROM WHERE SCREEN SHOULD START.
        #***************************ADDING VARIABLES****************************
        self.addmedvar=StringVar()
        self.addrefvar=StringVar()
        self.refvar=StringVar()
        self.cpynamevar=StringVar()
        self.typevar=StringVar()
        self.mednamevar=StringVar()
        self.lotvar=StringVar()
        self.issuevar=StringVar()
        self.expirevar=StringVar()
        self.usesvar=StringVar()
        self.efectsvar=StringVar()
        self.warningvar=StringVar()
        self.dosagevar=StringVar()
        self.pricevar=StringVar()
        self.qntyvar=StringVar()
        

        
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
        button=Button(buttonframe,command=self.AddMedlower,text=" ADD MEDICINE ",
                      font=("arial",12,"bold"),bg="darkgreen",fg="white")
        button.grid(row=0,column=0,padx=0,pady=5)
        button=Button(buttonframe,text="  UPDATE  ",
                      font=("arial",12,"bold"),bg="orange",fg="white")
        button.grid(row=0,column=1,padx=2,pady=5)
        button=Button(buttonframe,text="  DELETE  ",
                      font=("arial",12,"bold"),bg="darkred",fg="white")
        button.grid(row=0,column=2,padx=3,pady=5)
        button=Button(buttonframe,text="  RESET  ",
                      font=("arial",12,"bold"),bg="purple",fg="white")
        button.grid(row=0,column=3,padx=4,pady=5)
        button=Button(buttonframe,text="  EXIT  ",
                      font=("arial",12,"bold"),bg="darkgrey",fg="white")
        button.grid(row=0,column=4,padx=5,pady=5)
             #SEARCH BY OPTION:-
        Iblsearch=Label(buttonframe,font=("ariel",17,"bold"),
                        text="  SEARCH BY  ",
                        padx=2,bg="darkblue",fg="white",)
        Iblsearch.grid(row=0,column=5,padx=6,pady=5,sticky=W)
        serch_combo=ttk.Combobox(buttonframe,width=12,font=("arial",13,"bold"),state="readonly")
        serch_combo["value"]=("Ref","Lot","Medname")
        serch_combo.grid(row=0,column=6,padx=7,pady=5)
        serch_combo.current(0)

        txtserch=Entry(buttonframe,bd=3,relief=RIDGE,width=12,font=("ariel",12,"bold"))
        txtserch.grid(row=0,column=8,padx=8,pady=5)
        button=Button(buttonframe,text=" SEARCH  ",
                      font=("arial",12,"bold"),bg="darkblue",fg="white")
        button.grid(row=0,column=9,padx=9,pady=5)
        button=Button(buttonframe,text="  SHOW ALL  ",
                      font=("arial",12,"bold"),bg="black",fg="white")
        button.grid(row=0,column=10,padx=10,pady=5)
        #*****************************************************label and entry:-************************************************************
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="REFERENCE NO", padx=0)
        refno.grid(row=0,column=0,sticky=W)
        #******************************FETCHING DATA FROM SMALL WINDOW ON RIGHT SIDE TO LEFT COMBO BOXES LIKE REF,MEDICINE NAME***************************************
       
        conn=mysql.connector.connect(host="localhost",user="root",password="7006760858",database="UMMTRACKER")
        cursor=conn.cursor()
        cursor.execute("SELECT REF FROM PHARMA")
        row=cursor.fetchall()
        ref_combo=ttk.Combobox(dataframeleft,textvariable=self.refvar,width=20, font=("arial", 12, "bold"), state="readonly")
        ref_combo["values"]=row
        ref_combo.current(0)
        ref_combo.grid(row=0,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="COMPANY NAME", padx=2)
        refno.grid(row=1,column=0,sticky=W)
        ref_combo=Entry(dataframeleft,  textvariable=self.cpynamevar,width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=1,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="TYPE OF MEDICINE", padx=2)
        refno.grid(row=2,column=0,sticky=W)
        ref_combo=ttk.Combobox(dataframeleft,textvariable=self.typevar ,width=20, font=("arial", 12, "bold"), state="readonly")
        ref_combo["values"]=("TABLET", "LIQUID", "CAPSULE","DROPS","INJECTION","INHALER")
        ref_combo.current(0)
        ref_combo.grid(row=2,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="MEDICINE NAME", padx=2)
        refno.grid(row=3,column=0,sticky=W)
        #******************************FETCHING DATA FROM SMALL WINDOW ON RIGHT SIDE TO LEFT COMBO BOXES LIKE REF,MEDICINE TYPE,MEDICINE NAME***************************************
        conn=mysql.connector.connect(host="localhost",user="root",password="7006760858",database="UMMTRACKER")
        cursor=conn.cursor()
        cursor.execute("SELECT MEDNAME FROM PHARMA")
        row=cursor.fetchall()
        ref_combo=ttk.Combobox(dataframeleft,  textvariable=self.mednamevar,width=20, font=("arial", 12, "bold"), state="readonly")
        ref_combo["values"]=row
        ref_combo.current(0)
        ref_combo.grid(row=3,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="LOT NO", padx=2)
        refno.grid(row=4,column=0,sticky=W)
        ref_combo=Entry(dataframeleft, textvariable=self.lotvar,font=("arial", 12, "bold"),background="white",width=22)
        ref_combo.grid(row=4,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="ISSUE DATE", padx=2)
        refno.grid(row=5,column=0,sticky=W)
        ref_combo=Entry(dataframeleft,  textvariable=self.issuevar,width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=5,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="EXP DATE", padx=2)
        refno.grid(row=6,column=0,sticky=W)
        ref_combo=Entry(dataframeleft,  textvariable=self.expirevar,width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=6,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="USES", padx=2)
        refno.grid(row=7,column=0,sticky=W)
        ref_combo=Entry(dataframeleft,  textvariable=self.usesvar,width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=7,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="SIDE EFFECT", padx=2)
        refno.grid(row=8,column=0,sticky=W)
        ref_combo=Entry(dataframeleft,  textvariable=self.efectsvar,width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=8,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="WARNINGS", padx=2)
        refno.grid(row=9,column=0,sticky=W)
        ref_combo=Entry(dataframeleft,  textvariable=self.warningvar,width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=9,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="DOSAGE", padx=2)
        refno.grid(row=10,column=0,sticky=W)
        ref_combo=Entry(dataframeleft, textvariable=self.dosagevar, width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=10,column=1)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="MED PRICE", padx=2)
        refno.grid(row=0,column=2,sticky=W)
        ref_combo=Entry(dataframeleft, textvariable=self.pricevar, width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=0,column=3)
        refno=Label(dataframeleft, font=("arial", 10, "bold"), text="PRODUCT QTY")
        refno.grid(row=1,column=2,sticky=W)
        ref_combo=Entry(dataframeleft, textvariable=self.qntyvar, width=22, font=("arial", 12, "bold"))
        ref_combo.grid(row=1,column=3,sticky=W)
        #************************************xuv auer jaha auer tag********************************************
        refno=Label(dataframeleft,font=("arial", 18, "bold"), text="ZUV AUER---JAHA AUER", padx=2,pady=6,background="white",foreground="darkblue")
        refno.place(x=345,y=65)
        #****************************************LEFT FRAME IMAGES*********************************************
        logo3=Image.open("C:\\Users\\X1 Yoga\\OneDrive\\Desktop\\PYTHON LAB\\left2.webp")
        logo3=logo3.resize((185, 135),Image.LANCZOS)
        self.imagelogo3=ImageTk.PhotoImage(logo3)
        button2=Button(self.root,image=self.imagelogo3,borderwidth=0)        #position of image
        button2.place(x=520,y=300)
        logo4=Image.open("C:\\Users\\X1 Yoga\\OneDrive\\Desktop\\PYTHON LAB\\left1.webp")
        logo4=logo4.resize((155, 135),Image.LANCZOS)
        self.imagelogo4=ImageTk.PhotoImage(logo4)
        button2=Button(self.root,image=self.imagelogo4,borderwidth=0)        #position of image
        button2.place(x=400,y=300)
        #****************************************RIGHT FRAME IMAGES*********************************************
        logo5=Image.open("C:\\Users\\X1 Yoga\\OneDrive\\Desktop\\PYTHON LAB\\right1.jpg")
        logo5=logo5.resize((95, 55),Image.LANCZOS)
        self.imagelogo5=ImageTk.PhotoImage(logo5)
        button2=Button(self.root,image=self.imagelogo5,borderwidth=0)        #position of image
        button2.place(x=1060,y=160)
        logo6=Image.open("C:\\Users\\X1 Yoga\\OneDrive\\Desktop\\PYTHON LAB\\right2.webp")
        logo6=logo6.resize((70, 55),Image.LANCZOS)
        self.imagelogo6=ImageTk.PhotoImage(logo6)
        button2=Button(self.root,image=self.imagelogo6,borderwidth=0)        #position of image
        button2.place(x=1150,y=160)
        refno=Label(dataframeright,font=("arial", 10, "bold"), text="REFERENCE NO")
        refno.place(x=0,y=0)
        refno=Entry(dataframeright,textvariable=self.addrefvar,width=19, font=("arial", 12, "bold"),bg="white",bd=2,relief=RIDGE,)
        refno.place(x=115,y=0)
        medname=Label(dataframeright,font=("arial", 10, "bold"), text="MEDICINE NAME")
        medname.place(x=0,y=25)
        medname=Entry(dataframeright,textvariable=self.addmedvar,width=19, font=("arial", 12, "bold"),bg="white",bd=2,relief=RIDGE,)
        medname.place(x=115,y=25)
        sideframe=Frame(dataframeright,bd=4,relief=RIDGE,bg="white")
        sideframe.place(x=0,y=80,width=290,height=185)
        #**********************************SCROLL BAR RIGHT FRAME MINI******************************************
        x=ttk.Scrollbar(sideframe,orient=HORIZONTAL)
        x.pack(side=BOTTOM,fill=X)
        y=ttk.Scrollbar(sideframe,orient=VERTICAL)
        y.pack(side=RIGHT,fill=Y)
        self.medtable=ttk.Treeview(sideframe,column=("REF","MEDNAME"),xscrollcommand=x.set,yscrollcommand=y.set)
        x.config(command=self.medtable.xview)
        y.config(command=self.medtable.yview)
        self.medtable.heading("REF",text=("REF"))
        self.medtable.heading("MEDNAME",text=("MEDICINE NAME"))
        self.medtable["show"]="headings"
        self.medtable.pack(fill=BOTH,expand=1)
        self.medtable.column("REF",width=100)
        self.medtable.column("MEDNAME",width=100)
        self.medtable.bind("<ButtonRelease-1>",self.medget) #BINDING DATA FROM SMALL FRAME TO REF AND MEDNMAE
        #*******************************MAKING OF ADDD,UPDATE,DELETE,CLEAR PORTION->RIGHTFRAME***********************
        downframe=Frame(dataframeright,bd=4,relief=RIDGE,bg="darkred")
        downframe.place(x=320,y=110,width=135,height=160)
        btnAddmed=Button(downframe,command=self.AddMed,text=" ADD  ",width=12,
                      font=("arial",12,"bold"),bg="darkgreen",fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)
        btnUpdatemed=Button(downframe,command=self.updatemed,text=" UPDATE  ",width=12,
                      font=("arial",12,"bold"),bg="orange",fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)
        btnDeletemed=Button(downframe,command=self.deletemed,text="  DELETE ",width=12,
                     font=("arial",12,"bold"),bg="red",fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)
        btnClearmed=Button(downframe,command=self.clearmed,text=" CLEAR  ",width=12,
                      font=("arial",12,"bold"),bg="purple",fg="white",pady=4)
        btnClearmed.grid(row=3,column=0)
        #****************************************LOWER FRAME****************************************************
        Framedeatils=Frame(self.root,bd=7,relief=RIDGE)
        Framedeatils.place(x=4,y=525,width=1260,height=115)
        #*************************************LOWER FRAME TABLE AND SCROLLBAR***********************************
        Tableframe=Frame(Framedeatils, bd=5, relief=RIDGE)
        Tableframe.place(x=0,y=0,width=1250,height=105)
        scrollx=ttk.Scrollbar (Tableframe,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly=ttk.Scrollbar (Tableframe,orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)
        self.pharmacy_table=ttk.Treeview(Tableframe,column=("reg", "companyname", "type", "tabletname", "lotno", "issuedate","expdate", "uses", "sideeffect", "warning", "dosage", "price", "productqty"),
                                          xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.pharmacy_table.xview)
        scrolly.config(command=self.pharmacy_table.yview)
        self.pharmacy_table["show"]="headings"
        self.pharmacy_table.heading("reg", text="REF NO")
        self.pharmacy_table.heading("companyname", text="COMPANY NAME")
        self.pharmacy_table.heading("type", text="TYPE OF MEDICINE")
        self.pharmacy_table.heading("tabletname",text="MEDICINE NAME")
        self.pharmacy_table.heading("lotno", text="LOT NO")
        self.pharmacy_table.heading("issuedate", text="ISSUE DATE")
        self.pharmacy_table.heading("expdate", text="EXP DATE")
        self.pharmacy_table.heading("uses", text="USES")
        self.pharmacy_table.heading("sideeffect", text="SIDE EFFECT")
        self.pharmacy_table.heading("warning", text="WARNINGS")
        self.pharmacy_table.heading("dosage", text="DOSAGE")
        self.pharmacy_table.heading("price", text="MED PRICE")
        self.pharmacy_table.heading("productqty", text="PRODUCT QTY")
        self.pharmacy_table.pack(fill=BOTH,expand=1)
        #***********************************WIDTH TO LOWER FRAME CONTENT FOR SCROLLING*******************************
        self.pharmacy_table.column("reg",width=50)
        self.pharmacy_table.column("companyname",width=90)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=40)
        self.pharmacy_table.column("issuedate",width=70)
        self.pharmacy_table.column("expdate",width=70)
        self.pharmacy_table.column("uses",width=35)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=70)
        self.pharmacy_table.column("dosage",width=60)
        self.pharmacy_table.column("price",width=70)
        self.pharmacy_table.column("productqty",width=100)
        self.fetchdataMed()

                   #******************************CREATING TABLE IN MYSQL*******************************************
                   #FIRSTLY CREATE DATABASE NAMELY UMMTRACKER AND THEN CREATE TWO TABLES IN THAT--->PHARMA AND 
                   #**********************************WORKING OF ADD BUTTON*****************************************
    def AddMed(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="7006760858",database="UMMTRACKER")
        cursor=conn.cursor()
        val1=self.addrefvar.get()
        val2=self.addmedvar.get()
        query="INSERT INTO PHARMA(Ref,Medname) VALUES (%s,%s)"
        values=(val1,val2)
        cursor.execute(query,values)
        conn.commit()
        messagebox.showinfo("Success","MEDICINE ADDED SUCCESSFULLY")
        conn.close()
        self.fetchdataMed()
        self.medget()
        self.root.update_idletasks()
        

#***************************SHOWING DATA ADDED IN RIGHT SIDE SMALL WINDOW********************************************
    def fetchdataMed(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="7006760858",database="UMMTRACKER")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM PHARMA")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.medtable.delete(*self.medtable.get_children())
            for i in rows:
                self.medtable.insert("",END,values=i)
        conn.commit()
        conn.close()
    def medget(self,event=""):
        row=self.medtable.focus()
        content=self.medtable.item(row)
        rows=content["values"]
        self.addrefvar.set(rows[0])
        self.addmedvar.set(rows[1])
        #***************************UPDATING DATA IN SMALL WINDOW RIGHT SIDE********************************************
    def updatemed(self):
            if self.addrefvar.get()=="" or self.addmedvar.get()=="":
                messagebox.showerror("Error","BOTH FIELDS ARE REQUIRED")
            else:
                 conn=mysql.connector.connect(host="localhost",user="root",password="7006760858",database="UMMTRACKER")
                 cursor=conn.cursor()
                 cursor.execute("UPDATE PHARMA SET MEDNAME=%s WHERE REF=%s",(
                                                               self.addmedvar.get(),
                                                            self.addrefvar.get()
                 ))
                 conn.commit()
                 print("updated successfully")
                 messagebox.showinfo("Success","DATA UPDATED SUCCESSFULLY")
                 self.fetchdatamed()
                 conn.close()
               
        #******************************************************DELETING MEDICINE ITEM**************************************
    def deletemed(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="7006760858",database="UMMTRACKER")
        cursor=conn.cursor()
        query="DELETE FROM PHARMA WHERE REF=%s"
        value=(self.addrefvar.get(),)
        cursor.execute(query,value)
        conn.commit()
        self.fetchdataMed()
        conn.close()
        messagebox.showinfo("Success","DATA DELETED SUCCESSFULLY")
         #******************************************************CLEARING  MEDICINE ITEM FROM REF AND MEDNAME**************************************
    def clearmed(self):
        self.addrefvar.set("")
        self.addmedvar.set("")
        messagebox.showinfo("Success","DATA CLEARED SUCCESSFULLY")

                #***********************************WORKING OF LOWER BUTTONS:************************************
    
    def AddMedlower(self):
        if self.refvar.get()=="" or self.cpynamevar.get()=="":
                messagebox.showerror("Error","BOTH FIELDS ARE REQUIRED")
        else:
          conn = mysql.connector.connect(host="localhost",user="root",password="7006760858",database="UMMTRACKER")
          cursor = conn.cursor()
          val1 = self.refvar.get()
          val2 = self.cpynamevar.get()
          val3 = self.typevar.get()
          val4 = self.mednamevar.get()
          val5 = self.lotvar.get() 
          val6 = self.issuevar.get()  
          val7 = self.expirevar.get()  
          val8 = self.usesvar.get()
          val9 = self.efectsvar.get()
          val10 = self.warningvar.get()
          val11 = self.dosagevar.get()
          val12 = self.pricevar.get()
          val13 = self.qntyvar.get()
          query = """
        INSERT INTO PHDATA (REFNO, COMPANYNAME, MEDICINETYPE, MEDICINENAME, LOTNO, ISSUEDAT, EXPDAT, USES, EFFECTS, WARNINGS, DOSAGE, MEDPRICE, QNTY)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
          values = (val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13)

          cursor.execute(query, values)
          conn.commit()
          messagebox.showinfo("Success", "Data inserted successfully!")
          conn.close()





if __name__ =="__main__":
    root=Tk()
    obj=ummtracker(root)
    root.mainloop() #CLOSING OF ROOT
         
