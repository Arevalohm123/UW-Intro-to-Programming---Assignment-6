# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# AArevalo,2/7/2021,Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
todo = "C:\\_PythonClass\\Assignment06\\ToDoList.txt"  # The name of the data file
dicRow = {}  # A r ow of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #


class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file: file location of the to-do list
        :param list_of_rows: (list) you want filled with file data:
        :return: list_of_rows: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        obj_file = open(file, "r")
        for line in obj_file:
            read_task, read_priority = line.split(",")
            row = {"Task": read_task.strip(), "Priority": read_priority.strip()}
            list_of_rows.append(row)
        obj_file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(new_task, new_priority, list_of_rows):
        """ Adds a new task and priority to the list of dictionary rows

        :param new_task: (str) new task you want to add
        :param new_priority: (str) new priority you want to add
        :param list_of_rows: (list) of rows you want to display
        :return: list_of_rows: (list) of dictionary rows
        """
        new_row = {"Task": new_task, "Priority": new_priority}
        list_of_rows.append(new_row)
        print("\nTask has been successfully added!")
        IO.print_current_tasks_in_list(list_of_rows)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(remove_task, list_of_rows):
        """ Remove specified task from list of dictionary rows

        :param remove_task: (str) task you want to remove
        :param list_of_rows: (list) of existing tasks and priorities:
        :return: list_of_rows: (list) of dictionary rows
        """
        table_range = len(list_of_rows) - 1
        i = 0
        while i <= table_range:
            if remove_task in str(list(dict(list_of_rows[i]).values())[0]):
                del list_of_rows[i]
                print("\n" + task + " has been successfully deleted!")
                break
            else:
                i = i + 1
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file, list_of_rows):
        """ Write latest list of tasks and priorities to a file

        :param file: file location of the to-do list
        :param list_of_rows: (list) of existing tasks and priorities:
        :return: list_of_rows: (list) of dictionary rows
        """
        obj_file = open(file, "w")
        for dic_row in list_of_rows:
            obj_file.write(dic_row["Task"] + "," + dic_row["Priority"] + "\n")
        obj_file.close()
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        6) Show Current Data
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("\n******* The current To-Do list items are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Gets the input from user on new task and priority

        :return: new_task: (string) input from user on new task
        :return: new_priority: (string) input from user on new priority
        """
        new_task = str(input("\nWhat task would you like to add? :")).strip()
        new_priority = str(input("What is the priority? (1-5): ")).strip()
        return new_task, new_priority

    @staticmethod
    def input_task_to_remove():
        """ Gets the input from user on which existing task to remove

        :return: remove_task: (string) input from user on which task to remove
        """
        remove_task = str(input("\nWhich task would you like to remove?"))
        return remove_task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.


Processor.read_data_from_file(todo, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 Show current data
    IO.print_current_tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        Processor.add_data_to_list(task, priority, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        task = IO.input_task_to_remove()
        Processor.remove_data_from_list(task, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(todo, lstTable)
            IO.input_press_to_continue("File Saved!")
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            Processor.read_data_from_file(todo, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break   # and Exit

    elif strChoice == '6':  # Show Current List
        IO.print_current_tasks_in_list(lstTable)  # Show current data in the list/table
        continue   # and Exit
