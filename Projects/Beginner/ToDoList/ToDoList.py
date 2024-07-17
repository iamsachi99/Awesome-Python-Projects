tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Deleted task: {removed_task}")
    else:
        print("Invalid task number.")

def main():
    print("To-Do List Application")

    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter choice(1/2/3/4): ")

        if choice == '1':
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
