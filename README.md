# Personal Expense Tracker

A simple command-line expense tracker built using Python. This project helps users record expenses, view saved records, calculate total spending, search by expense name, and delete expenses.

## Features

- Add new expenses with a name and cost.
- View all saved expenses.
- Calculate total expenses.
- Search expenses by name.
- Delete expenses by name.
- Save expense records permanently in a text file.
- Search names without case sensitivity.

## Technologies Used

- Python 3
- Variables and data types
- Loops and conditional statements
- Lists and strings
- String methods: `strip()`, `split()`, and `lower()`
- File handling: reading, appending, and rewriting files

## Project Structure

```text
python-expense-tracker/
├── main.py
├── expense.txt
└── README.md
```

- `main.py` contains the application code.
- `expense.txt` stores expense records.
- `README.md` provides project documentation.

## Requirements

- Python 3
- A code editor or terminal

No external libraries are required.

## How to Run

1. Download or clone this repository.
2. Open the project folder in your code editor.
3. Make sure `expense.txt` exists in the same folder as `main.py`.
4. Run the program:

```bash
python main.py
```

On some systems, use `python3 main.py` instead.

## Example Data

The expense file stores records in this format:

```text
Food-100
Travel-200
Books-150
```

The total for these three expenses is 450.

## Current Limitations

- Expense costs must be entered as integers.
- The expense file must exist before reading or deleting records.
- Expense names should not contain hyphens (`-`).
- Deleting a name removes all records with that matching name.
- The program searches by expense name, not by a separate category.
- Invalid numeric input is not yet handled.

## Future Improvements

- Add expense categories and dates.
- Validate user input.
- Handle missing files automatically.
- Allow deletion of a single transaction.
- Add monthly expense summaries.
- Develop a graphical or web interface.

## Learning Outcomes

This project helped me practise:

- Building a menu-driven Python application.
- Reading, appending, and rewriting files.
- Processing text using string methods.
- Using loops and conditions to manage records.
- Debugging and improving program logic.

## Author

Created as a personal Python learning project.
