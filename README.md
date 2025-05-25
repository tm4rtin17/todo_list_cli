# Todo CLI V2.0.0

A command-line application built with Python for managing tasks. It supports task creation with priorities and due dates, marking tasks as completed, and persistent storage using a JSON file.

---

## Features

- **Persistent Storage**: Tasks are saved to and loaded from a `tasks.json` file.
- **View Tasks**: Display task descriptions, priorities, due dates, and completion status.
- **Add Tasks**: Enter a description, assign a priority (High, Medium, Low), and set a due date.
- **Mark as Done**: Update a task’s status to "Done."
- **Interactive Menu**: Navigate with a numbered menu (input validation via `pyinputplus`).
- **Error Handling**: Creates an empty file or returns an empty list if `tasks.json` is missing or invalid.
- **Due Date Support**: Store due dates in `YYYY-MM-DD` format.

---

## Requirements

- Python 3.6+
- `pyinputplus` library

---

## Installation

Clone the repository (replace `your-username` with your GitHub username):

```bash
git clone https://github.com/your-username/todo-cli.git
cd todo-cli
```

Install the required package:

```bash
pip install pyinputplus
```

Ensure the directory `/home/pi/Coding_Projects/To-Do-List-CLI/` exists, or modify the file path in the code to a writable location.

Run the tool:

```bash
python todocli.py
```

---

## Usage

Upon running the script, a menu is displayed. Tasks are automatically loaded from `/home/pi/Coding_Projects/To-Do-List-CLI/tasks.json` (or created if missing).

### Add a Task

1. Select option `[1]`
2. Enter a task description
3. Choose a priority: `[1] High`, `[2] Medium`, `[3] Low`
4. Enter a due date in `MM/DD/YYYY` format

### Mark a Task as Done

1. Select option `[2]`
2. View the numbered list of tasks
3. Enter the number of the task to mark as done

### Exit the Program

- Select option `[3]`

---

## Example Session

```
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
```

---

## Task Storage

Tasks are stored in `/home/pi/Coding_Projects/To-Do-List-CLI/tasks.json` with this structure:

```json
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
```

- If the file doesn’t exist, it’s created as an empty array (`[]`).
- Tasks are saved automatically after changes.

---

## Notes

- **File Path**: Default is `/home/pi/Coding_Projects/To-Do-List-CLI/tasks.json`. Ensure it exists and is writable, or change the path.
- **Error Handling**: Automatically creates a new file and handles invalid JSON safely.
- **Due Date Format**: Stored in `YYYY-MM-DD`, entered as `MM/DD/YYYY`.

---

## Planned Features

- Task removal
- Task categories
- Sorting and filtering by priority or due date
- Reminders for upcoming due dates
- Editing existing tasks

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository  
2. Create a new branch:

```bash
git checkout -b feature/your-feature-name
```

3. Commit your changes:

```bash
git commit -m "Add your message here"
```

4. Push to GitHub and open a Pull Request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- Built with Python and the `pyinputplus` library for robust input validation.
- Persistent storage implemented using JSON for simplicity and portability.
