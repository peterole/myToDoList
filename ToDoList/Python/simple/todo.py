
# Add a task

tasks_dictionary = {

}

def add_tasks():

    task_desc = input("Description: ")
    task_priority = input("Priority: ")

    task_id = len(tasks_dictionary) + 1

    tasks_dictionary[task_id] = {
        'task': task_desc,
        'completed': False,
        'priority': task_priority
    }

    print(f"{task_desc} has been added with ID {task_id}")

# View a task

def view_task():
    pass

# Remove a task

def remove_task():
    pass

# Edit status of a task

def edit_status_task():
    pass

# Exit program

def exit_program():
    pass

# End