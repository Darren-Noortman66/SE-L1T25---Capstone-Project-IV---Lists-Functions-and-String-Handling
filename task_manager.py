# --------------------------------------------IMPORTS----------------------------------------------------------#


# Importing the date module from within the datetime class to work with dates later in the application.
from datetime import date

# Importing the datetime module from within the datetime class to work with dates later in the application.
from _datetime import datetime


# --------------------------------------- FUNCTIONS ------------------------------------------------ #


def reg_user():
    # Defining a function named 'reg_user' that will register a new user to the 'users.txt' text-file when called.

    if username == "admin":  # Using an if, else-statement to ensure that only the admin can Register new users.

        # Requesting the new username to be written to the 'users' text-file and casting it to lower-case.
        new_username = str.lower(input("\n\nInsert New Username:\t"))

        # Creating a boolean named 'duplicate' that is set to False.
        # This boolean will be used to determine whether or not the new username already exists
        duplicate = False

        # Opening the 'user.txt' file as 'users' in read-mode using the 'open' function.
        with open('user.txt', 'r') as users:

            for user in users:  # Creating a for-loop to run through each user in the 'users' file.

                # If the 'new_username' variable inserted by the user is found in the file,
                # then the 'duplicate' value will be set to True and the loop will break.
                if new_username in user:
                    duplicate = True
                    break

        # Creating a while-loop to ensure that there are not any duplicates written to the 'user.txt' file.
        # While the 'duplicate' value is True, then the loop will continue to run.
        while duplicate:

            print("There is already a user with this username.\n"  # Printing an error message.
                  "Please choose a different username.\n\n")

            # Requesting the 'new_username' variable to be compared and possibly stored.
            new_username = str.lower(input("\n\nInsert New Username:\t"))

            # Opening the 'user.txt' file as 'users' in read-mode using the 'open' function.
            with open('user.txt', 'r') as users:
                data = users.read()  # Reading from the 'user.txt' file and storing it in a variable called 'data'.

                # If the 'new_username' value is not found in the 'data' variable, then the while loop is broken.
                # Otherwise it will continue to run.
                if new_username in data:
                    duplicate = True
                else:
                    break

        # Requesting the new password to be written to the 'users' text-file.
        new_password = input("\nInsert New Password:\t")

        # Requesting the new password confirmation to make sure the user puts in the password they want.
        confirm_password = input("\nConfirm Your Password:\t")

        # Creating a while-loop to repeatedly ask the user to input their new password and confirmation password.
        # This is only looped if the new_password and confirmation_password do not match up.
        while new_password != confirm_password:
            print("\n\nPlease ensure that your New-Password and your Confirmed-Password are the same.")
            new_password = input("Insert New Password:\t")
            confirm_password = input("Confirm Your Password:\t")
            if new_password == confirm_password:
                break  # Breaking the while-loop once the new_password and confirmation_password match.

        # Opening the 'user.txt' file as 'users' in append-mode using the 'open' function.
        with open('user.txt', 'a') as users:

            # Writing the new username and password to the text-file.
            users.write("\n" + new_username.lower() + ", " + new_password)

        print("\n\nUser Successfully Added")  # Printing successful message

    else:

        # Printing a error statement telling the user that only the 'admin' can register new users.
        # This will only run if the admin is not the current user.

        print("\nOnly the user 'admin' is allowed to register new users.")

    menu()  # Calling the 'menu' function again to await the user's next input.


