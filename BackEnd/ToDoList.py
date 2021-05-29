import ToDoQue.ToDoDatabase_I_O as db

class ToDoList:

    def firstTimeRun (self):
        db.getConnection()



    def __init__(self):
         global data
         data = db.ToDoDatabase_I_O()

testing = ToDoList()
testing