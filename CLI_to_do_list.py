#Making a CLI to do list using Python. The user can add, remove, and view tasks in the to-do list.
# What it needs to do:
# 1. Add a task to the to-do list via CLI.
# 2. Remove a task from the to-do list via CLI.
# 3. View all tasks in the to-do list via CLI.
# 4. Edit a task in the to-do list via CLI.
# 5. Mark a task as completed in the to-do list via CLI.
# 6. Save the to-do list to a file via CLI.
# 7. Load the to-do list from a file via CLI.
# 8. Exit the to-do list via CLI.
# In the future I will add a GUI to the to-do list using Tkinter.
import json

tasks = []

def loading_task():
    
    load_task =[]
    try:
     with open("tasks.json", "r", encoding="utf-8") as file:
            load_task = json.load(file)
            print("JSON loaded succesfully")
            tasks.extend(load_task)
    except FileNotFoundError:
        print("File doesn't exist yet!")  
    print(f"Loaded List: {load_task}")
    
def save_task():
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file)    

def add_tasks(task):
    tasks.append(task)

def remove_tasks(task_no):
    index = task_no - 1
    removed = tasks.pop(index)

def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def edit_task(task_no, new_task):
    index = task_no -1
    tasks[index] = new_task

def save_txt():
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for i, task in enumerate(tasks, start=1):
            file.write(f"{i}. {task}\n")
    print("Tasks saved to tasks.txt successfully! 💾")        

def mark_complete(task_no):
    index = task_no -1
    current_task = tasks[index]
    if current_task.endswith('✅'):
        print("This task is already marked as completed! 🛑")
    else:
        tasks[index] = current_task + '✅'

def check_complete():

    complete=[task for  task in tasks if task.endswith('✅')]

    if not complete:
      print("No Task has been completed yet!!!")      

    with open("Completed_tasks.txt", "w", encoding="utf-8") as file:
        print("---Completed Tasks---")
        for i, task in enumerate(complete, start=1):
            print(f"{i}. {task}")
            file.write(f"{i}. {task}\n")
   

def mark_incomplete(task_no):
    index = task_no -1
    current_task = tasks[index]
    if current_task.endswith('✅'):
        tasks[index] = current_task.replace('✅', '').strip()
    else:
        print("Task is Already Incomplete")               
            
def check_incomplete():

    incomplete=[task for task in tasks if not task.endswith('✅')]
    if not incomplete:
       print("All tasks are complete 🫡")             
    with open("Incomplete_tasks.txt", "w", encoding="utf-8") as file:
        print("---Incomplete Tasks---")
        for i, task in enumerate(incomplete, start=1):
            print(f"{i}. {task}") 
            file.write(f"{i}. {task}\n")

def main():
    loading_task()

    while True:
        print("---CLI TO-DO List")
        print(f"{int(1)}. Add a task")
        print(f"{int(2)}. View Tasks")
        print(f"{int(3)}. Edit a task")
        print(f"{int(4)}. Remove a task")
        print(f"{int(5)}. Mark task complete")
        print(f"{int(6)}. Mark task Incomplete")
        print(f"{int(7)}. Check Completed Tasks")
        print(f"{int(8)}. Check Incomplete Tasks")
        print(f"{int(9)}. Save tasks to Text File")
        print(f"{int(10)}. Save and Exit")

        try:
            choice =int(input("What would you like to do?:"))
            if choice == 1:
                add_task = input("Input New Task:")
                add_tasks(add_task)
                print("Task Added Successfully 😁")
            

            elif choice == 2:
                view_tasks() 

            elif choice == 3:
                while True:
                    N= len(tasks)
                    try:
                        view_tasks()
                        num=int(input(f"Enter Task ID you would like to edit:"))
                        if 1 <= num <= N:
                            print(f"Current task is: {tasks[num-1]}")
                            task_input = input("Enter updated task:")
                            edit_task(num, task_input)
                            view_tasks()
                            break
                        else:
                            print(f"Error!: Number should be between 1 and {N}. Try Again")
                    except ValueError:
                        print("Error: Invalid input. Please enter a whole number.")  

            elif choice == 4:
                while True:
                    N= len(tasks)
                    try:
                        view_tasks()
                        task_id=int(input("Enter Task ID of task you would like to delete:"))
                        if 1<= task_id <= N :
                            remove_tasks(task_id)
                            print(f"Task Deleted Successfully 👍")
                            view_tasks()
                            break
                        else:
                            print(f"Error!!!🤬 ID should be in range [1 - {N}]")       
                    except ValueError:
                        print("Error!!! 🤬 Task ID should be an Integer" )  

            elif choice == 5:
                while True:
                    N= len(tasks)
                    try:
                        view_tasks()
                        task_id=int(input("Enter Task ID of task you would like to mark Complete ✅:"))
                        if 1<= task_id <= N :
                            mark_complete(task_id)
                            print(f"Task Marked Complete ✅")
                            view_tasks()
                            break
                        else:
                                print(f"Error!!!🤬 ID should be in range [1 - {N}]")       
                    except ValueError:
                        print("Error!!! 🤬 Task ID should be an Integer" )

            elif choice == 6:
                while True:
                    N= len(tasks)
                    try:
                        view_tasks()
                        task_id=int(input("Enter Task ID of task you would like to mark Incomplete :"))
                        if 1<= task_id <= N :
                            mark_incomplete(task_id)
                            print("Task Marked Incomplete")
                            view_tasks()
                            break
                        else:
                            print(f"Error!!!🤬 ID should be in range [1 - {N}]")
                    except ValueError:        
                        print("Error!!! 🤬 Task ID should be an Integer" )

            elif choice == 7:
                check_complete()

            elif choice == 8:
                check_incomplete()    

            elif choice == 9:
                save_txt()

            elif choice == 10:
                print("JSON file updated!!!")
                print("Goodbye 👋")  
                break

            else:
                print("Error!:Choice ID should be between 1 and 10. Try Again")  

        except ValueError:
                     print("Error: Invalid input. Please enter a whole number.") 
    save_task()
main()         
