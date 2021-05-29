import pygame
from tkinter import *
from tkinter import messagebox


# import databases as db

class ToDoList:
    def __init__(self):
        window = Tk()
        window.geometry("450x700")

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
                messagebox.showinfo("Task Add", "Task Added")
                Reset()

        def update():
            db.Update(selectedValue[0], name.get(), Author.get(), Year.get(), ISBN.get())
            list.delete(0, END)
            list.insert(END, (name.get(), Author.get(), Year.get(), ISBN.get()))
            messagebox.showinfo("Task Update", "Task Updated")

        def delete():
            # print(selectedValue[0],"\t",type(selectedValue[0]))
            db.Delete(selectedValue[0])
            veiwAll()
            Reset()
            messagebox.showinfo("Task Delete", "Task Deleted")

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
            Indexes.set(str("Number of tasks:" + str(index)))

        title = Label(window, text="Tasks to Complete", font=('Ink Free', 40, "bold", "underline"), fg="black")
        title.place(x=0, y=10)

        textFont = ('Ink Free', 16, "bold")
        buttonFont = ('Ink Free', 12, "bold")

        AddBtn = Button(window, text="Add", font=buttonFont, command=adding)
        AddBtn.place(y=650, x=25)

        UpDateBtn = Button(window, text="Update", font=buttonFont, command=update)
        UpDateBtn.place(y=650, x=85)

        DelBtn = Button(window, text="Delete", font=buttonFont, command=delete)
        DelBtn.place(y=650, x=175)

        SearBtn = Button(window, text="Search", font=buttonFont, command=search)
        SearBtn.place(y=650, x=255)

        ViewBtn = Button(window, text="View All", font=buttonFont, command=veiwAll)
        ViewBtn.place(y=650, x=345)

        list = Listbox(window, width=60)
        list.place(x=40, y=100)

        sb1 = Scrollbar(window)
        sb1.place(x=410, y=275)

        list.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list.yview)

        Indexes = StringVar()

        list.bind('<<ListboxSelect>>', getSelectedRow)

        window.mainloop()


"""
        lbl = Label(window, text="Task Name", font=textFont)
        lbl.place(x=75, y=75)

        name = StringVar()
        NameBox = Entry(window, textvariable=name)
        NameBox.place(x=250, y=75)

        lbl = Label(window, text="Category", font=textFont)
        lbl.place(x=75, y=125)

        Author = StringVar()
        AuthorBox = Entry(window, textvariable=Author)
        AuthorBox.place(x=250, y=125)

        lbl = Label(window, text="Start Task", font=textFont)
        lbl.place(x=150, y=175)

        boxFont = ('Ink Free', 10, "bold")

        lbl = Label(window, text="Start Year", font=boxFont)
        lbl.place(x=50, y=240)
        Year = IntVar()
        YearBox = Entry(window, textvariable=Year)
        YearBox.place(x=50, y=225)

        lbl = Label(window, text="Start Month", font=boxFont)
        lbl.place(x=250, y=240)
        Month = IntVar()
        MonthBox = Entry(window, textvariable=Month)
        MonthBox.place(x=250, y=225)

        lbl = Label(window, text="Start Hours", font=boxFont)
        lbl.place(x=50, y=290)
        Hours = IntVar()
        HoursBox = Entry(window, textvariable=Hours)
        HoursBox.place(x=50, y=275)

        lbl = Label(window, text="Start Mins", font=boxFont)
        lbl.place(x=250, y=290)
        Mins = IntVar()
        MinsBox = Entry(window, textvariable=Mins)
        MinsBox.place(x=250, y=275)

        lbl = Label(window, text="End Task", font=textFont)
        lbl.place(x=160, y=325)

        lbl = Label(window, text="End Year", font=boxFont)
        lbl.place(x=50, y=390)
        StartYear = IntVar()
        StartYearBox = Entry(window, textvariable=StartYear)
        StartYearBox.place(x=50, y=375)

        lbl = Label(window, text="End Month", font=boxFont)
        lbl.place(x=250, y=390)
        StartMonth = IntVar()
        StartMonthBox = Entry(window, textvariable=StartMonth)
        StartMonthBox.place(x=250, y=375)

        lbl = Label(window, text="End Hour", font=boxFont)
        lbl.place(x=50, y=440)
        StartHour = IntVar()
        StartHourBox = Entry(window, textvariable=StartHour)
        StartHourBox.place(x=50, y=425)

        lbl = Label(window, text="End Mins", font=boxFont)
        lbl.place(x=250, y=440)
        StartMins = IntVar()
        StartMinsBox = Entry(window, textvariable=StartMins)
        StartMinsBox.place(x=250, y=425)
"""