def add_task():
    # Defining a function named 'add_task' that will add a new task to the 'tasks.txt' file when called.

    # Requesting the name of the user that the task is assigned to.
    task_user = str(input("\n\nInsert the Username of the Person the Task is Assigned to:\t"))

    # Requesting the title of the task.
    task_title = str(input("\nInsert the Title of the Task:\t"))

    # Requesting the description of the task.
    task_desc = str(input("\nInsert the Description of the Task:\t"))

    # Requesting when the task due-date is in a specific format.
    task_due = input("\nInsert the Due-Date for the Task in the format dd mmm yyyy :\t")

    # Creating a variable for when the task was given to the user by using the date module.
    task_given = date.today()  # Using the 'today' function to determine what day it is today.
    task_given = task_given.strftime('%d %b %Y')  # Changing the format of 'task_given' by using the 'strftime' function

    task_complete = "No"  # Creating a variable named 'task_complete' and assigning the value "No" to it.

    # Opening the 'tasks.txt' file as 'tasks' in append-mode using the 'open' function.
    with open('tasks.txt', 'a') as tasks:

        # Writing out all the inserted information into the 'tasks' text-file in the correct format.
        tasks.write("\n" + task_user.lower() + ", " + task_title + ", " + task_desc + ", "
                    + str(task_given) + ", " + task_due + ", " + task_complete)

    print("\n\nTask Successfully Added")  # Printing successful message

    menu()  # Calling the 'menu' function again to await the user's next input.


def view_all():
    # Defining a function named 'view_all' that will view all the tasks in
    # the 'tasks.txt' file in an easy-to-read format.

    # Opening the 'tasks.txt' file as 'tasks' in read-mode using the 'open' function.
    with open('tasks.txt', 'r') as tasks:

        # Using a for-loop to print out each line in the 'tasks' text-file'.
        for task in tasks:

            # Using the split function to determine each different piece of information in the line.
            details = task.split(", ")

            # Printing out the results
            print(f"\nUsername:\t\t{details[0]}\n"
                  f"Task Title:\t\t{details[1]}\n"
                  f"Task Description:\t{details[2]}\n"
                  f"Date Assigned Task:\t{details[3]}\n"
                  f"Date Due:\t\t{details[4]}\n"
                  f"Task Complete:\t\t{details[5]}\n")

    menu()  # Calling the 'menu' function again to await the user's next input.


