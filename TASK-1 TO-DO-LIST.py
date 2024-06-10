from tkinter import *
import random

root = Tk()
root.title('Neeraj_task-1')
root.geometry("350x250")
root.configure(bg="gray")

tasks = []

#FUNCTIONS

def update_listbox():
    clear_listbox()

    for task in tasks:
        lb_tasks.insert("end",task)

def clear_listbox():
    lb_tasks.delete(0,"end")

def add_task():
    task = txt_input.get()

    if task !='':
        tasks.append(task)
        update_listbox()

    else:
        display['text'] = "Please enter a task"
    txt_input.delete(0,'end')

def delete():
    task = lb_tasks.get('active')
    if task in tasks:
        tasks.remove(task)

    update_listbox()
    display['text'] = "task deleted"

def delete_all():
    global tasks
    tasks = []
    update_listbox()

def choose_random():
    task = random.choice(tasks)
    display['text'] = "task"

def number_of_task():
    number_of_tasks = len(tasks)

    msg = "number of tasks : %s" %number_of_tasks
    display['text'] = msg

def exit():
    quit()

title = Label(root,text="TO DO LIST",bg="lightyellow",width=20)
title.grid(row=0,column=0)

display = Label(root,text="",bg="white")
display.grid(row=0,column=1)

txt_input = Entry(root, width=30)
txt_input.grid(row=1,column=1)

btn_add_task = Button(root, text = "Add Task", fg = 'black', bg = None, command = add_task,width=20,relief=RAISED)
btn_add_task.grid(row=1,column=0)

btn_delete = Button(root, text = "Delete", fg = 'black', bg = None, command = delete,width=20,relief=RAISED)
btn_delete.grid(row=2,column=0)

btn_delete_all = Button(root, text = "Delete All", fg = 'black', bg = None, command = delete_all,width=20,relief=RAISED)
btn_delete_all.grid(row=3,column=0)

btn_choose_random = Button(root, text = "Choose Random", fg = 'black', bg = None, command = choose_random,width=20,relief=RAISED)
btn_choose_random.grid(row=4,column=0)


btn_number_of_task = Button(root, text = "Number of Tasks", fg = 'black', bg = None, command = number_of_task,width=20,relief=RAISED)
btn_number_of_task.grid(row=5,column=0)


btn_close = Button(root, text = "Exit", fg = 'black', bg = None, command = exit,width=20,relief=RAISED)
btn_close.grid(row=6,column=0)

lb_tasks = Listbox(root)
lb_tasks.grid(row=2,column=1,rowspan=7)

root.mainloop()
