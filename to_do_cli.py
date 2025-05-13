import pyinputplus as pyip

todo = []

def main_menu():
    while True:
        choice = pyip.inputInt('''Would you like to:
        [1] View current to-do list
        [2] Add item to list                           
        [3] Remove an item
        [4] Exit Program''', min=1, max=4)

        if choice == 1: 
            view_list()
        elif choice == 2:
            add_list()
        elif choice == 3:
            remove_item()
        elif choice == 4:
            print('---Exiting Program---')
            break

def view_list():
    if len(todo) >= 1:
        for i, task in enumerate(todo, start=1):
            print(f'[{i}] {task}')
    else:
        print('Your list is empty!')

def add_list():
    while True:
        item = pyip.inputStr('What would you like to add to your to-do list?')
        todo.append(item)
        more_option = pyip.inputYesNo('Add more? (y/n)')
        if more_option == 'no':
            break
        
def remove_item():
    if len(todo) > 1:
        while True:
            print('Which item would you like to clear from the list?')
            view_list()
            rmv_item = pyip.inputInt()
            todo.pop(rmv_item - 1)
            more_option = pyip.inputYesNo('Remove more? (y/n)')
            if more_option == 'no':
                break
    else:
        print("You can't remove items from an empty list!\n")

main_menu()