def view_mine():
    # Defining a function named 'view_mine' that will display the task info for the user currently logged-in.
    # This function will also allow some of the details of a task to be changed.

    # Creating an empty list called 'index_details' that will be used to store each task related to
    # the user currently logged-in. This list will also assist with indexing.
    index_details = []

    count = 0  # Creating a 'count' variable and setting it to 0. This will be used for indexing of the user's tasks.

    # -------- INITIAL TASK DISPLAY ---------- #

    # Opening the 'tasks.txt' file as 'tasks' in read-mode using the 'open' function.
    with open('tasks.txt', 'r') as tasks:

        # Using a for-loop to run through each task in the 'tasks.txt' file in order to
        # find the tasks related to the user currently logged-in.
        for task in tasks:

            # Using an if-statement to determine which tasks belong the user currently logged-in.
            if username in task:

                index_details.append(task)  # Appending task to the 'index_details' list once username is found.

                # Incrementing the 'count' variable everytime the the user is found so that each
                # task belonging to the user is numbered for editing.
                count += 1

                # Splitting the details of the tasks by the ', ' in order to print each detail in
                # an easy-to-read format. This list is called 'details'.
                details = task.split(', ')

                # Printing out the results
                print(f"\n{count}.\t"
                      f"Username:\t\t{details[0]}\n\t"
                      f"Task Title:\t\t{details[1]}\n\t"
                      f"Task Description:\t{details[2]}\n\t"
                      f"Date Assigned Task:\t{details[3]}\n\t"
                      f"Date Due:\t\t{details[4]}\n\t"
                      f"Task Complete:\t\t{details[5]}\n\t")

    # ----------- EDIT-LOOP ----------- #

    # Creating a boolean variable named 'loop' that is set to True. This boolean will be used to
    # determine whether or not the user is done working with/ viewing their task information.
    loop = True

    # Requesting an integer input from the user to determine which task they wish to edit.
    task_choice = int(input("\nInsert the number of the task you want to edit.\n"
                            "-1 to return to the menu.\n\n"))

    # If the user inserts the value -1, then the value of 'loop' will be set to False and
    # the following while-loop will not be executed.
    if task_choice == -1:
        loop = False

    # Creating a while-loop to allow the user to edit/ view info about their tasks until they are finished.
    while loop:

        # Creating a new variable named 'task_choice' that is equal to the value inserted by the user,
        # then subtracted by 1. This is because list start at the index of 0 so choice number 3 is actually index 2.
        task_choice = task_choice - 1

        # Creating a variable called 'chosen_task' based off the 'index_details' list and the 'task_choice' index.
        chosen_task = index_details[task_choice]

        # Requesting an integer from the user in order to determine what they would like to do with their currently
        # selected task, or if they would like to return to the menu.
        option_choice = int(input("\n\nWould you like to:\n"
                                  "1. Mark the Task as Complete\n"
                                  "2. Edit the Task\n"
                                  "-1. Return the menu\n\n"))

        # Using if, elif-statements to determine what will happen based on the input given by the user.
        # If the 'option_choice' value is equal to 1, then currently selected task will be marked as complete.
        if option_choice == 1:

            # Opening the 'tasks.txt' file as 'tasks' in read-mode using the 'open' function.
            with open('tasks.txt', 'r') as tasks:

                # Reading each line in the 'tasks.txt' file and storing it in a list called 'data'.
                data = tasks.readlines()

                # Using a for-loop and enumerate function to determine the position/ index of the chosen task.
                # Once the chosen task is found, then that line of text is replaced by an edited version of
                # the same text in order to state that the task is complete.
                for index, item in enumerate(data):
                    if chosen_task in item:
                        details = chosen_task.split(', ')
                        details[5] = 'Yes'
                        details_text = ", ".join(details)
                        data[index] = details_text

            # Opening the 'tasks.txt' file as 'tasks' in write-mode using the 'open' function.
            with open("tasks.txt", "w") as tasks:

                # Replacing the information in the 'tasks.txt' file with the same data,
                # except the specifically chosen task is now marked as complete.
                tasks.write('\n'.join(str(line.strip('\n')) for line in data))

        # If the 'option_choice' value is equal to 2, then user will be asked what they would like to edit.
        elif option_choice == 2:

            task_complete = True  # Creating a boolean named 'task_complete' with the value True

            # Using an if-statement to determine whether or not the task has been completed. If it has,
            # then the 'task_complete' variable will be set to False and the user will not be able to edit the task.
            if "Yes" in chosen_task:
                task_complete = False

            # If the 'task_complete' variable is True, then the user will be able to edit the task,
            # otherwise an error message will be printed.
            if task_complete:

                # Requesting an integer input from the user to determine what detail of
                # their task they would like to edit.
                user_date = int(input("Select which option you would like to edit by "
                                      "inserting the corresponding number:\n"
                                      "1. Username of person assigned to task\n"
                                      "2. Due-Date for Task\n\n"))

                # Using an if, elif-statement to determine what code should be executed.
                # If the user inserts number 1, then the user will be asked to insert the new username of the
                # person assigned to the task.
                if user_date == 1:

                    # Requesting the name of the new user assigned to task.
                    new_user = str.lower(input("Insert new username of person assigned to task:\t"))

                    # Opening the 'tasks.txt' file as 'tasks' in read-mode using the 'open' function.
                    with open('tasks.txt', 'r') as tasks:

                        # Reading each line in the 'tasks.txt' file and storing it in a list called 'data'.
                        data = tasks.readlines()

                        # Using a for-loop and enumerate function to determine the position/ index of the chosen task.
                        # Once the chosen task is found, then that line of text is replaced by an edited version of
                        # the same text in order to change the user assigned to the task.
                        for index, item in enumerate(data):
                            if chosen_task in item:
                                details = chosen_task.split(', ')
                                details[0] = new_user
                                details_text = ", ".join(details)
                                data[index] = details_text

                    # Opening the 'tasks.txt' file as 'tasks' in write-mode using the 'open' function.
                    with open("tasks.txt", "w") as tasks:

                        # Replacing the information in the 'tasks.txt' file with the same data,
                        # except the specifically chosen task is changed to a different user.
                        tasks.write('\n'.join(str(line.strip('\n')) for line in data))

                # If 'user_date' equals 2, then the user will be asked to insert the new due-date for the chosen task.
                elif user_date == 2:

                    # Requesting the new due-date for the chosen task
                    new_date = input("\nInsert the Due-Date for the Task in the format dd mmm yyyy :\t")

                    # Opening the 'tasks.txt' file as 'tasks' in read-mode using the 'open' function.
                    with open('tasks.txt', 'r') as tasks:
                        # Reading each line in the 'tasks.txt' file and storing it in a list called 'data'.
                        data = tasks.readlines()

                    # Using a for-loop and enumerate function to determine the position/ index of the chosen task.
                    # Once the chosen task is found, then that line of text is replaced by an edited version of
                    # the same text in order to change the due-date for the task.
                    for index, item in enumerate(data):
                        if chosen_task in item:
                            details = chosen_task.split(', ')
                            details[4] = new_date
                            details_text = ", ".join(details)
                            data[index] = details_text

                    # Opening the 'tasks.txt' file as 'tasks' in write-mode using the 'open' function.
                    with open("tasks.txt", "w") as tasks:

                        # Replacing the information in the 'tasks.txt' file with the same data,
                        # except the specifically chosen task now has a different due-date.
                        tasks.write('\n'.join(str(line.strip('\n')) for line in data))

            else:

                # Printing an error message stating that the task task cannot be edited if it is completed.
                print("\n\nOnly tasks that have NOT been completed can be edited.\n\n")

        # If the user inserts the value -1, then the value of 'loop' will be set to False and
        # the while-loop will not be executed again and will be broken out of.
        elif option_choice == -1:
            break

        # Requesting an integer input from the user to determine which task they wish to edit.
        task_choice = int(input("\nInsert the number of the task you want to edit.\n"
                                "-1 to return to the menu.\n\n"))

        # If the user inserts the value -1, then the value of 'loop' will be set to False and
        # the while-loop will not be executed again and will be broken out of.
        if task_choice == -1:
            break

    menu()  # Calling the 'menu' function again to await the user's next input.


