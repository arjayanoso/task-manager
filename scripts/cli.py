import argparse
from . import tasks, database

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Add task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("title", help="Title of the task")
    parser_add.add_argument("-d", "--description", default="", help="Description of the task")
    parser_add.add_argument("--due", default=None, help="Due date of the task")

    # List tasks
    subparsers.add_parser("list", help="List all tasks")

    # Mark task as done
    parser_done = subparsers.add_parser("done", help="Mark a task as done")
    parser_done.add_argument("id", type=int, help="ID of the task to mark as done")

    # Delete task
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task to delete")

    args = parser.parse_args()

    # Ensure the database is initialized
    conn = database.get_connection()
    database.initialize_db(conn)
    conn.close()

    if args.command == "add":
        task_id = tasks.add_task(args.title, args.description, args.due)
        print(f"Task added with ID: {task_id}")
    elif args.command == "list":
        tasks_list = tasks.list_tasks()
        if tasks_list:
            print(f"{'ID':<5}{'Title':<30}{'Done':<5}")
            print("-" * 40)
            for task in tasks_list:
                status = "Yes" if task["done"] else "No"
                print(f"{task['id']:<5}{task['title']:<30}{status:<5}")
        else:
            print("No tasks found.")
    elif args.command == "done":
        updated = tasks.mark_task_done(args.id)
        if updated:
            print(f"Task {args.id} marked as done.")
        else:
            print(f"Task {args.id} not found.")
    elif args.command == "delete":
        deleted = tasks.delete_task(args.id)
        if deleted:
            print(f"Task {args.id} deleted.")
        else:
            print(f"Task {args.id} not found.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
