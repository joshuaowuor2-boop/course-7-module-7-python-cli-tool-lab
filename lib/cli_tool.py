# cli_tool.py

import argparse
from lib.models import Task, User

# Global dictionary to store users and their tasks
users = {}


def add_task(args):
    """Add a task with the given title to a user, creating the user if needed."""
    user = users.get(args.user)
    if user is None:
        user = User(args.user)
        users[args.user] = user
    task = Task(args.title)
    user.add_task(task)


def complete_task(args):
    """Mark a user's task as complete, reporting if the user or task is missing."""
    user = users.get(args.user)
    if user is None:
        print("❌ User not found.")
        return

    task = user.get_task_by_title(args.title)
    if task is None:
        print("❌ Task not found.")
        return

    task.complete()


# CLI entry point
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for adding tasks
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user", help="Name of the user")
    add_parser.add_argument("title", help="Title of the task to add")
    add_parser.set_defaults(func=add_task)

    # Subparser for completing tasks
    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user", help="Name of the user")
    complete_parser.add_argument("title", help="Title of the task to complete")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
