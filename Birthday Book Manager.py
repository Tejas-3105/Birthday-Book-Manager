import os
import datetime

"""
Tejas Thind - Birthday Book Manager

What the program does:
The Birthday Book Manager is a command-line program designed to assist users in managing birthday information efficiently. 
It offers various commands for adding, listing, deleting, searching, saving, and loading birthday entries.

Input:
The inputs to the program include commands entered by the user, along with any necessary additional arguments. 
For example, inputs may consist of commands like "add," "list," "delete," "search," "save," and "load," along with 
corresponding data such as names, dates, and filenames.

Output:
The output of the program varies depending on the command executed.
 
For instance:
Adding an entry displays a confirmation message.
Listing entries presents a numbered list of all birthdays.
Deleting an entry prompts for confirmation and may display error messages if necessary.
Searching for birthdays lists matching entries.
Saving to a file confirms the action with a message.
Loading from a file adds birthdays to the current list with appropriate feedback.
Additionally, the program provides error messages for invalid inputs or commands, 
ensuring seamless interaction with the user.
"""

# Here's one function for you. No reason for everyone to write this one.
def print_help(): 
    """This function can be used to print out the help message."""
    print("Allowed commands:")
    print("1. add [firstName] [lastName] [month] [day] [year]")
    print("2. list") 
    print("3. delete [number]")
    print("4. search [name]")
    print("5. sort alphabetically (by first name)")
    print("   sort age")
    print("6. save [filename]")
    print("7. load [filename]")
    print("8. help")
    print("9. echo on")
    print("   echo off")


# Define the main function of the Birthday Book program
def main():
    """The main function of the Birthday Book program."""

    # Print a welcome message
    print()
    print("\033[1m\033[4mWelcome to the Birthday Book Manager\033[0m")
    print()
    print('Enter "help" to see a list of commands.')
    
    # Initialize lists and variables
    birthday_list = []  # List to store birthdays
    names_list = []     # List to store names
    saved_files = []    # List to store names of saved files
    echo_flag = False   # Flag to determine if echoing is enabled or not
    
    # Infinite loop for user to keep entering commands
    while True:
        user_input = input('> ')  # Prompt user for input
        input_list = user_input.split()  # Split the input string into a list

        # Error Testing and processing the input
        if input_list[0] == 'add':
            # Call function to add birthday
            add_Birthday(input_list, birthday_list, names_list, echo_flag, user_input)  
        elif input_list[0] == 'list' and len(input_list) == 1:
            # Call function to list birthdays
            list_bdays(birthday_list, echo_flag, user_input) 
        elif input_list[0] == 'delete' and len(input_list) == 2:
            # Call function to delete an entry
            delete_entry(input_list[1], birthday_list, names_list, echo_flag, user_input) 
        elif input_list[0] == 'search' and len(input_list) == 2:
            # Call function to search for a name
            search_name(input_list[1], names_list, birthday_list, echo_flag, user_input)
        elif input_list[0] == 'sort' and len(input_list) == 2:
            # Call function to sort the list of birthdays
            sort_list(input_list[1], birthday_list, echo_flag, user_input)
        elif input_list[0] == 'save':
            # Call function to save data to a file
            saved_files.append(save_to_file(input_list[1], birthday_list, echo_flag, user_input, names_list))
        elif input_list[0] == 'load':
            # Call function to load data from a file
            load_file(input_list[1], birthday_list, saved_files, echo_flag, user_input, names_list)
        elif input_list[0] == 'help' and len(input_list) == 1:
            if echo_flag:
                print(f'You entered: "help"')
            print_help()  # Call function to display help information
        elif input_list[0] == 'quit' and len(input_list) == 1:
            if echo_flag:
                print(f'You entered: "quit"')
            print('Thank you for using the Birthday Book Manager!')
            break  # Exit loop if 'quit' command is entered
        elif input_list[0] == 'echo':
            echo_flag = echo(input_list[1], echo_flag)  # Call function to toggle echoing
        else:
            if echo_flag:
                print(f'You entered: "{user_input}"')
            print("I am sorry, but that is not a recognized command, or")
            print("you have entered an incorrect number of arguments.")
            print("You may enter 'help' to see a list of commands.")

