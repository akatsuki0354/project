n = int(input("Enter the number: "))
total = 0
for i in range(1, n + 1):
    print(i, end="")
    if i < n:
        print(" + ", end="")
    total += i
    
print(" =", total)