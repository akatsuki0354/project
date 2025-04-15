user_input = input("Enter something: ").strip()
while not user_input:
    print("Input cannot be empty.")
    user_input = input("Enter something: ").strip()

print(f"You entered: {user_input}")