# Function to add a birthday entry to the list.
def add_Birthday(input_list, birthday_list, names_list, echo_flag, user_input):
    """
    Add a birthday entry to the birthday book.

    Parameters:
        input_list (list): List containing the input arguments.
        birthday_list (list): List of birthdays.
        names_list (list): List of names corresponding to birthdays.
        echo_flag (bool): Flag indicating whether echoing is enabled.
        user_input (str): The user input command.

    Returns:
        tuple: A tuple containing the updated birthday list and names list.
    """
    # Check if echoing is enabled and print user input
    if echo_flag:
        print(f'You entered: "{user_input}"')
    
    # Check if the number of arguments is correct
    if len(input_list) != 6:
        print("I am sorry, but that is not a recognized command, or")
        print("you have entered an incorrect number of arguments.")
        print("You may enter 'help' to see a list of commands.")
    # Check if the date components are integers
    elif not (input_list[3].isdigit() and input_list[4].isdigit() and input_list[5].isdigit()):
        print("Error: Unable to add birthday to book. Please use integers for dates.")
    else:
        # If all error tests passed, create Birthday object and print message
        birthday = Birthday(input_list[1], input_list[2], input_list[3], input_list[4], input_list[5])
        print(f'Added "{birthday}" to birthday book.')
        # Append the first name and last name to the names list
        names_list.append(input_list[1] + ' ' + input_list[2])
        # Format and add the birthday entry to the birthday list
        format_list(input_list[1], input_list[2], input_list[3], input_list[4], input_list[5], birthday_list)
        # Return the updated birthday list and names list
        return birthday_list, names_list

# Function to format and add a birthday entry to the list.
def format_list(firstName, lastName, month, day, year, birthday_list):
    """
    Format and add a birthday entry to the birthday list.

    Parameters:
        firstName (str): The first name of the person.
        lastName (str): The last name of the person.
        month (str): The month of the birthday.
        day (str): The day of the birthday.
        year (str): The year of the birthday.
        birthday_list (list): The list of birthdays.

    Returns:
        list: The updated birthday list.
    """
    # Format the birthday entry
    bday = f'{firstName} {lastName}, {month}/{day}/{year}'
    birthday_list.append(bday)
    # Return the updated birthday list
    return birthday_list

# Function to list birthdays in the birthday book.
def list_bdays(birthday_list, echo_flag, user_input):
    """
    List birthdays in the birthday book.

    Parameters:
        birthday_list (list): The list of birthdays.
        echo_flag (bool): Flag indicating whether echoing is enabled.
        user_input (str): The user input command.
    """
    # Check if echoing is enabled and then echo the user input
    if echo_flag:
        print(f'You entered: "{user_input}"')
    # Check if the birthday list is not empty
    if len(birthday_list) > 0:
        # Iterate over the birthday list and print each entry
        for i in range(len(birthday_list)):
            print(f'{i + 1}. {birthday_list[i]}')
    else:
        # Print a message if the birthday book is empty
        print("The birthday book is empty.")

# Function to delete an entry from the birthday book.
def delete_entry(user_entry, birthday_list, names_list, echo_flag, user_input):
    """
    Parameters:
        user_entry (str): The index of the entry to delete.
        birthday_list (list): The list of birthdays.
        names_list (list): The list of names corresponding to birthdays.
        echo_flag (bool): Flag indicating whether echoing is enabled.
        user_input (str): The user input command.

    Returns:
        The updated birthday list and names list if an entry is deleted.
        Otherwise, returns the unchanged birthday list.
    """
    # Check if echoing is enabled and print user input
    if echo_flag:
        print(f'You entered: "{user_input}"')

    # Convert user entry to an integer to use as index
    index = int(user_entry)
    
    # Check if the index is out of range
    if index <= 0 or index > len(names_list):
        print('I\'m sorry, but there is no such entry in the book.')
        return birthday_list  # Return unchanged list if index is out of range
    
    # Verify user input
    if not user_entry.isdigit():
        print('Error: Please specify the item to delete using an integer.')
        return birthday_list  # Return unchanged list if input is not a number

    # Get the name corresponding to the index
    name = names_list[index - 1]
    
    # Prompt the user for confirmation
    user_answer = input(f'Really delete {name} from the birthday book? (y/n) ')
    while True:
        # Validate user input
        if user_answer != 'y' and user_answer != 'n':
            pass
        # If they say no, return unchanged birthday list
        elif user_answer == 'n':
            return birthday_list
        elif user_answer == 'y':
            # Remove the entry from the birthday list if confirmed
            birthday_list.pop(index - 1)
            names_list.pop(index - 1)
            return birthday_list, names_list
        user_answer = input('Please enter "y" or "n" (y/n) ')
        
