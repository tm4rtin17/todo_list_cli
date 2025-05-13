# todo_list_cli
Todo List CLI Tool
Welcome to the Todo List CLI Tool! This is a simple, lightweight command-line application built with Python to help you manage your tasks efficiently. Whether you're jotting down daily chores or planning your next big project, this tool keeps your tasks organized with a user-friendly interface.
The tool is actively maintained, with plans to add exciting new features over time! Contributions are welcome, so feel free to dive in and make it your own.
Features

View Tasks: Display your current to-do list with numbered items for easy reference.
Add Items: Quickly add new tasks to your list, with the option to add multiple items in one go.
Remove Items: Clear completed tasks or unwanted items with a simple selection process.
Interactive Menu: Navigate through a clean, numbered menu to perform actions.
Input Validation: Powered by pyinputplus to ensure valid inputs every time.
Lightweight & Portable: No complex dependencies—just Python and a single library!

Installation
Get started in just a few steps! Follow these instructions to set up the Todo List CLI Tool on your machine.
Prerequisites

Python 3.6 or higher
pyinputplus library

Steps

Clone the Repository:
git clone https://github.com/your-username/todo-list-cli.git
cd todo-list-cli


Install Dependencies:Install the required pyinputplus library using pip:
pip install pyinputplus


Run the Tool:Launch the CLI by running the main script:
python todo.py



Usage
Once you run the script, you'll be greeted with an interactive menu. Here's how to use it:

View To-Do List:

Select option [1] to see all tasks.
If the list is empty, you'll get a friendly reminder to add some tasks!


Add a Task:

Choose option [2].
Enter a task description and decide if you want to add more tasks in the same session.


Remove a Task:

Pick option [3].
View the list, enter the number of the task to remove, and choose whether to remove more.


Exit:

Select option [4] to gracefully exit the program.



Example Session
Would you like to:
[1] View current to-do list
[2] Add item to list
[3] Remove an item
[4] Exit Program
2
What would you like to add to your to-do list? Buy groceries
Add more? (y/n) y
What would you like to add to your to-do list? Call mom
Add more? (y/n) n
Would you like to:
[1] View current to-do list
[2] Add item to list
[3] Remove an item
[4] Exit Program
1
[1] Buy groceries
[2] Call mom

Planned Features
This tool is just getting started! Here are some features on the horizon:

Task Categories: Group tasks by work, personal, or custom categories.
Due Dates: Add deadlines to keep track of time-sensitive tasks.
Task Prioritization: Mark tasks as high, medium, or low priority.
Persistent Storage: Save tasks to a file for cross-session use.
Have suggestions? Let me know what you think!

Contributing
We love contributions! Want to add a feature, fix a bug, or improve the code? Here's how to get involved:

Fork the repository
Create a new branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add some amazing feature')
Push to your branch (git push origin feature/amazing-feature)
Open a Pull Request

Please ensure your code follows the existing style and includes clear comments. Check out the Issues page for ideas or to report bugs.
License
This project three project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgements

Built with love using pyinputplus for robust input handling.
Inspired by the need to stay organized in a busy world!


Happy task managing! If you enjoy this tool, give it a star on GitHub and share it with friends. Let's make productivity fun!

