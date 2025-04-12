n = int(input("enter the number: "))
x = 1
y = 1
t = 0
for i in range(1, n):
    t = x + y
    x = y
    y = t
    print(x)