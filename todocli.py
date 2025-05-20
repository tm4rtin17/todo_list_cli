import pyinputplus as pyip
import datetime

class Task:
    def __init__(self, description: str,priority: str, duedate: datetime, done: bool):
        self.description = description
        self.priority = priority
        self.duedate = duedate
        self.done = False

tasks = []

def add():
    description = pyip.inputStr('Task Description: ')
    priority = pyip.inputInt('Assign Priority:\n[1] High\n[2] Medium\n[3] Low\n')
    duedate = pyip.inputDate('Assign a due date:\n')
    done = False
    if priority == 1:
        priority = 'High'
    elif priority == 2:
        priority = 'Medium'
    elif priority == 3:
        priority = 'Low'
    task = Task(description, priority, duedate, done)
    tasks.append(task)
    print(f'Added Task: {description}; Priority: {priority}, Due Date: {duedate}\n')

def view_tasks():
    global tasks
    if not tasks:
        print('\nNo tasks to view.\n')
    else:
        print('\n Tasks:')
        for index, task in enumerate(tasks, start=1):
            print(f'{index}. {task.description}; Priority: {task.priority}; Due Date: {task.duedate}; Done: {task.done}')

def mark_done():
    view_tasks()
    choice = pyip.inputInt('Which task would you like to mark as done?') - 1
    tasks[choice].done=True

while True:
    view_tasks()
    choice = pyip.inputInt('''\nWould you like to:
    [1] Add a Task
    [2] Mark a Task as Done
    [3] Exit Program\n''', min=1, max=3)

    if choice == 1:
        add()
    elif choice == 2:
        mark_done()
    elif choice == 3:
        exit()