# Simple to do list application based on command-line.

tasks = []

def create_tasks():
    global in_task
    in_task = input("Enter the tasks separated by commas: ").split(',')
    
    global tasks    # we can use this global veriable in every function
    for i in in_task:
       tasks.append(i.strip())#string.strip(): Return a copy of the string with leading and trailing whitespace removed.
       
def show_tasks():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        for indx, task in enumerate(tasks, start=1):
            print(indx, task)
            
def delete_task():
    if len(tasks) == 0:
        print("No tasks to remove")
    else:
        show_tasks()  
        var = int(input("Enter task number which is done: "))
        if 1 <= var <= len(tasks):
            tasks.pop(var - 1)
            print("Task number ",var,"is removed.")
        else:
            print("Invalid task number.")

# Main Method
while True:
    print("MAIN MENU\n1.CREATE TASK\n2.SHOW TASK \n3.TASKS DONE\n0.EXIT")
    choice = int(input("Enter choice"))
    if choice == 1:
        create_tasks()
    elif choice == 2:
        show_tasks()
    elif choice == 3:
      delete_task()
    elif choice == 0:
     break
    else:
     print("Invalid choice !!")