def display_statistics():
    # This option is only available to the 'admin' user.

    # Defining a function named 'display_statistics' that will display the statistics of all information gathered
    # from the 'task_overview' and 'user_overview' files.

    # Using an if, else-statement to determine whether or not this option is available.
    # If the 'username' variable is equal to 'admin', then the users and tasks will be counted.
    # Otherwise the else-statement will be executed stating an error message.
    if username == "admin":

        # Using a try, except box to test whether or not the needed files exist.
        # The code will try open the files, and if it can't, then the files will be generated.
        try:

            # Opening the 'task_overview.txt' file as 'tasks' and then closing it.
            tasks = open('task_overview.txt')
            tasks.close()
            # Opening the 'user_overview.txt' file as 'users' and then closing it.
            users = open('user_overview.txt')
            users.close()
        except FileNotFoundError:  # Using the FileNotFoundError exception in the case that the file is not found.

            generate_reports()  # Calling the 'generate_reports' function in order to create the needed files.

        # Opening the 'task_overview.txt' file as 'tasks' in read-mode using the 'open' function.
        with open('task_overview.txt', 'r') as tasks:
            data = tasks.readlines()  # Reading each line in 'tasks' to a list.

            print("\n\nTask Overview Info:\n\n")  # Printing heading

            # Using a for-loop to print each line in the 'data' list.
            for line in data:
                print(line)

        # Opening the 'user_overview.txt' file as 'users' in read-mode using the 'open' function.
        with open('user_overview.txt', 'r') as users:
            data = users.readlines()  # Reading each line in 'users' to a list.

            print("\n\nUser Overview Info:\n\n")  # Printing heading

            # Using a for-loop to print each line in the 'data' list.
            for line in data:
                print(line)

    else:

        # Printing a error statement telling the user that only the 'admin' can display statistics.
        # This will only run if the admin is not the current user.

        print("Only the user 'admin' is able to use this option")

    menu()  # Calling the 'menu' function again to await the user's next input.


def leave():
    # Defining a function named 'leave' that will quit the program when called.

    quit()  # Using the 'quit' function to exit the program.


