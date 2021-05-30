import pygame
from tkinter import *
from tkinter import messagebox


import BackEnd.ToDoDatabase_I_O as db

class ToDoList:

    def __init__(self):
        window = Tk()
        window.geometry("450x700")
        global x,y
        x=450
        y=700
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
                #print(name.get(), Author.get(), Year.get(), ISBN.get())

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
        def editing():
            popUp()

        def popUp():
            panel = Tk()
            panel.geometry("450x700")
            panel['background'] = '#00998f'

            lbl = Label(panel, text="Name", font=textFont, fg="white", bg='#00998f')
            lbl.place(x=100, y=75)


            NameBox = Entry(panel, textvariable=Name, fg="white", bg='#00998f')
            NameBox.place(x=175, y=80)

            lbl = Label(panel, text="Deadline", font=textFont, fg="white", bg='#00998f')
            lbl.place(x=150, y=125)

            boxFont = ('Ink Free', 15, "bold")

            lbl = Label(panel, text="Year", font=boxFont, fg="white", bg='#00998f')
            lbl.place(x=60, y=175)


            YearBox = Entry(panel, textvariable=Year, fg="white", bg='#00998f', width=4)
            YearBox.place(x=65, y=155)

            lbl = Label(panel, text="Month", font=boxFont, fg="white", bg='#00998f')
            lbl.place(x=110, y=175)


            MonthBox = Entry(panel, textvariable=Month, fg="white", bg='#00998f', width=2)
            MonthBox.place(x=130, y=155)

            lbl = Label(panel, text="Day", font=boxFont, fg="white", bg='#00998f')
            lbl.place(x=195, y=175)


            DayBox = Entry(panel, textvariable=Day, fg="white", bg='#00998f', width=2)
            DayBox.place(x=195, y=155)

            lbl = Label(panel, text="Hours", font=boxFont, fg="white", bg='#00998f')
            lbl.place(x=260, y=175)


            HoursBox = Entry(panel, textvariable=Hours, fg="white", bg='#00998f', width=2)
            HoursBox.place(x=260, y=155)

            lbl = Label(panel, text="Minutes", font=boxFont, fg="white", bg='#00998f')
            lbl.place(x=325, y=175)


            MinsBox = Entry(panel, textvariable=Mins, fg="white", bg='#00998f', width=2)
            MinsBox.place(x=325, y=155)

            lbl = Label(panel, text="Predicted Hours", font=textFont, fg="white", bg='#00998f')
            lbl.place(x=50, y=225)


            NameBox = Entry(panel, textvariable=PredHours, fg="white", bg='#00998f')
            NameBox.place(x=250, y=230)

            AddBtn = Button(panel, text="Add", font=buttonFont, command=adding, fg="white", bg='#00998f')
            AddBtn.place(y=325, x=17)

            UpDateBtn = Button(panel, text="Update", font=buttonFont, command=update, fg="white", bg='#00998f')
            UpDateBtn.place(y=325, x=75)

            DelBtn = Button(panel, text="Delete", font=buttonFont, command=delete, fg="white", bg='#00998f')
            DelBtn.place(y=325, x=169)

            list = Listbox(panel, width=60, height=15)
            list.place(x=40, y=400)

            sb1 = Scrollbar(panel)
            sb1.place(x=410, y=450)

            list.configure(yscrollcommand=sb1.set)
            sb1.configure(command=list.yview)

        Name = StringVar()
        Year = IntVar()
        Month = IntVar()
        Day = IntVar()
        Hours = IntVar()
        Mins = IntVar()
        PredHours = IntVar()

        #(0,153,143)
        window['background']='#00998f'
        title = Label(window, text="Tasks to Complete", font=('Ink Free', 40, "bold", "underline"), fg="white",bg='#00998f')
        title.place(x=0, y=10)

        textFont = ('Ink Free', 16, "bold")
        buttonFont = ('Ink Free', 16, "bold")



        SearBtn = Button(window, text="Search", font=buttonFont, command=search, fg="white",bg='#00998f')
        SearBtn.place(y=550, x=300)

        ViewBtn = Button(window, text="View All", font=buttonFont, command=veiwAll, fg="white",bg='#00998f')
        ViewBtn.place(y=550, x=175)

        EditBtn = Button(window, text="Edit Task", font=buttonFont, command=editing, fg="white", bg='#00998f')
        EditBtn.place(y=550, x=50)

        list = Listbox(window, width=60,height=25)
        list.place(x=40, y=100)

        sb1 = Scrollbar(window)
        sb1.place(x=410, y=275)

        list.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list.yview)

        Indexes = StringVar()

        list.bind('<<ListboxSelect>>', getSelectedRow)

        window.mainloop()
