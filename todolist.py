import pygame
from tkinter import *
from tkinter import messagebox

import databases as db

class ToDoList:
    def __init__(self):
        window = Tk()

        pygame.display.set_caption('To Do List')

        def Allinputed():
            if name.get() != "" and Author.get() != "" and Year.get() != 0 and ISBN.get() != 0:

                return True
            else:
                print("Please enter all fields")
                return False

        def Reset():
            name.set("")
            Author.set("")
            Year.set(0)
            ISBN.set(0)

        def getSelectedRow(event):
            global selectedValue
            index = list.curselection()[0]
            selectedValue = list.get(index)
            print(selectedValue)
            name.set(selectedValue[1])
            Author.set(selectedValue[2])
            Year.set(selectedValue[3])
            ISBN.set(selectedValue[4])

        def adding():
            list.delete(0, END)
            if Allinputed():
                print(name.get(), Author.get(), Year.get(), ISBN.get())
                db.addRec(name.get(), Author.get(), Year.get(), ISBN.get())
                list.insert(END, (name.get(), Author.get(), Year.get(), ISBN.get()))
                messagebox.showinfo("add", "Record added")
                Reset()

        def update():
            db.Update(selectedValue[0], name.get(), Author.get(), Year.get(), ISBN.get())
            list.delete(0, END)
            list.insert(END, (name.get(), Author.get(), Year.get(), ISBN.get()))
            messagebox.showinfo("Update", "Record Updated")

        def delete():
            # print(selectedValue[0],"\t",type(selectedValue[0]))
            db.Delete(selectedValue[0])
            veiwAll()
            Reset()
            messagebox.showinfo("Delete", "One Record Deleted")

        def search():
            list.delete(0, END)
            for data in db.SearchRecord(name.get(), Author.get(), Year.get(), ISBN.get()):
                list.insert(END, data)

        def veiwAll():
            list.delete(0, END)
            table, index = db.veiwAll()
            for data in table:
                list.insert(END, data)
            Reset()
            Indexes.set(str("Number of books:" + str(index)))

        title = Label(window, text="My Book Store", font=("arial black", 28, "bold", "underline"), fg="green")
        title.place(x=80, y=10)

        textFont = ("arial", 14)

        lbl = Label(window, text="Book Name", font=textFont)
        lbl.place(x=74, y=75)

        name = StringVar()
        NameBox = Entry(window, textvariable=name)
        NameBox.place(x=250, y=75)

        lbl = Label(window, text="Author Name", font=textFont)
        lbl.place(x=74, y=125)

        Author = StringVar()
        AuthorBox = Entry(window, textvariable=Author)
        AuthorBox.place(x=250, y=125)

        lbl = Label(window, text="Year", font=textFont)
        lbl.place(x=74, y=175)

        Year = IntVar()
        YearBox = Entry(window, textvariable=Year)
        YearBox.place(x=250, y=175)

        lbl = Label(window, text="ISBN", font=textFont)
        lbl.place(x=74, y=225)

        ISBN = IntVar()
        ISBNBox = Entry(window, textvariable=ISBN)
        ISBNBox.place(x=250, y=225)

        btnExit = Button(window, text=X, command=exit, fg="red", font=("arial", 16, "bold"))
        btnExit.place(x=400, y=0)

        buttonFont = ("arial", 14, "bold")

        AddBtn = Button(window, text="Add", font=buttonFont, command=adding)
        AddBtn.place(y=275, x=25)

        UpDateBtn = Button(window, text="Update", font=buttonFont, command=update)
        UpDateBtn.place(y=275, x=85)

        DelBtn = Button(window, text="Delete", font=buttonFont, command=delete)
        DelBtn.place(y=275, x=175)

        SearBtn = Button(window, text="Search", font=buttonFont, command=search)
        SearBtn.place(y=275, x=255)

        ViewBtn = Button(window, text="View All", font=buttonFont, command=veiwAll)
        ViewBtn.place(y=275, x=345)

        list = Listbox(window, width=60)
        list.place(x=40, y=330)

        sb1 = Scrollbar(window)
        sb1.place(x=410, y=350)

        list.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list.yview)

        Indexes = StringVar()
        lbl = Label(window, text="", textvariable=Indexes, font=textFont)
        lbl.place(x=100, y=500)

        list.bind('<<ListboxSelect>>', getSelectedRow)

        window.mainloop()
