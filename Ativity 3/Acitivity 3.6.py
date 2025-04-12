n1 = int(input("Enter base Number: : "))
n2 = int(input("Enter Exponent Number: "))
total = 1
for i in range(1, n2 + 1):
    total *= n1
    print(n1, end=" ")
    if i < n2:
        print("*", end=" ")
print("=",total)