def generate_reports():
    # This option is only available to the 'admin' user.

    # Defining a function named 'generate_reports' that will create reports providing helpful information based on
    # the data in the 'user.txt' and 'tasks.txt' files

    # Declaring a variable for each counter needed to create the 'task_overview' and 'user_overview' files.
    task_total = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_count = 0

    # Using an if, else-statement to determine whether or not this option is available.
    # If the 'username' variable is equal to 'admin', then the reports will be generated.
    # Otherwise the else-statement will be executed stating an error message.
    if username == "admin":

        # ------- TASK OVERVIEW ------- #

        # Opening the 'tasks.txt' file as 'tasks' in read-mode using the 'open' function.
        with open('tasks.txt', 'r') as tasks:

            # Reading each line in the 'tasks.txt' file and storing it in a list called 'data'.
            data = tasks.readlines()

            # Adding 1 to 'tasks_total' for every line in the 'tasks' text-file.
            for task in data:
                task_total += 1

                # Getting the details of each task by splitting from each comma and space (, ).
                details = task.strip('\n').split(', ')

                # If the last index in the 'details' list is equal to 'Yes', then the 'completed_tasks' variable is
                # incremented by 1.
                if details[5] == 'Yes':
                    completed_tasks += 1

                # If the last index in the 'details' list is equal to 'No', then the 'uncompleted_tasks' variable is
                # incremented by 1.
                if details[5] == 'No':
                    uncompleted_tasks += 1

                # Creating a boolean named 'overdue' and setting it to False.
                # This boolean will be used to determine whether or not a task is overdue.
                overdue = False

                due_date = details[4].strip()  # Assigning 'due_date' to the 5th index in the 'details' list.

                # Converting the 'due_date' variable into the correct format so that it can be compared.
                due_date = datetime.strptime(due_date, '%d %b %Y')

                present = datetime.today()  # Creating a variable called 'present' based on the current date.

                # Using an if-statement to determine whether or not the present date has passed the due-date.
                if present > due_date:
                    overdue = True

                # Using an if-statement to determine whether or not the task is overdue.
                # If the task is not completed AND the 'overdue' boolean is True, then the 'overdue_count' variable
                # will be incremented by 1.
                if details[5] == 'No' and overdue:
                    overdue_count += 1

            # Calculating the incomplete percentage
            incomplete_perc = round(uncompleted_tasks / task_total * 100)

            # Calculating the overdue percentage
            overdue_perc = round(overdue_count / task_total * 100)

        # Generating the 'task_overview.txt' file as 'tasks' in write-mode using the 'open' function.
        with open('task_overview.txt', 'w') as tasks:
            # Write the details for the tasks to the 'task_overview' file in an easy-to-read format.
            tasks.write(f"The total number of tasks that have been generated and "
                        f"tracked using the task_manager.py:\t{task_total}\n"
                        f"The total number of completed tasks:\t\t\t\t\t\t\t\t{completed_tasks}\n"
                        f"The total number of uncompleted tasks:\t\t\t\t\t\t\t\t{uncompleted_tasks}\n"
                        f"The total number of tasks that haven't been completed and are overdue:\t\t\t\t{overdue_count}\n"
                        f"The percentage of tasks that are incomplete:\t\t\t\t\t\t\t{incomplete_perc}%\n"
                        f"The percentage of tasks that are incomplete:\t\t\t\t\t\t\t{overdue_perc}%\n")

        # ---------- USER OVERVIEW ---------- #

        user_list = []  # Creating a list named 'user_list' to store each user in the 'user.txt' file.

        # Opening the 'user.txt' file as 'users' in read-mode using the 'open' function.
        with open('user.txt', 'r') as users:

            # Reading each line in the 'user.txt' file and storing it in a list called 'user_info'.
            user_info = users.readlines()

            # Creating a counter for the total amount of users and calling it 'total_users'.
            total_users = 0

            # Using a for-loop to run through each value in the 'user_info' list.
            for line in user_info:

                total_users += 1  # Incrementing the 'total_users' variable by 1 for every index.

                # Getting the name of each user by splitting from each comma (,) and stripping any spaces.
                user_details = line.strip().split(',')

                # Appending the name of each user to the 'user_list' list. This list will be used for writing later on.
                user_list.append(user_details[0])

        # Opening the 'tasks.txt' file as 'tasks' in read-mode using the 'open' function.
        with open('tasks.txt', 'r') as tasks:

            # Reading each line in the 'tasks.txt' file and storing it in a list called 'data'.
            data = tasks.readlines()

        # Generating the 'user_overview.txt' file as 'users' in write-mode using the 'open' function.
        with open('user_overview.txt', 'w') as users:

            # Generating and writing the first text for the 'user_overview' file.
            users.write(f"The total number of users registered with task_manager.py:\t\t\t\t\t\t{total_users}\n"
                        f"The total number of tasks that have been generated and "
                        f"tracked using the task_manager.py:\t\t{task_total}\n\n\t"
                        f"Information on each user:\n\n")

        # Opening the 'user_overview.txt' file as 'users' in append-mode using the 'open' function.
        with open('user_overview.txt', 'a') as users:

            # Using a for-loop to run through each user in the 'user_list' list.
            # This is to find all tasks related to that specific user.
            for user in user_list:

                # Creating the counters for each needed piece of information.
                user_task_count = 0
                user_completed_tasks = 0
                user_uncompleted_tasks = 0
                user_overdue_tasks = 0

                # Using a for-loop to run through each task in the 'tasks.txt' file.
                for task in data:

                    # If the current user in the 'user_list' list is found in the current task,
                    # then that user's specific task details are found.
                    if user in task:

                        user_task_count += 1  # The user's total task count is incremented by 1

                        # Getting the details of each task by splitting from each comma and space (, ).
                        details = task.strip().split(', ')

                        # Using an if,elif-statement to determine whether the task has been completed or not.
                        # If the Task Completed is 'Yes', then 'user_completed_tasks' will be incremented by 1.
                        # Otherwise 'user_uncompleted_tasks' will be incremented by 1.
                        if details[5] == 'Yes':
                            user_completed_tasks += 1
                        elif details[5] == 'No':
                            user_uncompleted_tasks += 1

                        due_date = details[4].strip()  # Assigning 'due_date' to the 5th index of the 'details' list.

                        # Changing the format of the 'due_date' variable so that it can be compared.
                        due_date = datetime.strptime(due_date, '%d %b %Y')

                        overdue = False  # Creating a boolean named 'overdue' with the value of False.

                        # If the present date variable is past the due-date variable,
                        # then the 'overdue' variable is changed to True
                        if present > due_date:
                            overdue = True

                        # Using an if-statement to determine whether or not the task is overdue.
                        # If the task is not completed AND the 'overdue' boolean is True,
                        # then the 'user_overdue_tasks' variable will be incremented by 1.
                        if details[5] == 'No' and overdue:
                            user_overdue_tasks += 1

                # Calculating the percentage of tasks belonging to user based on the total amount of tasks.
                user_task_perc = round(user_task_count / task_total * 100)

                # Using an if, else-statement to test whether or not the calculation should be made.
                # If any of the counters are equal to zero,
                # then that percentage won't be calculated as you cannot multiply anything by 0
                if user_completed_tasks == 0:
                    user_complete_perc = 0
                else:

                    # Calculating the percentage of tasks that the user has completed.
                    user_complete_perc = round(user_completed_tasks / user_task_count * 100)

                if user_uncompleted_tasks == 0:
                    user_uncompleted_perc = 0
                else:
                    # Calculating the percentage of tasks that the user has NOT completed.
                    user_uncompleted_perc = round(user_uncompleted_tasks / user_task_count * 100)

                if user_overdue_tasks == 0:
                    user_overdue_perc = 0
                else:
                    # Calculating the percentage of tasks that the user has overdue.
                    user_overdue_perc = round(user_overdue_tasks / user_task_count * 100)

                # Writing the information to the 'user_overview.txt' file in an easy-to-read format.
                users.write(f"\t{user}\n\tThe total number of tasks assigned to user:\t\t\t\t\t\t{user_task_count}\n\t"
                            f"Percentage of the total number of tasks that have been assigned to user:"
                            f"\t\t{user_task_perc}%\n\t"
                            f"Percentage of the user's tasks that have been completed:\t\t\t\t{user_complete_perc}%\n\t"
                            f"Percentage of the user's tasks that have not been completed:"
                            f"\t\t\t\t{user_uncompleted_perc}%\n\t"
                            f"Percentage of the user's tasks that have not been completed AND are overdue:"
                            f"\t\t{user_overdue_perc}%\n\n")

        print("\n\nFiles Successfully Generated")  # Printing success message

    else:

        # Printing a error statement telling the user that only the 'admin' can generate reports.
        # This will only run if the admin is not the current user.

        print("Only the user 'admin' is able to use this option")

    menu()  # Calling the 'menu' function again to await the user's next input.


