import sys
import json

DATA_FILE = "tasks.json"

def load_tasks():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f)

def add_task(desc):
    tasks = load_tasks()
    tasks.append({"desc": desc, "done": False})
    save_tasks(tasks)
    print("Task added.")

def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['desc']} - {'Done' if task['done'] else 'Pending'}")

def complete_task(idx):
    tasks = load_tasks()
    tasks[idx-1]["done"] = True
    # Bug: not saving after marking as done!
    print("Task marked complete.")

def delete_task(idx):
    tasks = load_tasks()
    tasks.pop(idx-1)  # Bug: may crash on bad index!
    save_tasks(tasks)
    print("Task deleted.")

def main():
    if len(sys.argv) < 2:
        print("Missing command: add/list/complete/delete")
        return
    cmd = sys.argv[1]
    if cmd == "add":
        add_task(sys.argv[2])
    elif cmd == "list":
        list_tasks()
    elif cmd == "complete":
        complete_task(int(sys.argv[2]))
    elif cmd == "delete":
        delete_task(int(sys.argv[2]))
    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()
