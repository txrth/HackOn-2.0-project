import sqlite3
import datetime


class ToDoDatabase_I_O:
    def getConnection(self):
        global conn
        global cur
        conn = sqlite3.connect("ToDoDataBase.db")
        cur = conn.cursor()

    def addTask(self, name, category, predictedHours, deadline, partnum=1, Tpart=1,start=None, end=None,done= 0):
        self.getConnection()
        cur.execute("insert into tasks values(null, ?,?,?, ?,?,?, ?,?,?)", (name, category,predictedHours,deadline,start,
                                                                          end,partnum,Tpart,done))
        taskId = cur.lastrowid
        conn.commit()
        cur.execute("insert into log values(null, ?, ?, ?)", (str("Event " + name + " part: " + str(partnum) + " of " +
                                                    str(Tpart)+" has been added to task"), datetime.datetime.now(),taskId ))
        conn.commit()
        conn.close()

    def removeTask(self,id):
        self.getConnection()
        cur.execute("select * from tasks where id =?",(id,))
        data = cur.fetchall()
        conn.commit()
        cur.execute("delete from tasks where id =?",(id,))
        conn.commit()
        cur.execute("insert into log values(null, ?, ?, ?)", (str("Event" + str(data[0][1])  + " part: " + str(data[0][7]) + " of " +
                                                                 str(data[0][8]) + " has been added to task"),
                                                            datetime.datetime.now(), id))
        conn.commit()
        conn.close()
# create function to remove setup queSystems for Tasks and logs
    def getA_Task(self,id):
        self.getConnection()
        cur.execute("select * from tasks where id =?", (id,))
        raw = cur.fetchall()
        data=[]
        for element in raw[0]:
            data.append(element)
        conn.commit()
        conn.close()
        return data

    def updateTask (self,id, name="", category="", predictedHours=0, deadline="", partnum=1, Tpart=1,start=None, end=None,done= 0 ):

        data = self.getA_Task(id)
        print(data)
        if (name!=""):
            data[1]=name
        if (category!=""):
            data[2]=category
        if (predictedHours!=0):
            data[3]=predictedHours
        if (deadline!=""):
            data[4]=deadline
        if (partnum!=1):
            data[5]=partnum
        if (Tpart!=1):
            data[6]=Tpart
        if(start!=None):
            data[7]=start
        if (end!=None):
            data[8]=end
        if(done!=0):
            data[9]=done

        self.getConnection()
        cur.execute("update tasks set name=?, category=?, predictedHours=?, deadline=?, partnum=?, Tparts=?,start=?"
                    ", end=?,done=?  where id=?", (name,category,predictedHours,deadline,partnum,Tpart,start,end,done,id))
        cur.execute("insert into log values(null, ?, ?, ?)",(str("taks id "+ str(id)+ " was updated"),datetime.datetime.now(),id))
        conn.commit()
        conn.close()

    def searchRecord (self, name="", category="", partnum="", Tpart="",done= "" ):
        self.getConnection()
        cur.execute("select * from tasks where name =? or category=? or partnum=? or Tparts=? or done=?",(name,category,partnum,Tpart,done))
        data = cur.fetchall()
        return data

# "tasks"," name text NOT NULL, category text NOT NULL, predictedHours Interger,deadline timestamp, start timestamp,
    # end timestamp,partNum Integer, Tparts Interger, done Interger"

# "log","actionDone text, time timestamp,task_id Interger"

    def test (self):
        self.getConnection()
        try:
            cur.execute('drop table tasks')
            cur.execute('drop table log')
        except:
            pass
        else:
            pass
        finally:
            self.createTable("tasks"," name text NOT NULL, category text NOT NULL, predictedHours Interger, "
                            "deadline timestamp, start timestamp, end timestamp,partNum Integer, Tparts Interger, done Interger")
            self.createTable("log","actionDone text, time timestamp,task_id Interger, Foreign Key(task_id) references tasks (id)")

    def createTable(self, name, parameters ):
        self.getConnection()
        cur.execute(str("create table if not exists " + name +"  (id integer PRIMARY KEY, " + parameters +" )"))
        conn.commit()
        conn.close()

    def printTable(self):
        self.getConnection()
        cur.execute("Select * from tasks")
        data = cur.fetchall()
        print("from tasks table:\n",data)
        print("\n")
        cur.execute("Select * from log")
        data = cur.fetchall()
        print("from log table:\n", data )
        conn.close()

    def getlog (self):
        self.getConnection()
        cur.execute("Select * from log")
        raw = cur.fetchall()
        data= []
        for row in raw:
            #time_str = row[2]
            #format_string = "%Y-%m-%d %H:%M:%S.%f"
            #date = datetime.datetime.strptime(time_str,format_string)
            line =[row[1],row[2],row[3]]
            data.append(line)
        return data

    def getTasks (self):
        self.getConnection()
        cur.execute("Select * from tasks")
        raw = cur.fetchall()
        data= []
        for row in raw:
            line = []
            for element in row:
                line.append(element)
            data.append(line)
        return data

    def __init__(self):
        pass
        """
        self.test()
        self.addTask("hello", "work", 2,datetime.datetime(2021,5,28,7,12),1,1)
        self.addTask("hw", "work", 4, datetime.datetime(2021, 5, 29, 9, 13), 1, 1)
        self.printTable()
        print("\n")

        self.getTasks()
        self.updateTask(1,name="HOMEWORK")
        self.printTable()
        self.searchRecord(name="hello")
"""

