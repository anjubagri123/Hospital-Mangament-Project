from tkinter import *
from tkinter import ttk
import random
import time
import datetime as dt
from tkinter import messagebox
import pymysql

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("HOSPITAL MANAGEMENT SYSTEM")
        self.root.geometry("1349x700+0+0")  #widthXheight+x axis start+y axis start


  #============All Variable=============#
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.Expdate=StringVar()
        self.DailyDose=StringVar()
        self.sideeffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.Drivingusingmachine=StringVar()
        self.HowtouseMedi=StringVar()
        self.PAtientID=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateofBirth=StringVar()
        self.PatientAddress=StringVar()










          #====================label=====================#
        # lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",fg="dark blue",bg="White",font=("cursive",42,"bold"))
        # lbltitle.pack(side=TOP,fill=X)

        #==========Timing System==============
 #=============CLOCK==============#
        T_frame = Frame(self.root, bd=10, relief=RIDGE, bg="dark blue")
        T_frame.place(x=0, y=0, width=1349, height=100)
        I_lb1 = Label(T_frame, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white",bg="dark blue",font=("times new roman", 15, "bold"),
                       bd=0).place(x=10, y=7)

        def clock():
            G_time = time.strftime("%H:%M:%S")
            clock_lb3.config(text=G_time)
            clock_lb3.after(1000, clock)

        clock_lb3 = Label(T_frame, font=("times new roman", 17, "bold"), fg='white',bg="dark blue", bd=0)
        clock_lb3.place(x=1200, y=7)
        clock()
        # ..............................................................................................................................................
        I_lb2 = Label(T_frame, text="+Hospital Management System", font=("times new roman", 40, "bold"), bg='dark blue',
                      fg='white', bd=0).place(x=315, y=4)
        #=========end top time frame===============#
        #================Data Frame===========#
        Dataframe=Frame(self.root,bd=10,relief=RIDGE)
        Dataframe.place(x=0,y=109,width=1349,height=400)

        #==============data frame left============#
        dataframeleft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Patient Information")
        dataframeleft.place(x=0,y=5,width=980,height=375)

         #==============dataframe right==================#
        dataframeright=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Prescription")
        dataframeright.place(x=985,y=5,width=345,height=375)

        #===================buttons frame===============#

        buttonDataframe=Frame(self.root,bd=10,relief=RIDGE)
        buttonDataframe.place(x=0,y=500,width=1349,height=70)

        #==================details frame================#
        detailsDataframe=Frame(self.root,bd=10,relief=RIDGE)
        detailsDataframe.place(x=0,y=570,width=1349,height=125)

 #========================data frame left===============#
    #==========label Name Tablet==========#
        lblnametablet=Label(dataframeleft,text="Names of Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblnametablet.grid(row=0,column=0,sticky=W)
      #==========Combo Box for NAME OF TABLET=========#
        combo_nametab=ttk.Combobox(dataframeleft,textvariable=self.Nameoftablets,font=("times new roman",13,"bold"),width=32,state='readonly')         #state readonly means user can't write
        combo_nametab['values']=("Select","Paracetamol","Disprin","Citrazin","Amlycure","MeftalSpas")
        combo_nametab.grid(row=0,column=1,padx=20,pady=10)
        combo_nametab.current(0)

        
    #==========label Reference no==========#     
        lblReferenceno=Label(dataframeleft,text="Reference No.",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblReferenceno.grid(row=1,column=0,sticky=W)
      #===========Text box refrence no==========#
        txt_Refno=Entry(dataframeleft,textvariable=self.ref,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_Refno.grid(row=1,column=1,pady=1,padx=20,sticky="w")

    #===============label dose==========#
        lbldose=Label(dataframeleft,text="Dose",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbldose.grid(row=2,column=0,sticky=W)
      #=============text dose=============#
        txt_Dose=Entry(dataframeleft,textvariable=self.Dose,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_Dose.grid(row=2,column=1,pady=1,padx=20,sticky="w")

    #================label no of tablet=============#
        lblnooftablet=Label(dataframeleft,text="No of Tablets",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblnooftablet.grid(row=3,column=0,sticky=W)
      #=============text no of tab===========#
        txt_Nooftab=Entry(dataframeleft,textvariable=self.NumberofTablets,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_Nooftab.grid(row=3,column=1,pady=1,padx=20,sticky="w")

    #==============label lot================#  
        lblLOT=Label(dataframeleft,text="Lot",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLOT.grid(row=4,column=0,sticky=W)
      #=============text lot==============#
        txt_lot=Entry(dataframeleft,textvariable=self.Lot,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_lot.grid(row=4,column=1,pady=1,padx=20,sticky="w")  

    

    #=============label Issue date==========#
        lblissuedate=Label(dataframeleft,text="Issue date",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblissuedate.grid(row=5,column=0,sticky='w')

        #=============text issue date===========#
        txt_IssueDate=Entry(dataframeleft,textvariable=self.IssueDate,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_IssueDate.grid(row=5,column=1,pady=1,padx=20,sticky="w")

    
      #===========Exp date label=============#  
        lblExpdate=Label(dataframeleft,text="Exp Date",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblExpdate.grid(row=6,column=0,sticky='w')
       #==============text box exp date===========#
        txt_expdate=Entry(dataframeleft,textvariable=self.Expdate,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_expdate.grid(row=6,column=1,pady=1,padx=20,sticky="w")

    #=============label daily dose============#
        lblDailydose=Label(dataframeleft,text="Daily Dose",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDailydose.grid(row=7,column=0,sticky='w')



      #============text box daily dose================#
        txt_dlydose=Entry(dataframeleft,textvariable=self.DailyDose,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_dlydose.grid(row=7,column=1,pady=1,padx=20,sticky="w")

    #===============label side effect==============#
        lblSideEffect=Label(dataframeleft,text="Side Effect",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky='w')
      #============text box side effect=============#
        txt_sideeff=Entry(dataframeleft,textvariable=self.sideeffect,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_sideeff.grid(row=8,column=1,pady=1,padx=20,sticky="w")

#============Right Side Text Entry Fields===============#
     #=============label further info============#
        lblFurtherInfo=Label(dataframeleft,text="Further Information",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblFurtherInfo.grid(row=0,column=2)
      #============text box further info===========#
        txt_furinfo=Entry(dataframeleft,textvariable=self.FurtherInformation,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_furinfo.grid(row=0,column=3,pady=1,padx=20,sticky="w")


       #========label blood pressure no==============# 
        lblBloodPressure=Label(dataframeleft,text="Blood Pressure",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        #==========text box blood pressure============#
        txt_bldpresur=Entry(dataframeleft,textvariable=self.Drivingusingmachine,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_bldpresur.grid(row=1,column=3,pady=1,padx=20,sticky="w")


        #===========label storage advice==================#
        lblStorageAD=Label(dataframeleft,text="Storage Advice",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblStorageAD.grid(row=2,column=2,sticky='w')
        #======text box storege advice=========#
        txt_storagead=Entry(dataframeleft,textvariable=self.StorageAdvice,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_storagead.grid(row=2,column=3,pady=1,padx=20,sticky="w")


       #==============label madiaction=========#
        lblMedi=Label(dataframeleft,text="Medication",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMedi.grid(row=3,column=2,sticky=W)
        #=========text box medi=========#
        txt_medi=Entry(dataframeleft,textvariable=self.HowtouseMedi,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_medi.grid(row=3,column=3,pady=1,padx=20,sticky="w")

       #==============label patient id=============#
        lblPatientID=Label(dataframeleft,text="Patient ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPatientID.grid(row=4,column=2,sticky=W)
        #===========text ptient id===========#
        txt_patientid=Entry(dataframeleft,textvariable=self.PAtientID,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_patientid.grid(row=4,column=3,pady=1,padx=20,sticky="w")

         #==============label Nhs No=========#
        lblNHS=Label(dataframeleft,text="NHS Number",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNHS.grid(row=5,column=2,sticky=W)
        #==========text box nhs no===========#
        txt_nhsno=Entry(dataframeleft,textvariable=self.nhsNumber,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_nhsno.grid(row=5,column=3,pady=1,padx=20,sticky="w")

        #=============label pateint name===========#
        lblPatientName=Label(dataframeleft,text="Patient Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        #==========text Box =============#
        txt_patientname=Entry(dataframeleft,textvariable=self.PatientName,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_patientname.grid(row=6,column=3,pady=1,padx=20,sticky="w")

        #===========label date of birth==============#
        lblDOB=Label(dataframeleft,text="Date of Birth",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDOB.grid(row=7,column=2,sticky=W)
        #============text box=========#
        txt_dob=Entry(dataframeleft,textvariable=self.DateofBirth,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_dob.grid(row=7,column=3,pady=1,padx=20,sticky="w")

      #============Label Patient Address===========#
        lblPateintAdd=Label(dataframeleft,text="Patient Address",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPateintAdd.grid(row=8,column=2,sticky=W)
        #===========patient Add text box============#
        txt_pateintadd=Entry(dataframeleft,textvariable=self.PatientAddress,font=("times new roman",15,"bold"),width=30,bd=5,relief=GROOVE)
        txt_pateintadd.grid(row=8,column=3,pady=1,padx=20,sticky="w")

  #===========text box for prescription frame============#
        self.txt_prescript=Text(dataframeright,font=("times new roman",15,"bold"),width=30,height=15,padx=2,pady=0)
        self.txt_prescript.grid(row=0,column=0)

#==========Buttons Frame==============#
        # # #==================button Frame==============#
        # btn_Frame=Frame(buttonDataframe,bd=4,relief=RIDGE,bg="GREEN")
        # btn_Frame.place(x=10,y=525,width=425)

        # ==============buttons: Prescription,Presctiption data , Update , Delete ,Reset, Exit ===========#
        # Presbtn=Button(buttonDataframe,text="Prescription",bg="green",fg="white",font=("times new roman",12,"bold"),width=23,height=2,padx=2,pady=6)
        # Presbtn.grid(row=0,column=0)

        Presbtn=Button(buttonDataframe,text="Prescription",command=self.iprescription,font=("times new roman",12,"bold"),width=24,height=2,bg="dark blue",fg="white").grid(row=0,column=0,padx=0,pady=0)

        PresDatabtn=Button(buttonDataframe,text="Prescription Data",command=self.iPrescriptionData,font=("times new roman",12,"bold"),width=24,height=2,bg="dark blue",fg="white").grid(row=0,column=1,padx=0,pady=0)
        # PresDatabtn.grid(row=0,column=1)

        Updatebtn=Button(buttonDataframe,text="Update",command=self.update,font=("times new roman",12,"bold"),width=24,height=2,bg="dark blue",fg="white").grid(row=0,column=2,padx=0,pady=0)
        # Updatebtn.grid(row=0,column=2)

        Deletebtn=Button(buttonDataframe,text="Delete",command=self.idelete,font=("times new roman",12,"bold"),width=24,height=2,bg="dark blue",fg="white").grid(row=0,column=3,padx=0,pady=0)
        # Deletebtn.grid(row=0,column=3)

        Resetbtn=Button(buttonDataframe,text="Reset",command=self.clear,font=("times new roman",12,"bold"),width=24,height=2,bg="dark blue",fg="white").grid(row=0,column=4,padx=0,pady=0)
        # Resetbtn.grid(row=0,column=4)
        
        Exitbtn=Button(buttonDataframe,text="Exit",command=self.exit,font=("times new roman",12,"bold"),width=21,height=2,bg="dark blue",fg="white").grid(row=0,column=5,padx=0,pady=0)
        # Exitbtn.grid(row=0,column=5)

        # #==============table Frame====================#
        # Table_Frame=Frame(detailsDataframe,bd=4,relief=RIDGE,bg="dark blue")
        # Table_Frame.place(x=10,y=70,width=790,height=510)

        #==================scrollbar X And Y =================#
        scroll_x=Scrollbar(detailsDataframe,orient=HORIZONTAL)
        scroll_y=Scrollbar(detailsDataframe,orient=VERTICAL)
        self.Patient_Table=ttk.Treeview(detailsDataframe,columns=("nameoftable","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        # scroll_x.config(command=self.Patient_table.xview)
        # scroll_y.config(command=self.Patient_table.yview)
        scroll_x=ttk.Scrollbar(command=self.Patient_Table.xview)
        scroll_y=ttk.Scrollbar(command=self.Patient_Table.yview)

        self.Patient_Table.heading("nameoftable",text="Name of Table")
        self.Patient_Table.heading("ref",text="Reference No.")
        self.Patient_Table.heading("dose",text="Dose")
        self.Patient_Table.heading("nooftablets",text="Name of Tablets")
        self.Patient_Table.heading("lot",text="LOT")
        self.Patient_Table.heading("issuedate",text="Issue Date")
        self.Patient_Table.heading("expdate",text="Exp Date")
        self.Patient_Table.heading("dailydose",text="DailyDose")
        self.Patient_Table.heading("storage",text="Storage")
        self.Patient_Table.heading("nhsnumber",text="NHS No.")
        self.Patient_Table.heading("pname",text="Pname")
        self.Patient_Table.heading("dob",text="DOB")
        self.Patient_Table.heading("address",text="Address")

        self.Patient_Table['show']='headings'
        
        self.Patient_Table.column("nameoftable",width=100)
        self.Patient_Table.column("ref",width=100)
        self.Patient_Table.column("dose",width=100)
        self.Patient_Table.column("nooftablets",width=100)
        self.Patient_Table.column("lot",width=100)
        self.Patient_Table.column("issuedate",width=100)
        self.Patient_Table.column("expdate",width=100)
        self.Patient_Table.column("dailydose",width=100)
        self.Patient_Table.column("storage",width=100)
        self.Patient_Table.column("nhsnumber",width=100)
        self.Patient_Table.column("pname",width=100)
        self.Patient_Table.column("dob",width=100)
        self.Patient_Table.column("address",width=100)


        self.Patient_Table.pack(fill=BOTH,expand=1)      # fill= Both means do white in full frame and expand for truly done the functionality
        self.Patient_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetchdata()

        # self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
 #===================FUNCTIONALITY DECLARATION=================#
    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are Required")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="hms db")
            cur=con.cursor()
            cur.execute("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.IssueDate.get(),
                self.Expdate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateofBirth.get(),
                self.PatientAddress.get()
                
                
            ))
                                                                        
                                                                         
            
            con.commit()
            self.fetchdata()
            con.close()
            messagebox.showinfo("Success","Record has been inserted.")

    
    def update(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="hms db")
            cur=con.cursor()
            cur.execute("update patient set Nameoftablets=%s,dose=%s,Numbersoftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,DOB=%s,patientaddress=%s where Reference_No=%s",(
                
                self.Nameoftablets.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.IssueDate.get(),
                self.Expdate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateofBirth.get(),
                self.PatientAddress.get(),
                self.ref.get()
                
                
            ))
                                                                        
            con.commit()
            self.fetchdata()
            con.close()
            messagebox.showinfo("Success","Record has been updated successfully.")
                                                             
            
                   
                        
            

                        
                        
                        
                        
                        
            
                        
                        
                                                                                                                                                                                                                                                                                                                                                                                                                              
    def fetchdata(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="hms db")
            cur=con.cursor()
            cur.execute("select * from patient")  
            rows=cur.fetchall()
            if len(rows)!=0:
                 self.Patient_Table.delete(*self.Patient_Table.get_children())
                 for i in rows:
                      self.Patient_Table.insert("",END,values=i)
                 con.commit()
            con.close()

    def get_cursor(self,eve):
            cursor_row=self.Patient_Table.focus()
            content=self.Patient_Table.item(cursor_row)
            row=content["values"]
            self.Nameoftablets.set(row[0])
            self.ref.set(row[1])
            self.Dose.set(row[2])
            self.NumberofTablets.set(row[3])
            self.Lot.set(row[4])
            self.IssueDate.set(row[5])
            self.Expdate.set(row[6])
            self.DailyDose.set(row[7])
            self.StorageAdvice.set(row[8])
            self.nhsNumber.set(row[9])
            self.PatientName.set(row[10])
            self.DateofBirth.set(row[11])
            self.PatientAddress.set(row[12])

    def iprescription(self):
         self.txt_prescript.insert(END,"Name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
         self.txt_prescript.insert(END,"Reference No.:\t\t\t"+self.ref.get()+"\n")
         self.txt_prescript.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
         self.txt_prescript.insert(END,"Number of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
         self.txt_prescript.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
         self.txt_prescript.insert(END,"Issue Date:t\t\t"+self.IssueDate.get()+"\n")
         self.txt_prescript.insert(END,"Expire Dateate:\t\t\t"+self.Expdate.get()+"\n")
         self.txt_prescript.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
         self.txt_prescript.insert(END,"Side Effect:\t\t\t"+self.sideeffect.get()+"\n")
         self.txt_prescript.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
         self.txt_prescript.insert(END,"Storage Advice:\t\t\t"+self.StorageAdvice.get()+"\n")
         self.txt_prescript.insert(END,"Blood Pressure:\t\t\t"+self.Drivingusingmachine.get()+"\n")
        #  self.txt_prescript.insert(END,"Patient Id:\t\t\t"+self.HowtouseMedi.get()+"\n")
         self.txt_prescript.insert(END,"Patient Id:\t\t\t"+self.PAtientID.get()+"\n")
         self.txt_prescript.insert(END,"NHS Number:\t\t\t"+self.nhsNumber.get()+"\n")
         self.txt_prescript.insert(END,"Patient Name:\t\t\t"+self.PatientName.get()+"\n")
         self.txt_prescript.insert(END,"Date of Birth:\t\t\t"+self.DateofBirth.get()+"\n")
         self.txt_prescript.insert(END,"Patient Address:\t\t\t"+self.PatientAddress.get()+"\n")
         

    def idelete(self):
         con=pymysql.connect(host="localhost",user="root",password="",database="hms db")
         cur=con.cursor()
         query="delete from patient where Reference_No=%s"
         value=(self.ref.get(),)
         cur.execute(query,value)   #second way to write query

         con.commit()
         con.close()
         self.fetchdata()
         messagebox.showinfo("Delete","Patient has been deleted successfully")
    

    def clear(self):
         self.Nameoftablets.set("")
         self.ref.set("")
         self.Dose.set("")
         self.NumberofTablets.set("")
         self.Lot.set("")
         self.IssueDate.set("")
         self.Expdate.set("")
         self.DailyDose.set("")
         self.sideeffect.set("")
         self.FurtherInformation.set("")
         self.StorageAdvice.set("")
         self.Drivingusingmachine.set("")
         self.HowtouseMedi.set("")
         self.PAtientID.set("")
         self.nhsNumber.set("")
         self.PatientName.set("")
         self.DateofBirth.set("")
         self.PatientAddress.set("")
         self.txt_prescript.delete("1.0",END)

    def exit(self):
         exit=messagebox.askyesno("Hospital Management System","Confirm you want to exit")
         if exit>0:
              root.destroy()
              return
root = Tk()
ob = Hospital(root)
root.mainloop()
