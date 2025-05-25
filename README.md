Todo CLI V2.0.0
This is a command-line application built with Python for managing tasks. It supports task creation with priorities and due dates, marking tasks as completed, and persistent storage using a JSON file.
Features

Persistent Storage: Tasks are saved to and loaded from a tasks.json file, ensuring data persists between sessions.
View Tasks: Display the current to-do list with task descriptions, priorities, due dates, and completion status.
Add Tasks: Input a task description, assign a priority (High, Medium, Low), and set a due date.
Mark as Done: Update a task’s completion status to "Done."
Interactive Menu: Navigate using a numbered menu with input validation via pyinputplus.
Error Handling: Gracefully handles missing or invalid tasks.json files by creating an empty file or returning an empty task list.
Due Date Support: Assign and store due dates for tasks in YYYY-MM-DD format.

Requirements

Python 3.6+
pyinputplus library

Installation

Clone the repository (replace your-username with your GitHub username):
git clone https://github.com/your-username/todo-cli.git
cd todo-cli


Install the required package:
pip install pyinputplus


Ensure the directory /home/pi/Coding_Projects/To-Do-List-CLI/ exists or modify the file path in the code to a writable location.

Run the tool:
python todocli.py



Usage
Upon running the script, a menu is displayed. Tasks are automatically loaded from /home/pi/Coding_Projects/To-Do-List-CLI/tasks.json (or created as an empty file if it doesn’t exist).
Add a Task

Select option [1]
Enter a task description
Choose a priority: [1] High, [2] Medium, [3] Low
Specify a due date (format: MM/DD/YYYY)

Mark a Task as Done

Select option [2]
View the numbered list of tasks
Enter the number of the task to mark as done

Exit the Program

Select option [3]

Example Session
Tasks:
[1] Buy groceries; Priority: Medium; Due Date: 2025-10-05; Done: False
[2] Call mom; Priority: High; Due Date: 2025-06-01; Done: False

Would you like to:
[1] Add a Task
[2] Mark a Task as Done
[3] Exit Program
> 2

Which task would you like to mark as done?
> 2

Tasks:
[1] Buy groceries; Priority: Medium; Due Date: 2025-10-05; Done: False
[2] Call mom; Priority: High; Due Date: 2025-06-01; Done: True

Task Storage
Tasks are stored in /home/pi/Coding_Projects/To-Do-List-CLI/tasks.json with the following structure:
[
    {
        "description": "Buy groceries",
        "priority": "Medium",
        "duedate": "2025-10-05",
        "done": false
    },
    {
        "description": "Call mom",
        "priority": "High",
        "duedate": "2025-06-01",
        "done": true
    }
]


If the file doesn’t exist, it is created with an empty array ([]).
Tasks are saved automatically after adding or marking as done.

Notes

File Path: The default file path is /home/pi/Coding_Projects/To-Do-List-CLI/tasks.json. Ensure this directory exists and is writable, or modify the path in the code.
Error Handling: The program creates an empty tasks.json if it’s missing and handles invalid JSON gracefully.
Due Date Format: Due dates are stored in YYYY-MM-DD format in the JSON file but entered as MM/DD/YYYY during input.

Planned Features

Task removal
Task categories
Sorting and filtering by priority or due date
Reminders for upcoming due dates
Support for editing existing tasks

Contributing
Contributions are welcome! To contribute:

Fork the repository
Create a new branch:git checkout -b feature/your-feature-name


Commit your changes:git commit -m "Add your message here"


Push to GitHub and open a Pull Request

License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgements

Built using Python and the pyinputplus library for robust input validation.
Persistent storage implemented with JSON for simplicity and portability.

