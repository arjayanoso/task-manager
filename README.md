# Task Manager

A simple command-line task manager application built with Python and SQLite.

## Features
- Add new tasks
- List existing tasks
- Mark tasks as completed
- Delete tasks

## Requirements
- Python 3.6+

## Setup

1. Clone the repository.
2. (Optional) Create and activate a virtual environment.
3. Install requirements:
   ```bash
   pip install -r requirements.txt

## Running the Application

Run the CLI:
```
python -m task_manager.cli add "My Task" --description "A sample task" --due "2025-12-31"
python -m task_manager.cli list
python -m task_manager.cli done 1
python -m task_manager.cli delete 1

