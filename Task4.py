#                                                Task 4
# Rock-Paper-Scissors Game

import json
import os
from datetime import datetime

class Task:
    def __init__(self, description, deadline=None, completed=False):
        self.description = description
        self.deadline = deadline
        self.completed = completed

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        deadline_info = f", Deadline: {self.deadline}" if self.deadline else ""
        return f"{self.description} - {status}{deadline_info}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print("Task marked as completed!")
        else:
            print("Invalid task index!")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted successfully!")
        else:
            print("Invalid task index!")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks):
                print(f"{index+1}. {task}")

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)
        print("Tasks saved to file successfully!")

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)
            self.tasks = [Task(task['description'], task['deadline'], task['completed']) for task in data]
            print("Tasks loaded from file successfully!")
        else:
            print("File does not exist. No tasks loaded.")

def main():
    print("Welcome to Sophisticated To-Do List Application!")
    todo_list = TodoList()
    filename = "todo_list.json"

    # Load tasks from file if the file exists
    todo_list.load_from_file(filename)

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. Display Tasks")
        print("5. Save Tasks to File")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            task_description = input("Enter task description: ")
            deadline_input = input("Enter deadline (optional, format: YYYY-MM-DD): ")
            deadline = datetime.strptime(deadline_input, '%Y-%m-%d') if deadline_input else None
            todo_list.add_task(Task(task_description, deadline))
        elif choice == '2':
            index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == '3':
            index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            todo_list.save_to_file(filename)
        elif choice == '6':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
