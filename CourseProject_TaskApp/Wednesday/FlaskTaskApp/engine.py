import sqlite3 
import json


class newTask(object):
    """new Task class with methods to add deadline, priority, status and notes; and to store it in our DB"""

    def __init__(self, task, userID):
        self.task = task
        self.userID = userID
        
    def addDeadline(self):
        deadline = input("What's the deadline? ")
        self.deadline = deadline
        return self.deadline
    
    def addPriority(self):
        priority = input("What's the priority? 1-high, 2-low. ")
        if priority == "1":
            self.priority = "High"
        elif priority== "2":
            self.priority ="Low"
        return self.priority

    def addStatus(self):
        status = input("What's the status? 1 - To do, 2 - In progress, 3 - Done. ")
        if status == "1":
            self.status = "To do"
        elif status == "2":
            self.status = "In progress"
        elif status == "3":
            self.status = "Done"
        return self.status
    
    def addNote(self):
        note = input("Add a note: ")
        self.note = note
        return self.note 

    def taskSummary(self): 
        """adds record to the table based on user input """    
        conn = sqlite3.connect('TaskApp.db') 
        c = conn.cursor()
        c.execute('INSERT INTO tasks(userID, task, date, priority, status, description) VALUES (?,?,?,?,?,?)', (self.userID, self.task, self.deadline, self.priority, self.status, self.note))
        conn.commit()
        c.close()
        conn.close()


#####GENERATING TASKS

def anotherTask(addAnotherTask):
    """ function that triggers creation of new tasks"""
    # This will loop for as long as the user keeps answering Y when asked if they want to add wnother task
    # If the answer is Y, calls typeTask() to ask for user input (task name stored as 'task') 
    # calls addTask(task) to crete an object, call all it's methods and save input to the database """
    
#    addAnotherTask="Y"
#    while addAnotherTask == "Y":  
    task = typeTask()
    addTask(task)        
      #  addAnotherTask = input("Add another task? Y or N. ")
#    else:
#        pass

def typeTask():
    """ gets user input for task name only """
    task = input("What's the task? ")
    return task 
        
def addTask(task):
    """ creates a new objects and calls methods as listed. taskSummary() stores all inputs as a record in the database """
    userID = "abc123" #will need to change it once we have login. it's set to abc123 for now 
    Task1 = newTask(task, userID)
    Task1.addDeadline()
    Task1.addPriority()
    Task1.addStatus()
    Task1.addNote()
    Task1.taskSummary()
        

def resultsDictionary():
    """ gets all the recods from the tasks table in TaskApp.db, converts them into a dictionary - results."""
    # task id is the key, task name, deadline, priority, status and note are in the value tuple
    ## example- { 4: ('feed the dog', 'asap', 'High', 'To do', 'dry food') ...}
    
    results = {} 
    conn = sqlite3.connect('TaskApp.db') 
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    resultsDb =  c.fetchall() 
    for row in resultsDb : 
        key = row[1]
        value = row [2:]
        results [key] = (value)
    print(results)
    c.close()
    conn.close()

def deleteTask(taskId):
    """ identifies task in the tasks table by task id and deletes it form the table"""
    
    """ !!! we need to get taskId from frontend?!!!"""
    
    conn = sqlite3.connect('TaskApp.db') 
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE taskId = ?', (taskId) )    
    conn.commit()
    c.close()
    conn.close()