import json
import os

# File to save tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, title, description):
    task_id = str(len(tasks) + 1)
    tasks[task_id] = {
        "title": title,
        "description": description,
        "status": "Pending"
    }
    print("Task added with ID:", task_id)

def update_task(tasks, task_id, title=None, description=None, status=None):
    if task_id in tasks:
        if title:
            tasks[task_id]["title"] = title
        if description:
            tasks[task_id]["description"] = description
        if status:
            tasks[task_id]["status"] = status
        print("Task ",task_id," updated.")
    else:
        print("Task ID ", task_id," not found.")

def delete_task(tasks, task_id):
    if task_id in tasks:
        del tasks[task_id]
        print("Task ", task_id," deleted.")
    else:
        print("Task ID ", task_id," not found.")

def list_tasks(tasks):
    if tasks:
        for task_id, details in tasks.items():
            print(f"ID: {task_id}\nTitle: {details['title']}\nDescription: {details['description']}\nStatus: {details['status']}\n")
    else:
        print("No tasks found.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(tasks, title, description)
            save_tasks(tasks)
        elif choice == '2':
            task_id = input("Enter task ID to update: ")
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            status = input("Enter new status (Pending/Completed, leave blank to keep current): ")
            update_task(tasks, task_id, title if title else None, description if description else None, status if status else None)
            save_tasks(tasks)
        elif choice == '3':
            task_id = input("Enter task ID to delete: ")
            delete_task(tasks, task_id)
            save_tasks(tasks)
        elif choice == '4':
            list_tasks(tasks)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
