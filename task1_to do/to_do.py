import json


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


tasks = load_tasks()


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    task = input("Enter your task: ")

    if tasks:
        new_id = max(task["id"] for task in tasks) + 1
    else:
        new_id = 1

    new_task = {
        "id": new_id,
        "task": task
    }

    tasks.append(new_task)
    save_tasks()

    print(f"Task '{task}' added successfully.")


def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Your tasks:")

        for task in tasks:
            print(f'{task["id"]}. {task["task"]}')


def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            print("Exiting the to-do list application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()