n = int(input("Enter the number: "))
total = 1
for i in range(1, n + 1):
    print(f"{i}", end= "")
    total *= i
    if i < n:
        print(" * ",  end= "")
print(" =", total)