def login():
    # --------------------------------------------- CORRECTION LOOP ------------------------------------------------- #

    # Making the 'username' and 'password' global variables so that they can be used inside this function.
    global username
    global password

    entry = False  # Creating a boolean variable called 'entry' with the value False

    # Opening the 'user.txt' file as 'users' in read-mode using the 'open' function.
    with open("user.txt", "r") as users:  # Opening the 'users' text-file in read-only mode.

        # Creating a for-loop to go through every line in the 'users' text-file.
        # If the username AND the password inputs are found on the same row within the text-file, then the user will be
        # granted access.

        for line in users:

            if username.lower() in line and password in line:
                entry = True
                break

    # Creating while-loop to repeatedly ask the user for their username
    # and password until it is found in the text-file.
    while not entry:

        # Printing the error message to the user to inform them that their username or password is incorrect.

        print("\n\nIncorrect Username or Password. Please ensure you are registered and that your spelling is correct.")

        username = input("\nInsert Your Username:\t")  # Asking the user to input their username again.
        password = input("Insert Your Password:\t")  # Asking the user to input their password again.

        # Opening the 'user.txt' file as 'users' in read-mode using the 'open' function.
        with open("user.txt", "r") as users:  # Opening the 'users' text-file in read-only mode.

            # Creating a for-loop to go through every line in the 'users' text-file.
            # If the username AND the password inputs are found on the same row within the text-file,
            # then the user will be granted access.

            for line in users:

                if username.lower() in line and password in line:
                    entry = True
                    break


