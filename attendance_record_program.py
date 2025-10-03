# Author: Laura Bejarano
# Date: March-April 2023
# Purpose: The  Module Attendance Records programme will allow a lecturer do the following tasks
#   - Record the attendance of a student for a class session in a particular modules (as present/absent)
#   - View statistical data about the average attendance of each module
from moduleEnrolled import *


def login():
    # printing title:

    login_title = "Module Record System - Login"
    length_login_title = len(login_title)

    print(f"{login_title}")
    print("-" * length_login_title)

    # getting name and password form user:

    user_input_name = input("Name: ").capitalize()
    user_input_psswrd = input("Password: ")

    password_verification(user_input_name, user_input_psswrd)


def password_verification(user_input_name, user_input_psswrd):
    # creating list for usernames and respective passwords:

    list_of_username = []
    list_of_user_passwd = []

    # reading from login data file:

    filename = "login_data.txt"
    with open(filename) as my_file:
        for i, line in enumerate(my_file):
            line = line.rstrip()
            line_data = line.split(",")
            list_of_username.append(line_data[0])
            list_of_user_passwd.append(line_data[1])

    # verifying login data from user input:

    for i in range(len(list_of_username)):
        if list_of_username[i] == user_input_name and list_of_user_passwd[i] == user_input_psswrd:
            welcome_menu(user_input_name)
            soft_6017(user_input_name)
            soft_6018(user_input_name)

        else:
            print("Login Failed.")
            print("Exiting Module Record System.")

        break


def welcome_menu(name):
    # printing Welcoming with user's name and menu with options:

    menu_title = "Module Record System - Options"
    length_menu_title = len(menu_title)

    print(f"\nWelcome {name}")
    print(f"\n{menu_title}")
    print("-" * length_menu_title)

    print("1. Record Attendance ")
    print("2. Generate Statistics ")
    print("3. Exit ")
    user_option = int(input("(1,2 or 3)--> "))

    # indicating to which function the user's option has chosen:

    while True:

        try:
            if user_option == 1:
                record_attendance(name)
            elif user_option == 2:
                generate_statistics()
            elif user_option == 3:
                print("\nExited system.")
                quit()
        except (ValueError, TypeError):
            print("Invalid option. Try again")

        else:
            if 3 < user_option < 1:
                break
            else:
                print("Invalid option. Try again")


def record_attendance(username):

    attendance_title = "Module Record System - Attendance - Choose a Module"
    length_attendance_title = len(attendance_title)

    print(f"\n{attendance_title}")
    print("-" * length_attendance_title)

    print("1. SOFT_6017 ")
    print("2. SOFT_6018 ")
    user_option = int(input("(1 or 2)--> "))

    while True:

        try:
            if user_option == 1:
                soft_6017(username)
            elif user_option == 2:
                soft_6018(username)

        except (ValueError, TypeError):
            print("Invalid option. Try again")

        else:
            if 2 < user_option < 1:
                break
            else:
                print("Invalid option. Try again")


def soft_6017(username):
    # printing title:

    soft_6017_title = "Module Record System - Attendance - SOFT_6017"
    length_soft_6017_title = len(soft_6017_title)

    print(f"\n{soft_6017_title}")
    print("-" * length_soft_6017_title)

    # calculating and printing the number of enrolled students in the module:

    num_of_students_6017 = len(student_list_6017)

    print(f"There are {num_of_students_6017} students enrolled.")

    # assigning filename to the respective module:

    filename = "SOFT_6017.txt"

    # going through all the students and presenting the user with the option to either mark them as absent or present:

    for i in range(num_of_students_6017):
        while True:

            try:
                name_display = Enrolled.print_to_file(student_list_6017[i])
                print(f"\nStudent #{i+1}: {name_display}")
                print("1. Present ")
                print("2. Absent ")
                user_option = int(input("(1 or 2)--> "))

                # if present update the file:

                if user_option == 1:
                    with open(filename, "w") as my_file:
                        for student in student_list_6017:
                            update = Enrolled.update_presents(student)
                            print(update, file=my_file)
                    break

                # if absent update the file:

                elif user_option == 2:
                    with open(filename, "a") as my_file:
                        for student in student_list_6017:
                            update = Enrolled.update_absences(student)
                            print(update, file=my_file)

                    break

            except (ValueError, TypeError):
                print("Invalid option. Try again")

            else:
                if 2 < user_option < 1:
                    break
                else:
                    print("Invalid option. Try again")

    print(f"\n{filename} was updated with the latest attendance records.")

    user_input = input("Press Enter to continue")
    if user_input == '':
        welcome_menu(username)
    else:
        welcome_menu(username)


