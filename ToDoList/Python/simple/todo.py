import datetime
import json
import os

TASK_FILE = "tasks.json"

if os.path.exists(TASK_FILE):
    print("File does exist!")
    pass
else:
    print("File does NOT exist!")
    file = open(TASK_FILE, "w")
    file.close()

# Add a task
task_id = 0

def add_tasks(task_id):

    # task ID

    task_id += 1

    # task description

    task_description = input("Description: ")

    # task status

    task_status = False

    if task_status == False:
        status = "Incomplete!"

    else:
        status = "Complete!"


    # task created at

    created_at = datetime.now()

    # task updated at

    updated_at = created_at

    # task populating

    task_list = [("ID: " + task_id), ("Decrription: " + task_description), 
            ("Status: " + task_status), ("Created At: " + created_at), 
            ("Updated At" + updated_at)]

    file = open(TASK_FILE, "a")
    for task in task_list:
        file.write(task_list[task])
    file.write("\n")
    file.close()

# View a task

def update_task():
    pass

# Remove a task

def remove_task():
    pass

# Edit status of a task

def list_tasks_all():
    pass

def list_completed_tasks():
    pass

def list_incomplete_tasks():
    pass

def exit_program():
    pass

program_menu = ["1: Add Task", "2: Update Task", "3: Delete Task", 
                "4: List All Tasks", "5: List All Completed Tasks",
                "6: List All Non-Completed Tasks", "7: Exit Program"]

for item in range(len(program_menu)):
    print(program_menu[item])
    item +=1

menu_input = int(input("Menu Selection: "))

if menu_input == 1:
    add_tasks()

elif menu_input == 2:
    update_task()

elif menu_input == 3:
    remove_task()

elif menu_input == 4:
    list_tasks_all()

elif menu_input == 5:
    list_completed_tasks()

elif menu_input == 6:
    list_incomplete_tasks()

elif
# End