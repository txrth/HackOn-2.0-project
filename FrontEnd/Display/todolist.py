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

        #(0,153,143)
        window['background']='#00998f'
        title = Label(window, text="Tasks to Complete", font=('Ink Free', 40, "bold", "underline"), fg="white",bg='#00998f')
        title.place(x=0, y=10)

        textFont = ('Ink Free', 16, "bold")
        buttonFont = ('Ink Free', 16, "bold")

        AddBtn = Button(window, text="Add", font=buttonFont, command=adding, fg="white",bg='#00998f')
        AddBtn.place(y=550, x=17)

        UpDateBtn = Button(window, text="Update", font=buttonFont, command=update, fg="white",bg='#00998f')
        UpDateBtn.place(y=550, x=75)

        DelBtn = Button(window, text="Delete", font=buttonFont, command=delete, fg="white",bg='#00998f')
        DelBtn.place(y=550, x=169)

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
