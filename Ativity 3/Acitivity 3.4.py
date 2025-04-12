n = int(input("Enter the number: "))
total = 1
for i in range(1, n + 1):
    total *= i
    print(f"{i} *", end= "")
print("=", total)