# Function to search for a name in the birthday book.
def search_name(name_to_search, names_list, birthday_list, echo_flag, user_input):
    """
    Parameters:
        name_to_search (str): The name to search for.
        names_list (list): The list of names corresponding to birthdays.
        birthday_list (list): The list of birthdays.
        echo_flag (bool): Flag indicating whether echoing is enabled.
        user_input (str): The user input command.
    """
    # Check if echoing is enabled and print user input
    if echo_flag:
        print(f'You entered: "{user_input}"')
    
    # Initialize a list to store matching entries
    matches = []
    
    # Iterate over names in the names list
    for i in range(len(names_list)):
        name_person = names_list[i].split()  # Split the name into first and last name
        # Iterate over parts of the name
        for j in range(len(name_person)):
            # Check if any part of the name matches the search term (case insensitive)
            if name_person[j].lower() == name_to_search.lower():
                matches.append(birthday_list[i])  # Add the corresponding birthday to the matches list
    
    # Check if there are any matches
    if matches:
        print(f'Entries with a name of "{name_to_search}"')
        # Print each matching entry
        for i in range(len(matches)):
            print(f'   {matches[i]}')
    # If no matches found, print a message
    if not matches:
        print(f'I\'m sorry, but there are no entries with a name of "{name_to_search}".')

# Sorts the birthday list based on the given sort type.
def sort_list(sort_type, birthday_list, echo_flag, user_input):
    """
    Parameters:
    sort_type (str): The type of sorting to be performed. Can be 'alphabetically' or 'age'.
    birthday_list (list): The list of birthdays to be sorted.
    echo_flag (bool): Flag to determine whether to print the user input.
    user_input (str): The user input to be printed if echo_flag is True.

    Returns:
    list: The sorted birthday list.

    """
    # If echoing is enabled, print the user's input.
    if echo_flag:
        print(f'You entered: "{user_input}"')

    # If sorting alphabetically:
    if sort_type == 'alphabetically':
        # Sort the birthday list alphabetically.
        birthday_list.sort()
        print('Birthdays successfully sorted alphabetically. \nType "list" to view the changes.')
        return birthday_list

    # If sorting by age:
    elif sort_type == 'age':
        age_list = []
        for i in range(len(birthday_list)):
            # Split the birthday string into its components and convert to a date object.
            birthday = birthday_list[i].split()
            birthday = birthday[2].split('/')
            birthday_1 = datetime.date(int(birthday[2]), int(birthday[0]), int(birthday[1]))
            # Calculate the age and append it to the age list.
            age = calculate_age(birthday_1)
            age_list.append(age)
        # Iterate through the age list for sorting.
        for j in range(0, len(age_list) - 1):
            # If the age at index j is greater than the age at index j+1, swap the birthdays.
            if age_list[j] > age_list[j + 1]:
                temp = birthday_list[j]
                birthday_list[j] = birthday_list[j + 1]
                birthday_list[j + 1] = temp
        print('Birthdays successfully sorted by age (ascending). \nType "list" to view the changes.')
        return birthday_list


# Calculates the age based on the given birthday.
def calculate_age(birthday):
    """
    Parameters:
    birthday (datetime.date): The date of birth.

    Returns:
    int: The calculated age.
    """
    today = datetime.date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

