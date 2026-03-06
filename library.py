from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter



class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1200x600+100+100") 


        #==================================Variable==================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.authorname_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.actualprice_var=StringVar()



        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",font=("times new roman",50,"bold"),bg="powder blue",fg="green",bd=20,relief=RIDGE,padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        #==================================DataFrame Left==================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",font=("times new roman",12,"bold"),bg="powder blue",fg="black",bd=12,relief=RIDGE,padx=2,pady=6)
        DataFrameLeft.place(x=0,y=5,width=900,height=365)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",12,"bold"),width=27,state="readonly")
        comMember["values"]=("Select","Admin Staff","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1,)

        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN No",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,textvariable=self.prn_var,font=("times new roman",13,"bold"),width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",font=("arial",12,"bold"),padx=2,pady=4,text="ID No:")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,textvariable=self.id_var,font=("arial",13,"bold"),width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstname=Label(DataFrameLeft,bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6,text="First Name:")
        lblFirstname.grid(row=3,column=0,sticky=W)
        txtFirstname=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("arial",13,"bold"),width=29)
        txtFirstname.grid(row=3,column=1)

        lblLastname=Label(DataFrameLeft,bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6,text="Last Name:")
        lblLastname.grid(row=4,column=0,sticky=W)
        txtLastname=Entry(DataFrameLeft,textvariable=self.lastname_var,font=("arial",13,"bold"),width=29)
        txtLastname.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6,text="Address 1:")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,textvariable=self.address1_var,font=("arial",13,"bold"),width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6,text="Address 2:")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,textvariable=self.address2_var,font=("arial",13,"bold"),width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="powder blue",font=("arial",12,"bold"),padx=2,pady=4,text="Post Code:")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,textvariable=self.postcode_var,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6,text="Mobile No:")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6,text="Book ID:")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("arial",12,"bold"),width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6,text="Book Title:")
        lblBookTitle.grid(row=1,column=2,sticky=W)  
        txtBookTitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("arial",12,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6,text="Author Name:")
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,textvariable=self.authorname_var,font=("arial",12,"bold"),width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6,text="Date Borrowed:")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("arial",12,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6,text="Date Due:")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("arial",12,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6,text="Days On Book:")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,textvariable=self.daysonbook_var,font=("arial",12,"bold"),width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6,text="Late Return Fine:")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,textvariable=self.latereturnfine_var,font=("arial",12,"bold"),width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDue=Label(DataFrameLeft,bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6,text="Date Over Due:")
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,textvariable=self.dateoverdue_var,font=("arial",12,"bold"),width=29)
        txtDateOverDue.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6,text="Actual Price:")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,textvariable=self.actualprice_var,font=("arial",12,"bold"),width=29)
        txtActualPrice.grid(row=8,column=3)

        #==================================DataFrame Right==================================

        DataFrameRight=LabelFrame(frame,text="Book Details",font=("times new roman",12,"bold"),bg="powder blue",fg="black",bd=12,relief=RIDGE,padx=2,pady=6)
        DataFrameRight.place(x=910,y=5,width=570,height=365)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        #==================================Fetch Books from DB==================================
        def fetch_book_titles():
            book_titles = []
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="munu@123",database="library_management_system")
                my_cursor=conn.cursor()
                my_cursor.execute("select BookTitle from books")
                rows=my_cursor.fetchall()
                for row in rows:
                    book_titles.append(row[0])
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}")
            return book_titles

        listBooks=fetch_book_titles()

        #==================================Function to select book==================================
        def SelectBook(events=""):
            value=str(listBox.get(listBox.curselection()))
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="munu@123",database="library_management_system")
                my_cursor=conn.cursor()
                query="select * from books where BookTitle=%s"
                value_tuple=(value,)
                my_cursor.execute(query,value_tuple)
                row=my_cursor.fetchone()
                conn.close()

                if row:
                    self.bookid_var.set(row[0])
                    self.booktitle_var.set(row[1])
                    self.authorname_var.set(row[2])
                    self.actualprice_var.set(row[3])
                    d1=datetime.datetime.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set("15")
                    self.latereturnfine_var.set("Rs.100")
                    self.dateoverdue_var.set("No")
                else:
                    messagebox.showerror("Error","Book not found in database")

            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}")
        
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=24,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        #==================================Button Frame==================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)
        
        # Make the single grid row expand to the full frame height so buttons center vertically
        Framebutton.grid_rowconfigure(0, weight=1)
       
        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnAddData.grid(row=0,column=0)

        btnShowData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnShowData.grid(row=0,column=1)

        btnUpdate=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnDelete.grid(row=0,column=3)

        btnReset=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnReset.grid(row=0,column=4)

        btnExit=Button(Framebutton,command=self.Exit,text="Exit",font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnExit.grid(row=0,column=5)

        #==================================Information Frame==================================
        frameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frameDetails.place(x=0,y=600,width=1530,height=195)

        Table_frame=Frame(frameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1470,height=166)

        xscrollbar=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscrollbar=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,columns=("membertype","prnno","idno","firstname","lastname","address1","address2",
                                                             "postcode","mobile","bookid","booktitle","authorname","dateborrowed",
                                                             "datedue","daysonbook","latereturnfine","dateoverdue","actualprice"),
                                                             xscrollcommand=xscrollbar.set,yscrollcommand=yscrollbar.set)
        
        xscrollbar.pack(side=BOTTOM,fill=X)
        yscrollbar.pack(side=RIGHT,fill=Y)
        xscrollbar.config(command=self.library_table.xview)
        yscrollbar.config(command=self.library_table.yview)


        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("idno",text="ID No")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address 1")
        self.library_table.heading("address2",text="Address 2")
        self.library_table.heading("postcode",text="Post Code")
        self.library_table.heading("mobile",text="Mobile No")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("authorname",text="Author Name")
        self.library_table.heading("dateborrowed",text="Date Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("daysonbook",text="Days On Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("actualprice",text="Actual Price")
        
        self.library_table['show']='headings'
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("idno",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postcode",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("authorname",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("daysonbook",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("actualprice",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


#==================================Function Declaration==================================

#==================================Add Data==================================
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="munu@123",database="library_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                          (self.member_var.get(),self.prn_var.get(),self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(),
                           self.address1_var.get(),self.address2_var.get(),self.postcode_var.get(),self.mobile_var.get(),self.bookid_var.get(),
                           self.booktitle_var.get(),self.authorname_var.get(),self.dateborrowed_var.get(),self.datedue_var.get(),self.daysonbook_var.get(),
                           self.latereturnfine_var.get(),self.dateoverdue_var.get(),self.actualprice_var.get()))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success","Member has been added successfully")

