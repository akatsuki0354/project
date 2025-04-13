boys = []
girls = []
n = int(input("Enter the number of characters: "))

for i in range(1, n + 1):
    name = input(f"Enter name #{i}: ").strip().lower()
    
    if name[0] in ["a", "b", "c"]:
        boys.append(name)
    else:
        girls.append(name)
    
    print("Girls: ", girls)
    print("Boys: ", boys)
