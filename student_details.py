from tkinter import *
from tkinter import ttk
import sqlite3

a = sqlite3.connect("Students.db")
b = a.cursor()
b.execute("CREATE TABLE IF NOT EXISTS Students(ROLLNUMBER INTEGER, NAME VARCHAR(20), FATHERSNAME VARCHAR(20), DATEOFBIRTH VARCHAR(20), GENDER VARCHAR(20), BLOODGROUP VARCHAR(20), ADDRESS VARCHAR(20))")
a.commit()
a.close()


class student:
    def __init__(self,main):
        self.main=main
        self.t_frame=Frame(self.main, height=50, width=1200, bd=1)
        self.t_frame.pack()
        self.title=Label(self.t_frame, text="STUDENTS PORTAL", font="calibre 20", width=1200, bg="light green")
        self.title.pack()


        self.frame_1= Frame(self.main, height=600,width=450)
        self.frame_1.pack(side=LEFT)
        self.frame_1.pack_propagate(0)

        Label(self.frame_1, text="Student Details", font="calibre 13").pack()

        self.roll_number= Label(self.frame_1, text="Roll Number")
        self.roll_number.place(x=40, y=40)
        self.roll_number_Entry=Entry(self.frame_1, width=40)
        self.roll_number_Entry.place(x=150, y=40)

        self.name = Label(self.frame_1, text="Name")
        self.name.place(x=40, y=80)
        self.name_Entry = Entry(self.frame_1, width=40)
        self.name_Entry.place(x=150, y=80)

        self.f_name = Label(self.frame_1, text="Father's Name")
        self.f_name.place(x=40, y=120)
        self.f_name_Entry = Entry(self.frame_1, width=40)
        self.f_name_Entry.place(x=150, y=120)

        self.date_of_birth = Label(self.frame_1, text="Date Of Birth")
        self.date_of_birth.place(x=40, y=160)
        self.date_of_birth_Entry = Entry(self.frame_1, width=40)
        self.date_of_birth_Entry.place(x=150, y=160)


        self.gender = Label(self.frame_1, text="Gender")
        self.gender.place(x=40, y=200)
        self.gender_Entry = Entry(self.frame_1, width=40)
        self.gender_Entry.place(x=150, y=200)

        self.bloodgroup = Label(self.frame_1, text="Blood Group")
        self.bloodgroup.place(x=40, y=240)
        self.bloodgroup_Entry = Entry(self.frame_1, width=40)
        self.bloodgroup_Entry.place(x=150, y=240)


        self.address = Label(self.frame_1, text="City")
        self.address.place(x=40, y=280)
        self.address_Entry = Entry(self.frame_1, width=40)
        self.address_Entry.place(x=150, y=280)


        self.Button_Frame=Frame(self.frame_1, height=250, width=250)
        self.Button_Frame.place(x=175, y=320)

        self.add=Button(self.Button_Frame, text="Add", width=25, command=self.Add)
        self.add.pack()

        self.update=Button(self.Button_Frame, text="Update", width=25, command=self.Update)
        self.update.pack()

        self.delete=Button(self.Button_Frame, text="Delete", width=25, command=self.Delete)
        self.delete.pack()

        self.clear=Button(self.Button_Frame, text="Clear", width=25, command=self.Clear)
        self.clear.pack()


        self.frame_2 = Frame(self.main, height=600, width=750)
        self.frame_2.pack(side=RIGHT)

        self.col= ttk.Treeview(self.frame_2, columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7"),show='headings', height=25)

        self.col.column("#1", anchor=CENTER,width=75)
        self.col.heading("#1", text="Roll Number")

        self.col.column("#2", anchor=CENTER,width=110)
        self.col.heading("#2", text="Name")

        self.col.column("#3", anchor=CENTER,width=110)
        self.col.heading("#3", text="Father's Name")

        self.col.column("#4", anchor=CENTER,width=100)
        self.col.heading("#4", text="Date Of Birth")

        self.col.column("#5", anchor=CENTER,width=100)
        self.col.heading("#5", text="Gender")

        self.col.column("#6", anchor=CENTER,width=100)
        self.col.heading("#6", text="Blood Group")

        self.col.column("#7", anchor=CENTER,width=100)
        self.col.heading("#7", text="City")
        
        self.col.insert
        self.col.pack()


    def Add(self):
        roll = self.roll_number_Entry.get()
        name = self.name_Entry.get()
        fname = self.f_name_Entry.get()
        dob = self.date_of_birth_Entry.get()
        gender = self.gender_Entry.get()
        bloodgrp = self.bloodgroup_Entry.get()
        city = self.address_Entry.get()
        a = sqlite3.connect("Students.db")
        b = a.cursor()
        b.execute("INSERT INTO Students(ROLLNUMBER, NAME, FATHERSNAME, DATEOFBIRTH, GENDER, BLOODGROUP, ADDRESS) VALUES(?,?,?,?,?,?,?)",(roll, name, fname, dob, gender, bloodgrp, city))
        a.commit()
        a.close()
        print("Student Added Successfully")
        self.col.insert("", index=0, values=(roll, name, fname, dob, gender, bloodgrp, city)) 

    def Update(self):
        roll = self.roll_number_Entry.get()
        name = self.name_Entry.get()
        fname = self.f_name_Entry.get()
        dob = self.date_of_birth_Entry.get()
        gender = self.gender_Entry.get()
        bloodgrp = self.bloodgroup_Entry.get()
        city = self.address_Entry.get()
        row = self.col.selection()[0]
        selected_item = self.col.item(row)['values'][0]
        a = sqlite3.connect("Students.db")
        b = a.cursor()
        b.execute("UPDATE Students SET ROLLNUMBER=?, NAME=?, FATHERSNAME=?, DATEOFBIRTH=?, GENDER=?, BLOODGROUP=?, ADDRESS=? WHERE ROLLNUMBER=?", (selected_item, name, fname, dob, gender, bloodgrp, city, selected_item))
        a.commit()
        a.close()
        print("Student Details Updated Successfully")
        self.col.item(row, values=(roll, name, fname, dob, gender, bloodgrp, city))

    def Delete(self):
        row = self.col.selection()[0]
        selected_row = self.col.item(row)['values'][0]
        a = sqlite3.connect("Students.db")
        b = a.cursor()
        b.execute("DELETE FROM Students WHERE ROLLNUMBER={}".format(selected_row))
        print("Selected Student Row Deleted Successfully")
        a.commit()
        a.close()
        self.col.delete(row)

    def Clear(self):
        self.roll_number_Entry.delete(0,END)
        self.name_Entry.delete(0,END)
        self.f_name_Entry.delete(0,END)
        self.date_of_birth_Entry.delete(0,END)
        self.gender_Entry.delete(0,END)
        self.bloodgroup_Entry.delete(0,END)
        self.address_Entry.delete(0,END)

    
main=Tk()
main.title("STUDENTS PORTAL")
main.geometry("1200x600")

student(main)
main.mainloop()