# Function to save birthdays to a file.
def save_to_file(filename, birthday_list, echo_flag, user_input, names_list):
    """
    Parameters:
        filename (str): The name of the file to save to.
        birthday_list (list): The list of birthdays.
        echo_flag (bool): Flag indicating whether echoing is enabled.
        user_input (str): The user input command.
        names_list (list): The list of names corresponding to birthdays.

    Returns:
        The filename if birthdays are successfully saved.
    """
    # Check if echoing is enabled and print user input
    if echo_flag:
        print(f'You entered: "{user_input}"')
    
    # Open the file in write mode and write each birthday and corresponding name
    with open(filename, 'w') as file:
        for i in range(len(birthday_list)):
            file.write(f'{birthday_list[i]}\n')
            file.write(f'{names_list[i]}\n')
        print(f'Saved birthdays to "{filename}".')
        return filename
    
# Function to load birthdays from a file.
def load_file(filename, birthday_list, saved_files, echo_flag, user_input, names_list):
    """
    Parameters:
        filename (str): The name of the file to load from.
        birthday_list (list): The list of birthdays.
        saved_files (list): The list of previously saved files.
        echo_flag (bool): Flag indicating whether echoing is enabled.
        user_input (str): The user input command.
        names_list (list): The list of names corresponding to birthdays.

    Returns:
        The updated birthday list and names list if birthdays are loaded successfully.
        Otherwise, returns the unchanged birthday list and names list.
    """
    # Check if echoing is enabled and print user input
    if echo_flag:
        print(f'You entered: "{user_input}"')
    try:
        with open(filename, 'r') as file:
            # Check to see if the file name is the same as a previously saved one
            if len(saved_files) == 0:
                print(f"I'm sorry, but \"{filename}\" is not in the correct format.")
                print('You can only load files saved by this same program.')
            else:
                # Iterate through the list of saved file names
                for i in range(len(saved_files)):
                    # Compare the name of the file to be loaded with each of the saved file names
                    if filename == saved_files[i]:
                        lines = file.readlines()
                        for i in range(0, len(lines), 2):  # Iterate through every other line
                            # Add the entire line to the respective lists
                            birthday_list.append(lines[i].strip())
                            names_list.append(lines[i + 1].strip())
                    else:
                        print(f"I'm sorry, but \"{filename}\" is not in the correct format.")
                        print('You can only load files saved by this same program.')
                print(f'Birthdays in "{filename}" added to birthday book.')
                return birthday_list, names_list
    except FileNotFoundError:
        print(f"I'm sorry, but \"{filename}\" does not exist.")

# Sets the echo_flag variable on or off based on user input.
def echo(command, echo_flag):
    """
    Parameters:
        command (str): The users command to toggle echo on or off
        echo_flag (bool): Flag indicating whether echoing is currently enabled.

    Returns:
        The updated echo_flag value indicating whether echoing is now enabled or disabled.
    """
    # Verify user input
    try:
        # Try to convert the user entry to an integer
        int_value = int(command)
        # Try to convert the user entry to a float
        float_value = float(command)
        # If both conversions succeed, it's numeric (int or float)
        print("I am sorry, but that is not a recognized command, or")
        print("you have entered an incorrect number of arguments.")
        print("You may enter 'help' to see a list of commands.")
    except ValueError:
        # If the user entry is not numeric, check if it's a valid command
        if command != 'on' and command != 'off':
            print('Error: Please enter either "echo on" or "echo off"')
            print("You may enter 'help' to see a list of commands.")
        elif command == 'on':
            print('Echo turned on.')
            return True  # Return True to indicate echo is turned on
        elif command == 'off':
            if echo_flag:
                print(f'You entered: "echo off"')
                print('Echo turned off.')
            return False  # Return False to indicate echo is turned off

# Represents a person's birthday.
class Birthday:
    
    def __init__(self, firstName, lastName, month, day, year):
        # Initializes a Birthday object with the given attributes.

        self.firstName = firstName
        self.lastName = lastName
        self.month = month
        self.day = day
        self.year = year

    #Returns a string representation of the Birthday object.
    def __str__(self):

        return f'{self.firstName} {self.lastName}, {self.month}/{self.day}/{self.year}'
    
# Do not modify the code below.  Write all of your code above.
if __name__ == "__main__":
    main()