def soft_6018(username):
    # printing title:

    soft_6018_title = "Module Record System - Attendance - SOFT_6018"
    length_soft_6018_title = len(soft_6018_title)

    print(f"\n{soft_6018_title}")
    print("-" * length_soft_6018_title)

    # calculating and printing the number of enrolled students in the module:

    num_of_students_6018 = len(student_list_6018)

    print(f"There are {num_of_students_6018} students enrolled.")

    # assigning filename to the respective module:

    filename = "SOFT_6018.txt"

    for i in range(num_of_students_6018):
        while True:

            try:
                name_display = Enrolled.print_to_file(student_list_6018[i])
                print(f"\nStudent #{i + 1}: {name_display}")
                print("1. Present ")
                print("2. Absent ")
                user_option = int(input("(1 or 2)--> "))

                # if present update the file:

                if user_option == 1:
                    with open(filename, "a") as my_file:
                        for student in student_list_6018:
                            update = Enrolled.update_presents(student)
                            print(update, file=my_file)

                    break

                # if absent update the file:

                elif user_option == 2:
                    with open(filename, "a") as my_file:
                        for student in student_list_6018:
                            update = Enrolled.update_absences(student)
                            print(update, file=my_file)

                    break

            except (ValueError, TypeError):
                    print("Invalid option. Try again")

            else:
                if 2 < user_option < 1:
                    break
                else:
                    print("Invalid option. Try again")

        print(f"\n{filename} was updated with the latest attendance records.")

        user_input = input("Press Enter to continue")
        if user_input == '':
            welcome_menu(username)
        else:
            welcome_menu(username)


def generate_statistics():
    menu_title = "Module Record System - Average Attendance Data"
    length_menu_title = len(menu_title)
    print(f"\n{menu_title}")
    print("-" * length_menu_title)

    module_names_list = []
    module_codes_list = []

    with open("modules.txt") as my_file:
        for module in my_file:
            module = module.rstrip()
            module_data = module.split(",")
            module_names_list.append(module_data[1])
            module_codes_list.append(module_data[0])

# calculating average attendance for module SOFT_6017:

    attendance_list_17 = []
    absences_list_17 = []

    with open("SOFT_6017.txt") as my_file:
        for line in my_file:
            line = line.rstrip()
            line_date = line.split(',')
            attendance_list_17.append(int(line_date[1]))
            absences_list_17.append(int(line_date[2]))

    num_of_students = len(attendance_list_17)
    sum_of_attendance = sum(attendance_list_17)

    average_days_present = sum_of_attendance / num_of_students
    total_num_days = attendance_list_17[0] + absences_list_17[0]
    average_attendance_6017 = (average_days_present / total_num_days) * 100

# calculating average attendance for module with code SOFT_6018:

    attendance_list_18 = []
    absences_list_18 = []

    with open("SOFT_6018.txt") as my_file:
        for line in my_file:
            line = line.rstrip()
            line_date = line.split(',')
            attendance_list_18.append(int(line_date[1]))
            absences_list_18.append(int(line_date[2]))

    num_of_students = len(attendance_list_18)
    sum_of_attendance = sum(attendance_list_18)

    average_days_present = sum_of_attendance / num_of_students
    total_num_days = attendance_list_18[0] + absences_list_18[0]
    average_attendance_6018 = (average_days_present / total_num_days) * 100


# building the attendance representation bar:
#     status_bar_6017 = Stars.get_stars_bar(average_attendance_6017)
    status_bar_6017 = Stars(average_attendance_6017)
    status_bar_6018 = Stars(average_attendance_6018)

# printing the table:
    module_names_list = []
    module_codes_list = []

    with open("modules.txt") as my_file:
        for module in my_file:
            module = module.rstrip()
            module_data = module.split(",")
            module_names_list.append(module_data[1])
            module_codes_list.append(module_data[0])

    final_stats_6017 = FinalStats(module_names_list[0], module_codes_list[0], average_attendance_6017,
                                  status_bar_6017.get_stars_bar())
    print(final_stats_6017)

    final_stats_6018 = FinalStats(module_names_list[1], module_codes_list[1], average_attendance_6018,
                                  status_bar_6018.get_stars_bar())
    print(final_stats_6018)

    get_best_attended(average_attendance_6017, average_attendance_6018, module_names_list)


def get_best_attended(average_6017, average_6018, module_names_list):
    if average_6017 > average_6018:
        print(f"The best attended module is Modular Programming with a {average_6017:.1f}% attendance rate.")


if __name__ == '__main__':

    student_list_6017 = [Enrolled('Mary Martin', 10, 0),
                         Enrolled('Alan Wilson', 9, 1),
                         Enrolled('Alan Lowe', 5, 5)]

    student_list_6018 = [Enrolled('Mary Martin', 10, 0),
                         Enrolled('Alan Wilson', 9, 1),
                         Enrolled('Alan Lowe', 5, 5)]

    login()
