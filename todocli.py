import pyinputplus as pyip
import datetime
from datetime import datetime as dt
import json
import os

class Task:
    def __init__(self, description: str,priority: str, duedate: datetime, done: bool):
        self.description = description
        self.priority = priority
        self.duedate = duedate
        self.done = done

with open('/home/pi/Coding_Projects/To-Do-List-CLI/tasks.json', 'r') as file:
    tasks = json.load(file)

def load_tasks():
    #check if file exists, if not create an empty tasks.json
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as file:
            json.dump([], file)
        return []
    
    try:
        with open('tasks.json', 'r') as file:
            data = json.load(file)
            #convert json objects to task objects
            tasks = [
                Task(
                    description=task["description"],
                    priority=task["priority"],
                    duedate=dt.strptime(task["duedate"], "%Y-%m-%d").date(),
                    done=task["done"]
                )
                for task in data
            ]
            return tasks
    except (json.JSONDecodeError, KeyError):
        #return empty list if file is invalid or empty
        return []

def save_tasks(tasks):
    # Convert Task objects to JSON-serializable format
    data = [
        {
            "description": task.description,
            "priority": task.priority,
            "duedate": task.duedate.strftime("%Y-%m-%d"),
            "done": task.done
        }
        for task in tasks
    ]
    with open('/home/pi/Coding_Projects/To-Do-List-CLI/tasks.json', 'w') as file:
        json.dump(data, file, indent=4)

# Load tasks at the start
tasks = load_tasks()

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
    save_tasks(tasks)
    print(f'Added Task: {description}; Priority: {priority}, Due Date: {duedate}\n')

def view_tasks():
    global tasks
    if not tasks:
        print('\nNo tasks to view.\n')
    else:
        print('\n Tasks:')
        for index, task in enumerate(tasks, start=1):
            print(f'[{index}] {task.description}; Priority: {task.priority}; Due Date: {task.duedate}; Done: {task.done}')

def mark_done():
    view_tasks()
    choice = pyip.inputInt('Which task would you like to mark as done?\n') - 1
    tasks[choice].done=True
    save_tasks(tasks)

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