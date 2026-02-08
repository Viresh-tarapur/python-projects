def To_do():
    print("Welcome to To-Do List ")

    task = []
    task_list = int(input("Enter how many tasks you want to add in the task list: "))
    for i in range(1, task_list + 1):
        task_add = input(f" Enter Task {i}: ")
        task.append(task_add)
    print(f"Today's tasks are: {task}")

    while True:
        operation = int(input("\nEnter \n 1 = Add \n 2 = Update \n 3 = Delete \n 4 = View \n 5 = Exit\nChoice: "))
        
        if operation == 1:
            new = input("Enter the new task: ")
            task.append(new)
            print(f"Task added! Current tasks: {task}")

        elif operation == 2:
            old_task = input("Enter the task you want to update: ")
            if old_task in task:
                new_task = input("Enter the new task: ")
                ind = task.index(old_task)
                task[ind] = new_task
                print(f"Task updated! Current tasks: {task}")
            else:
                print("Task not found")

        elif operation == 3:
            delete = input("Enter the task you want to remove: ")
            if delete in task:
                task.remove(delete)
                print(f"Task removed! Current tasks: {task}")
            else:
                print("Task not found")

        elif operation == 4:
            print("\nCurrent To-Do List:")
            if task:
                for i, t in enumerate(task, start=1):
                    print(f"{i}. {t}")
            else:
                print("No tasks available.")

        elif operation == 5:
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid Input....")

To_do()

