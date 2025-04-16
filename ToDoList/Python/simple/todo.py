import datetime
import json
import os

TASK_FILE = "tasks.txt"

if os.path.exists(TASK_FILE):
    print("File does exist!")
    pass
else:
    print("File does NOT exist!")
    file = open(TASK_FILE, "w")
    file.close()

# Add a task


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

    created_at = datetime.datetime.now()

    # task updated at

    updated_at = created_at

    # task populating

    task_list = [("ID: " + str(task_id)), ("Description: " + task_description), 
            ("Status: " + status), ("Created At: " + str(created_at)), 
            ("Updated At: " + str(updated_at))]

    file = open(TASK_FILE, "a")
    i = 0
    for task in task_list:
        file.write(task_list[i] + "\n")
        i += 1
    file.writelines("\n")
    file.close()

    main()

# View a task

def update_task():
    pass

# Remove a task

def remove_task():
    pass

# List tasks

def list_tasks_all():
    pass

def list_completed_tasks():
    pass

def list_incomplete_tasks():
    pass

def main():

    program_menu = ["1: Add Task", "2: Update Task", "3: Delete Task", 
                    "4: List All Tasks", "5: List All Completed Tasks",
                    "6: List All Non-Completed Tasks", "7: Exit Program"]

    for item in range(len(program_menu)):
        print(program_menu[item])
        item +=1

    menu_input = int(input("Menu Selection: "))

    task_id = 0

    if menu_input == 1:
        add_tasks(task_id)

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

    elif menu_input == 7:
        exit


main()
# End