print("Student Management System feature is selected.")
students = []

while True:
    print("⌇⌇≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⌇⌇")
    print("⌇⌇                                        ⌇⌇")
    print("⌇⌇       STUDENT MANAGEMENT SYSTEM        ⌇⌇")
    print("⌇⌇≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⌇⌇")
    print("⌇⌇       [1] INPUT STUDENT NAME           ⌇⌇")
    print("⌇⌇       [2] DISPLAY STUDENTS             ⌇⌇")
    print("⌇⌇       [3] SEARCH STUDENTS              ⌇⌇")
    print("⌇⌇       [4] EXIT                         ⌇⌇")
    print("⌇⌇                                        ⌇⌇")
    print("⌇⌇≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⌇⌇")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("⌇⌇≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⌇⌇")
        print("⌇⌇≡≡≡≡≡≡≡   INPUT STUDENT NAME    ≡≡≡≡≡≡≡⌇⌇")
        print("⌇⌇≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⌇⌇")
        id = input(" ENTER STUDENT ID : ")
        name = input(" ENTER STUDENT NAME : ")
        students.append({'id': id, 'name': name})
        print(" STUDENT ADDED SUCCESSFULLY !!! ")
        with open("test.txt","a") as file:
            file.write(f"Name: {name}, ID: {id}\n")
            print(" STUDENT SUCESSFULLY ADDED IN test.txt FILE ")
    elif choice == '2':
            if not students:
                print("⌇⌇≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⌇⌇")
                print("⌇⌇≡≡≡≡≡≡  NO STUDENT RECORD FOUND !  ≡≡≡≡⌇⌇")
                print("⌇⌇≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⌇⌇")
            else:
                print("⌇⌇≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⌇⌇")
                print("⌇⌇≡≡≡≡≡≡≡≡≡≡  STUDENT FOUND !    ≡≡≡≡≡≡≡≡⌇⌇")
                print("⌇⌇≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⌇⌇")
                for student in students:
                    print(f"ID: {student['id']}, Name: {student['name']}")
    elif choice == '3':
            print("⌇⌇≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⌇⌇")
            print("⌇⌇≡≡≡≡≡≡≡   SEARCHING STUDENT !!   ≡≡≡≡≡≡⌇⌇")
            print("⌇⌇≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⌇⌇")
            id = input(" ENTER STUDENT ID TO SEARCH : ")
            found = False
            for student in students:
                if student['id'] == id:
                    print(f"Student found. ID: {student['id']}, Name: {student['name']}")
                    found = True
                    break
            if not found:
                print(" STUDENT NOT FOUND...")
    elif choice == '4':
            print("⌇⌇≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⌇⌇")
            print("⌇⌇≡≡≡≡≡≡≡     PROGRAM EXIT        ≡≡≡≡≡≡≡⌇⌇")
            print("⌇⌇≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⌇⌇")
            print("⌇⌇≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⌇⌇")
            print("⌇⌇≡≡≡≡≡≡≡ THANK YOU FOR USING IT   ≡≡≡≡≡≡⌇⌇")
            print("⌇⌇≡≡≡≡≡≡ AND I HOPE IT WAS HELPFUL ≡≡≡≡≡≡⌇⌇")
            print("⌇⌇≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⌇⌇")
            break
    else:
            print(" INVALID CHOICE .. PLEASE SELECT ONE OF THE GIVEN OPTIONS !! ")

            choice = input(" ARE YOU DONE? IF YOU WANT TO EXIT PLEASE ENTER 0: ")
           
            if choice == '0':
                print("Exiting program.")
              