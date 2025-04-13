students = []

while True:
    print("1. Add Student")
    print("2. View Student")
    print("3. search Student")
    print("4. Exit")
    choice = int(input("Enter the number: "))
    
    if choice == 1:
        name = input("name: ").upper()
        id = input("ID").upper()
        students.append({'id': id, 'name': name})
        print(" STUDENT ADDED SUCCESSFULLY !!! ")
        with open("test.txt","a") as file:
                file.write(f"Name: {name}, ID: {id}\n")
    elif choice == 2:
            for student in students:
                print(f"Name: {student['name']}, id: {student['id']} ")
            else:
                print("student not found")
    elif choice == 3:
        id = input("Enter id: ")
        for student in students:
            if student['id'] == id:
                print(f"Student found. Name: {student['id']}, Name: {student['name']}")
                break
            else:
                print("not found!!!....")
        
    