n = int(input("Enter the number: "))

x, y = 1, n
while x< n + 1:
    print(f"{x}{y}", end = "")
    x += 1
    y -= 1