#==================================Update Data==================================
    def update(self):
        if self.prn_var.get()=="" or self.prn_var.get()=="":
            messagebox.showerror("Error","Please enter PRN No to delete member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="munu@123",database="library_management_system")
            my_cursor=conn.cursor()
            my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,Postcode=%s,Mobile=%s,Bookid=%s,Booktitle=%s,Author=%s,Dateborrowed=%s,Datedue=%s,Daysonbook=%s,Latereturnfine=%s,Dateoverdue=%s,Actualprice=%s where PRN_NO=%s",
                              (self.member_var.get(),self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(),
                               self.address1_var.get(),self.address2_var.get(),self.postcode_var.get(),self.mobile_var.get(),self.bookid_var.get(),
                               self.booktitle_var.get(),self.authorname_var.get(),self.dateborrowed_var.get(),self.datedue_var.get(),self.daysonbook_var.get(),
                               self.latereturnfine_var.get(),self.dateoverdue_var.get(),self.actualprice_var.get(),self.prn_var.get()))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Update","Member details has been updated successfully")
       
#==================================Fetch Data================================== 
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="munu@123",database="library_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for row in rows:
                self.library_table.insert('',END,values=row)
            conn.commit()
        conn.close()
        
#==================================Get Cursor==================================
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.authorname_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook_var.set(row[14])
        self.latereturnfine_var.set(row[15])
        self.dateoverdue_var.set(row[16])
        self.actualprice_var.set(row[17])

#==================================Show Data==================================
    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN No:\t\t"+self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID No:\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"First Name:\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"Last Name:\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address 1:\t\t"+self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address 2:\t\t"+self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Post Code:\t\t"+self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book ID:\t\t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title:\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author Name:\t\t"+self.authorname_var.get()+"\n")
        self.txtBox.insert(END,"Date Borrowed:\t\t"+str(self.dateborrowed_var.get())+"\n")
        self.txtBox.insert(END,"Date Due:\t\t"+str(self.datedue_var.get())+"\n")
        self.txtBox.insert(END,"Days On Book:\t\t"+self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END,"Late Return Fine:\t\t"+self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"Date Over Due:\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"Actual Price:\t\t"+self.actualprice_var.get()+"\n")

#==================================Reset Data==================================
    def reset(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.authorname_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook_var.set("")
        self.latereturnfine_var.set("")
        self.dateoverdue_var.set("")
        self.actualprice_var.set("")
        self.txtBox.delete("1.0",END)

#==================================Exit==================================
    def Exit(self):
        Exit=tkinter.messagebox.askyesno("Library Management System","Confirm if you want to exit")
        if Exit>0:
            self.root.destroy()
            return
        

#==================================Delete Data==================================
    def delete(self):
        if self.prn_var.get()=="" or self.prn_var.get()=="":
            messagebox.showerror("Error","Please enter PRN No to delete member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="munu@123",database="library_management_system")
            my_cursor=conn.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),) 
            my_cursor.execute(query,value)
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("Delete","Member has been deleted successfully")



if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
