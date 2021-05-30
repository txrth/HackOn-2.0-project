import pygame
from tkinter import *
from tkinter import messagebox


import BackEnd.ToDoDatabase_I_O as db

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
            popUp()
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
            db.test()
            db.printTable()
            #table = db.getTasks()
            #for data in table:
             #   list.insert(END, data)
            #Reset()

        def popUp():
            panel = Tk()
            panel.geometry("450x700")
            lbl = Label(panel, text="Task Changes", font=textFont)
            lbl.place(x=75, y=75)

            name = StringVar()
            NameBox = Entry(panel, textvariable=name)
            NameBox.place(x=250, y=75)

            lbl = Label(panel, text="Category", font=textFont)
            lbl.place(x=75, y=125)

            Author = StringVar()
            AuthorBox = Entry(panel, textvariable=Author)
            AuthorBox.place(x=250, y=125)

            lbl = Label(panel, text="Start Task", font=textFont)
            lbl.place(x=150, y=175)

            boxFont = ('Ink Free', 10, "bold")

            lbl = Label(panel, text="Start Year", font=boxFont)
            lbl.place(x=50, y=240)
            Year = IntVar()
            YearBox = Entry(panel, textvariable=Year)
            YearBox.place(x=50, y=225)

            lbl = Label(panel, text="Start Month", font=boxFont)
            lbl.place(x=250, y=240)
            Month = IntVar()
            MonthBox = Entry(panel, textvariable=Month)
            MonthBox.place(x=250, y=225)

            lbl = Label(panel, text="Start Hours", font=boxFont)
            lbl.place(x=50, y=290)
            Hours = IntVar()
            HoursBox = Entry(panel, textvariable=Hours)
            HoursBox.place(x=50, y=275)

            lbl = Label(panel, text="Start Mins", font=boxFont)
            lbl.place(x=250, y=290)
            Mins = IntVar()
            MinsBox = Entry(panel, textvariable=Mins)
            MinsBox.place(x=250, y=275)

            lbl = Label(panel, text="End Task", font=textFont)
            lbl.place(x=160, y=325)

            lbl = Label(panel, text="End Year", font=boxFont)
            lbl.place(x=50, y=390)
            StartYear = IntVar()
            StartYearBox = Entry(panel, textvariable=StartYear)
            StartYearBox.place(x=50, y=375)

            lbl = Label(panel, text="End Month", font=boxFont)
            lbl.place(x=250, y=390)
            StartMonth = IntVar()
            StartMonthBox = Entry(panel, textvariable=StartMonth)
            StartMonthBox.place(x=250, y=375)

            lbl = Label(panel, text="End Hour", font=boxFont)
            lbl.place(x=50, y=440)
            StartHour = IntVar()
            StartHourBox = Entry(panel, textvariable=StartHour)
            StartHourBox.place(x=50, y=425)

            lbl = Label(panel, text="End Mins", font=boxFont)
            lbl.place(x=250, y=440)
            StartMins = IntVar()
            StartMinsBox = Entry(window, textvariable=StartMins)
            StartMinsBox.place(x=250, y=425)

            AddBtn = Button(window, text="Add", font=buttonFont, command=adding, fg="white", bg='#00998f')
            AddBtn.place(y=550, x=17)

            UpDateBtn = Button(window, text="Update", font=buttonFont, command=update, fg="white", bg='#00998f')
            UpDateBtn.place(y=550, x=75)

            DelBtn = Button(window, text="Delete", font=buttonFont, command=delete, fg="white", bg='#00998f')
            DelBtn.place(y=550, x=169)


        #(0,153,143)
        window['background']='#00998f'
        title = Label(window, text="Tasks to Complete", font=('Ink Free', 40, "bold", "underline"), fg="white",bg='#00998f')
        title.place(x=0, y=10)

        textFont = ('Ink Free', 16, "bold")
        buttonFont = ('Ink Free', 16, "bold")



        SearBtn = Button(window, text="Search", font=buttonFont, command=search, fg="white",bg='#00998f')
        SearBtn.place(y=550, x=255)

        ViewBtn = Button(window, text="View All", font=buttonFont, command=veiwAll, fg="white",bg='#00998f')
        ViewBtn.place(y=550, x=345)

        list = Listbox(window, width=60,height=25)
        list.place(x=40, y=100)

        sb1 = Scrollbar(window)
        sb1.place(x=410, y=275)

        list.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list.yview)

        Indexes = StringVar()

        list.bind('<<ListboxSelect>>', getSelectedRow)

        window.mainloop()
