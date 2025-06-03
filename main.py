from .console import console
import func
import pyinputplus as pyip

#Load tasks at the start
tasks = func.load_tasks()

while True:
    func.view_tasks()
    choice = pyip.inputInt('''\nWould you like to:
    [1] Add a Task
    [2] Mark a Task as Done
    [3] Exit Program\n''', min=1, max=3)

    if choice == 1:
        func.add()
    elif choice == 2:
        func.mark_done()
    elif choice == 3:
        exit()