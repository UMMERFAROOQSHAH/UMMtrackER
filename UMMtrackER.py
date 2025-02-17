from tkinter import * 
from PIL import Image,ImageTk #FOR SETTING IMAGES.
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
        button=Button(buttonframe,text="ADD MEDICINE",
                      font=("arial",12,"bold"),bg="darkred",fg="white")
        button.grid(row=0,column=0,padx=0,pady=5)
        button=Button(buttonframe,text="  UPDATE  ",
                      font=("arial",12,"bold"),bg="darkred",fg="white")
        button.grid(row=0,column=1,padx=0,pady=5)
        button=Button(buttonframe,text="  DELETE  ",
                      font=("arial",12,"bold"),bg="darkred",fg="white")
        button.grid(row=0,column=2,padx=0,pady=5)
        button=Button(buttonframe,text="  RESET  ",
                      font=("arial",12,"bold"),bg="darkred",fg="white")
        button.grid(row=0,column=3,padx=0,pady=5)
        button=Button(buttonframe,text="  EXIT  ",
                      font=("arial",12,"bold"),bg="darkred",fg="white")
        button.grid(row=0,column=4,padx=0,pady=5)
             #SEARCH BY OPTION:-
        Iblsearch=Label(buttonframe,font=("ariel",17,"bold"),
                        text="  SEARCH BY  ",
                        padx=2,bg="darkred",fg="white",)
        Iblsearch.grid(row=0,column=5,padx=0,pady=5,sticky=W)
          #**********************************************************DAY2************************************************************
        









if __name__ =="__main__":
    root=Tk()
    obj=ummtracker(root)
    root.mainloop() #CLOSING OF ROOT
        
