# Task 1 — To-Do List

A console-based To-Do List application developed as **Project 1** of the **DecodeLabs Industrial Training Kit — Python Programming Internship (Batch 2026)**.

##  Internship Task

Project 1 is the initial logic and data-management phase of the DecodeLabs Python Programming track. The objective is to build a program that allows users to **add tasks to a list and view the stored tasks**.

The project focuses on understanding how multiple items can be stored in a single variable and introduces the fundamental data-management concepts used in larger applications and databases.

According to the assigned task, the key Python skill is working with **Lists, `append()`, and loops**.

##  Objectives

The main objectives of this project are to:

- Store multiple tasks using a Python list
- Add new tasks using `append()`
- Display stored tasks using loops
- Take user input through a console interface
- Organize the application using functions
- Understand the Input → Process → Output (IPO) model
- Implement persistent storage using JSON
- Structure individual tasks as dictionaries
- Assign a unique ID to each task

##  Technologies & Concepts Used

- **Python 3**
- Python Lists
- Python Dictionaries
- Functions
- `if/elif/else` statements
- `while` loops
- `for` loops
- `enumerate()`
- User Input / Output
- File Handling
- JSON Serialization & Deserialization
- Exception Handling
- Modular Program Structure

##  Data Structure

The application uses a **list containing dictionaries**.

The list stores the complete collection of tasks, while each dictionary represents an individual task.

Example:


tasks = [
    {
        "id": 1,
        "task": "Complete Python assignment"
    },
    {
        "id": 2,
        "task": "Study JSON"
    }
]

## Data Persistence

The application uses JSON serialization to persist task data between program sessions.

When the application starts, existing data is loaded from the JSON file. Whenever a new task is added, the updated task collection is written back to the file.

## How to Run
Python 3.13 must be installed on the system.
Open the project directory in Visual Studio Code and run:
python to_do.py

## Project Status
Completed — Project 1

## Internship Information

Program: DecodeLabs Industrial Training Kit
Track: Python Programming
Batch: 2026
Project: Task 1 — To-Do List Application

## Author
Zainab Rashid

