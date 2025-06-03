import task
import pyinputplus as pyip
from datetime import datetime as dt
import json
import os
from rich import print
from rich.table import Table
from rich.console import console


def load_tasks():
    #check if file exists, if not create an empty tasks.json
    file_path = 'tasks.json'
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump([], file)
        return []
    
    try:
        with open('tasks.json', 'r') as file:
            data = json.load(file)
            #convert json objects to task objects
            tasks = [
                task.Task(
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
    with open('tasks.json', 'w') as file:
        json.dump(data, file, indent=4)

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
    task = task.Task(description, priority, duedate, done)
    tasks.append(task)
    save_tasks(tasks)
    print(f'Added Task: {description}; Priority: {priority}, Due Date: {str(duedate)}\n')

def view_tasks():
    global tasks, table
    if not tasks:
        print('\nNo tasks to view.\n')
    else:
        print('\n Tasks:')
        for index, task in enumerate(tasks, start=1):
            print(f'[{index}] {task.description}; Priority: {task.priority}; Due Date: {task.duedate}; Done: {task.done}')
            console.print(table)

def mark_done():
    view_tasks()
    choice = pyip.inputInt('Which task would you like to mark as done?\n') - 1
    tasks[choice].done=True
    save_tasks(tasks)

