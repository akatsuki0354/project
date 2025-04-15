import os

def SMS():
    students = []
    choice = -1
    while choice != 0:
        os.system('cls')
        print("                    #################################################################################################")
        print("                    #                                                                                               #")
        print("                    #                                  ######  ##     ##  ######                                    #")
        print("                    #                                 ##    ## ###   ### ##    ##                                   #")
        print("                    #                                 ##       #### #### ##                                         #")
        print("                    #                                  ######  ## ### ##  ######                                    #")
        print("                    #                                       ## ##     ##       ##                                   #")
        print("                    #                                 ##    ## ##     ## ##    ##                                   #")
        print("                    #                                  ######  ##     ##  ######                                    #")
        print("                    #                                                                                               #")
        print("                    #                                  STUDENT MANAGEMENT SYSTEM                                    #")
        print("                    #                                                                                               #")
        print("                    #################################################################################################")
        print("                    #                                                                                               #")
        print("                    #  [1] Add Student                                                                              #")
        print("                    #  [2] View Student                                                                             #")
        print("                    #  [3] Search Student                                                                           #")
        print("                    #  [0] Exit                                                                                     #")
        print("                    #                                                                                               #")
        print("                    #################################################################################################")
        print("                    #                                                                                               #")
        print("                    #  Enter your choice:                                                                           #")
        print("                    #                                                                                               #")
        print("                    #################################################################################################")
        print("\033[F\033[F\033[F", end="")  # Move to input line
        print("\033[42C", end="")  # Move cursor to aligned input spot

        try:
            choice = int(input())
        except ValueError:
            print("\n\033[38CInvalid input. Press Enter to continue...", end="")
            input()
            continue

        if choice == 1:
            os.system('cls')
            print("                    #################################################################################################")
            print("                    #                                      ADD STUDENT                                              #")
            print("                    #################################################################################################")
            print("                    #                                                                                               #")
            print("                    #  Enter student name:                                                                          #")
            print("                    #  Enter student ID:                                                                            #")
            print("                    #                                                                                               #")
            print("                    #################################################################################################")
            print("\033[F\033[F\033[F\033[F", end="")  # Go to ID input
            print("\033[43C", end=""); name = input().upper()
            print("\033[41C", end=""); student_id = input().upper()
            students.append({'id': student_id, 'name': name})
            with open("test.txt", "a") as file:
                file.write(f"Name: {name}, ID: {student_id}\n")
            print("                    #################################################################################################")
            print("                    #                                                                                               #")
            print("                    #  STUDENT ADDED SUCCESSFULLY !!!                                                               #")
            print("                    #                                                                                               #")
            print("                    #################################################################################################")
            input("                    Press Enter to continue...")

        elif choice == 2:
            os.system('cls')
            print("                    #################################################################################################")
            print("                    #                                     VIEW STUDENTS                                             #")
            print("                    #################################################################################################")
            if students:
                for student in students:
                    print(f"                    #  Name: {student['name']:<25} ID: {student['id']:<30}                            #")
            else:
                print("                    #  No students found.                                                                            #")
            print("                    #################################################################################################")
            input("                    Press Enter to continue...")

        elif choice == 3:
            os.system('cls')
            print("                    #################################################################################################")
            print("                    #                                     SEARCH STUDENT                                            #")
            print("                    #################################################################################################")
            print("                    #                                                                                               #")
            print("                    #  Enter student ID to search:                                                                  #")
            print("                    #                                                                                               #")
            print("                    #################################################################################################")
            print("\033[F\033[F\033[F", end="")
            print("\033[50C", end=""); search_id = input().upper()
            found = False
            for student in students:
                if student['id'] == search_id:
                    print("                    #################################################################################################")
                    print(f"                    #  Student found. ID: {student['id']}, Name: {student['name']:<35}              #")
                    print("                    #################################################################################################")
                    found = True
                    break
            if not found:
                print("                    #################################################################################################")
                print("                    #                                                                                               #")
                print("                    #  Student not found.                                                                           #")
                print("                    #                                                                                               #")
                print("                    #################################################################################################")
            input("                    Press Enter to continue...")

        elif choice == 0:
            print("                    Returning to main menu...")
            input("                    Press Enter to continue...")
            MainProject()

        else:
            print("                    #################################################################################################")
            print("                    #                                                                                               #")
            print("                    #  Invalid option. Please enter a valid number.                                                 #")
            print("                    #                                                                                               #")
            print("                    #################################################################################################")
            input("                    Press Enter to continue...")
SMS()