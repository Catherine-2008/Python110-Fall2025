# ------------------------------------------------------------------------- #
# Title: Working with Dictionaries and Files
# Desc: Shows how to work with dictionaries and files when using a table of data
# Change Log: (Who, When, What)
#   Catherine Ji, 11/8/2025, Created Script
# ------------------------------------------------------------------------- #

import json

# Define the Constants
FILE_NAME: str = 'MyLabData.json'
MENU: str = '''
---------------Student GPAs---------------
    Select from the following menu:
        1. Show Current Student Data
        2. Enter New Student Data
        3. Save Data to a File
        4. Exit the Program
------------------------------------------    
'''
# Define the Variables
student_first_name: str = ''
student_last_name: str = ''
student_gpa: float = 0.0
message: str = ''
menu_choice: str = ''
list_row: list = []
dict_row: dict = {}
students_table: list = []
file_obj = None
file_data: str = ''
user_choice: str = ''

# When the program starts, read the file data into a list of dictionary \
#    rows (table)
#file_obj = open(FILE_NAME,'r')

# Extract the data from the file
#for row in file_obj.readlines():
#    # Transform the data from the file
#    list_row = row.strip().split(",")
#    dict_row = {"FirstName": list_row[0],"LastName": list_row[1],
#                "GPA": float(list_row[2])}
#    # Load it into the collection
#    students_table.append(dict_row)
#file_obj.close()

try:
    file_obj = open(FILE_NAME, 'r')
    students_table = json.load(file_obj)
    file_obj.close()

except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')
# finally:
#     if file_obj.closed == False:
#         file_obj.close()


while True:
    # Repeat the following tasks
    #print(MENU)
    #menu_choice = input("Please enter the menu choice: ")
    menu_choice = input(MENU)
    print()

    if menu_choice == '1':
        # Display the table's current data
        print("----------The current data is:----------")
        for row in students_table:
            if row["GPA"] >= 4.0:
                message = "{} {} earned an A with a {} GPA"
            elif row["GPA"] >= 3.0:
                message = "{} {} earned a B with a {} GPA"
            elif row["GPA"] >= 2.0:
                message = "{} {} earned a C with a {} GPA"
            elif row["GPA"] >= 1.0:
                message = "{} {} earned a D with a {} GPA"
            else:
                message = "{} {}'s {} GPA was not a passing grade"
            print(message.format(row["FirstName"],row["LastName"],row["GPA"]))
        print("-"*40)
        continue

    elif menu_choice == '2':
        try:
            # Input the data
            student_first_name = input("Please enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("Please enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            try: # Using a nested try block to capture when an input cannot be changed to a float
                student_gpa = float(input("Please enter the student's GPA: "))
            except ValueError as e:
                raise ValueError("GPA must be a numeric value.")

            # Add new data to the table
            dict_row ={"FirstName":student_first_name,"LastName":student_last_name,
                       "GPA":student_gpa}
            students_table.append(dict_row)
        except ValueError as e:
            print(e)
            print("-- Technical Error Message --")
            print(e.__doc__)
            print(e.__str__)
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')

        continue

    elif menu_choice =='3':
#        # Save the data to the file
#        file_obj = open(FILE_NAME, 'w')
#        for row in students_table:
#            file_obj.write(f"{row["FirstName"]},{row["LastName"]},{row["GPA"]}\n")
#        file_obj.close()
        try:
            file_obj = open(FILE_NAME,"w")
            json.dump(students_table, file_obj)
            file_obj.close()
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message --")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file_obj.closed == False:
                file_obj.close()
        continue


    elif menu_choice == '4':
        #Exit the program
        break

    else:
        print("Invalid choice! Please try again!")
        continue

print("Program Ended")