def menu():
    # ----------------------------------------- USER INPUT ---------------------------------------------------------- #

    # Creating an if, else-statement to determine which menu should be presented.
    # If the 'username' value is equal to "admin", then the special menu will be presented.
    # Otherwise the normal menu will be presented without the 'ds' (Display Statistics) option.
    # Requesting the number for which function the user wants to perform and storing it in an integer named 'option'.
    if username == "admin":

        # Requesting the option the user would like to choose.
        print("\n\nPlease Select One of the Following Options:\n"
              "r - Register User\n"
              "a - Add Task\n"
              "va - View All Tasks\n"
              "vm - View My Tasks\n"
              "gr - generate reports\n"
              "ds - Display Statistics\n"
              "e - Exit\n\n")
    else:

        print("\n\nPlease Select One of the Following Options:\n"
              "r - Register User\n"
              "a - Add Task\n"
              "va - View All Tasks\n"
              "vm - View My Tasks\n"
              "e - Exit\n\n")


# ----------------------------------------------------- EXECUTION --------------------------------------------------- #


# ---------------- LOGIN INFORMATION ----------------- #


# Requesting the username to compare to the 'users.txt' text-file.
username = str.lower((input("\n\nInsert Your Username:\t")))

password = input("Insert Your Password:\t")  # Requesting the password to compare to the 'users.txt' text-file.

login()  # Calling the 'login' function to test whether or not the user is allowed into the program.

menu()  # Calling the 'menu' function to print out the program options for the user.


# ---------------------------------------APPLICATION-LOOP-------------------------------------------- #


