# Todo CLI (V1.2.0)

This is a simple command-line application built with Python that helps you manage your tasks. It includes support for priorities and lets you track completion status.

## Features

- **View Tasks:** Display your current to-do list with priorities and completion status.
- **Add Tasks:** Input a task description and assign a priority level (High, Medium, Low).
- **Mark as Done:** Update a task to indicate it’s been completed.
- **Interactive Menu:** Navigate using a numbered menu system.
- **Input Validation:** Powered by `pyinputplus` to ensure valid entries.

## Requirements

- Python 3.6+
- `pyinputplus` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/todo-cli.git
   cd todo-cli
   ```

2. Install the required package:

   ```bash
   pip install pyinputplus
   ```

3. Run the tool:

   ```bash
   python todocli.py
   ```

## Usage

Once the script runs, you'll be presented with a menu.

### Add a Task

- Choose option [1]
- Provide a task description
- Assign a priority: [1] High, [2] Medium, [3] Low

### Mark a Task as Done

- Choose option [2]
- View the list of tasks
- Select the number corresponding to the task you want to mark as done

### Exit the Program

- Choose option [3]

## Example Session

```
1. Buy groceries; Priority: Medium; Done: False
2. Call mom; Priority: High; Done: False

Would you like to:
[1] Add a Task
[2] Mark a Task as Done
[3] Exit Program
> 2

Which task would you like to mark as done?
> 2

1. Buy groceries; Priority: Medium; Done: False
2. Call mom; Priority: High; Done: True
```

## Planned Features

- Persistent storage (save and load tasks from a file)
- Task removal
- Task categories
- Due dates and reminders
- Enhanced filtering and sorting

## Contributing

Contributions are welcome! If you have a feature idea or want to fix a bug:

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

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- Built using Python and the `pyinputplus` library for reliable input handling.
