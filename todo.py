import sys
import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(desc):
    if not desc.strip():
        print("Error: Task description cannot be empty.")
        return
    tasks = load_tasks()
    tasks.append({"desc": desc, "done": False})
    save_tasks(tasks)
    print("Task added.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = '✅' if task['done'] else '❌'
        print(f"{i}. {task['desc']} - {status}")

def complete_task(idx):
    tasks = load_tasks()
    if idx < 1 or idx > len(tasks):
        print("Error: Invalid task number.")
        return
    tasks[idx-1]["done"] = True
    save_tasks(tasks)
    print("Task marked complete.")

def delete_task(idx):
    tasks = load_tasks()
    if idx < 1 or idx > len(tasks):
        print("Error: Invalid task number.")
        return
    tasks.pop(idx-1)
    save_tasks(tasks)
    print("Task deleted.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 todo.py [add/list/complete/delete] [arguments]")
        return
    cmd = sys.argv[1]
    if cmd == "add":
        if len(sys.argv) >= 3:
            add_task(sys.argv[2])
        else:
            print("Error: Provide a task description.")
    elif cmd == "list":
        list_tasks()
    elif cmd == "complete":
        if len(sys.argv) >= 3 and sys.argv[2].isdigit():
            complete_task(int(sys.argv[2]))
        else:
            print("Error: Provide a valid task number.")
    elif cmd == "delete":
        if len(sys.argv) >= 3 and sys.argv[2].isdigit():
            delete_task(int(sys.argv[2]))
        else:
            print("Error: Provide a valid task number.")
    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()

#updated
