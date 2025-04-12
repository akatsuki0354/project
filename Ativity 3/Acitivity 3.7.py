n = int(input("Enter the Number: "))
total = 0
for i in range(1, n + 1):
    total += i * i
    print(f"{i}^2", end = "")
    if i < n:
        print(" + ", end = "")
print("=", total)