# This is where the application is looped until it is told to exit. This will allow users to do more than one task
# in the application without it closing.

app_run = True  # Creating a Boolean named 'app_run' which will be set to True and is never changed to False.

while app_run:  # Creating a while-loop that will always run because the value of 'app_run' will always be True.

    # Requesting input from the user to determine which option from the application they would like to choose.
    answer = input()

    # Using an if, elif-statement to determine which functions should be called.
    # If the 'answer' is equal to one of the provided options, then the corresponding function will be called.
    if answer == 'r':
        reg_user()
    elif answer == 'a':
        add_task()
    elif answer == 'va':
        view_all()
    elif answer == 'vm':
        view_mine()
    elif answer == 'ds':
        display_statistics()
    elif answer == 'gr':
        generate_reports()
    elif answer == 'e':
        leave()


# ------------------------------------------------------------------------------------------------------------------- #


# References:

# - Previous projects on this level

# - HyperionDev (2021). SE L1T20 - Capstone Project III - Files - Task 20. Retrieved 5 March 2021,
#   from Dropbox/ Darren Noortman/ Task 20/ SE L1T20 - Capstone Project III - Files.pdf

# - HyperionDev (2021). example - Task 20. Retrieved 5 March 2021,
#   from Dropbox/ Darren Noortman/ Task 20/ example/ example.pdf

# - HyperionDev (2021). SE L1T25 - Capstone Project IV - Lists, Functions, and String Handling - Task 25. Retrieved 10 March 2021,
#   from Dropbox/ Darren Noortman/ Task 25/ SE L1T25 - Capstone Project IV - Lists, Functions, and String Handling.pdf

# - Unknown Hero (2019). How to Check if a File or Directory Exists in Python - Linuxize. Retrieved 25 March 2021,
#   from https://linuxize.com/post/python-check-if-file-exists/

# - Anupam Chaplot (2020). Simple way of adding task numbers to text file - stackoverflow. Retrieved 25 March 2021,
#   from https://stackoverflow.com/questions/60118561/simple-way-of-adding-task-numbers-to-text-file

# - nagyl (2020). How to run counts from text file for different functions - stackoverflow. Retrieved 25 March 2021,
#   from https://stackoverflow.com/questions/60511335/how-to-run-counts-from-text-file-for-different-functions

# - Jose Ricardo Bustos M. (2015). How to check if a date has Passed in Python - stackoverflow. Retrieved 25 March 2021,
#   from https://stackoverflow.com/questions/29975280/how-to-check-if-a-date-has-passed-in-python-simply

# - bharadhwaj (2016). How to convert dd-mon-yyyy dates to dd-mm-yyyy in python - stackoverflow. Retrieved 25 March 2021,
#   from https://stackoverflow.com/questions/40884442/how-to-convert-dd-mon-yyyy-dates-to-dd-mm-yyyy-in-python

# - Deepa Huddar (2019). How do I write a list into a file in Python? - Quora. Retrieved 15 March 2021,
#   from https://www.quora.com/How-do-I-write-a-list-into-a-file-in-Python

# - Selim (2020). Changing the correct object in the text file - stackoverflow. Retrieved 15 March 2021,
#   from https://stackoverflow.com/questions/60971143/changing-the-correct-object-in-the-text-file

# - Unknown Hero (2019). How to Modify an Item Within a List in Python - Data to Fish. Retrieved 18 March 2021,
#   from https://datatofish.com/modify-list-python/

# - Unknown Hero (?). How to edit a specific line in a text file in Python - kite. Retrieved 17 March 2021,
#   from https://www.kite.com/python/answers/how-to-edit-a-specific-line-in-a-text-file-in-python#:~:text=Use%20list%20indexing%20to%20edit,lines%20to%20overwrite%20the%20file.

# - Fejs (2017). Python find the index of a line of interest in a text file - stackoverflow. Retrieved 25 March 2021,
#   from https://stackoverflow.com/questions/46803413/python-find-the-index-of-a-line-of-interest-in-a-text-file


# ------------------------------------------------------------------------------------------------------------------- #
