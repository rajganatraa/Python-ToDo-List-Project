from tkinter import *
from tkinter import messagebox
from tkinter import *
from tkcalendar import Calendar

import mysql.connector
from mysql.connector import Error
mydb= mysql.connector.connect(host="localhost",user="raj",passwd="raj37500",database="db1")

def newTask():
    task = my_entry.get()
    count=my_entry2.get()
    status=my_entry3.get()
    if task != "":
        taskId=count
        insertuser(mydb,taskId,task,status)
        viewtable()
        my_entry.delete(0,END)
        my_entry2.delete(0,END)
        my_entry3.delete(0,END)
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def insertuser(mydb,taskid,task,status):
    query="insert into todolist values({},'{}','{}')".format(taskid,task,status)
    cursor=mydb.cursor()
    cursor.execute(query)
    mydb.commit()

def deleteTask():
   delid=int(my_entry2.get())
   query="DELETE FROM todolist WHERE id={}".format(int(delid))
   cursor = mydb.cursor()
   cursor.execute(query)
   mydb.commit()
   viewtable()
   my_entry.delete(0, END)
   my_entry2.delete(0, END)
   my_entry3.delete(0, END)

def updatetask():
    id=my_entry2.get()
    change=my_entry.get()
    stat=my_entry3.get()
    query="UPDATE todolist set task='{}',status='{}' where id={}".format(change,stat,id)
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()
    viewtable()
    my_entry.delete(0, END)
    my_entry2.delete(0, END)
    my_entry3.delete(0, END)
def select_date():
    root = Tk()

    # Set geometry
    root.geometry("400x400")

    # Add Calendar
    cal = Calendar(root, selectmode='day',
                   year=2020, month=5,
                   day=22)

    cal.pack(pady=20)

    def grad_date():
        date.config(text="Selected Date is: " + cal.get_date())

    # Add Button and Label
    Button(root, text="Get Date",
           command=grad_date).pack(pady=20)

    date = Label(root, text="")
    date.pack(pady=20)

    # Execute Tkinter
    root.mainloop()

ws = Tk()
ws.geometry('500x780+500+200')
ws.title('Python Mini Project')
ws.config(bg='#223441')
Label(ws, text="Please enter unique task id for each task",
      font=('TkheadingFont, 14')).pack(pady="10")
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=30,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
def delete():
   lb.delete(0,END)

lb.pack(side=LEFT, fill=BOTH)
def viewtable():
    delete()
    cursor = mydb.cursor()
    query="select * from todolist order by id"
    cursor.execute(query)
    for item in cursor:
        lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)
my_entry = Entry(
    ws,
    font=('times', 24)
)
my_entry2 = Entry(
    ws,
    font=('times', 24)
)
my_entry3 = Entry(
    ws,
    font=('times', 24)
)
Label(ws, text="Enter task here...!",
      font=('TkheadingFont, 14')).pack()
my_entry.pack(pady=15)
Label(ws, text="Enter taskID here...!",
      font=('TkheadingFont, 14')).pack()
my_entry2.pack(pady=15)
Label(ws, text="Enter task Status here...!",
      font=('TkheadingFont, 14')).pack()
my_entry3.pack(pady=15)

button_frame = Frame(ws)
button_frame.pack(pady=20)


addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)

addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)
updateTask_btn = Button(
    button_frame,
    text='UPDATE Task',
    font=('times 13'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=updatetask
)
updateTask_btn.pack(fill=BOTH, expand=FALSE, side=RIGHT)

Label(ws, text="To delete the task enter only the task id and click delete task!",
      font=('TkheadingFont, 10')).pack(pady="10")
Label(ws, text="To UPDATE the task enter the task id and updated task in task column and ",
      font=('TkheadingFont, 10')).pack(pady="10")
Label(ws, text="status in status column and click UPDATE Task to update it",
      font=('TkheadingFont, 10')).pack(pady="0")
viewtable()
ws.mainloop()
