grades = int(input("Enter the grades: "))

if grades >= 98:
    print("1.00")
elif grades >= 95:
    print("1.25")
elif grades >= 92:
    print("1.50")
elif grades >= 89:
    print("1.75")
elif grades >= 85:
    print("2.00")
elif grades >= 80:
    print("2.25")
elif grades >= 77:
    print("2.75")
elif grades <= 75:
    print("3.00")
else:
    print("out of range")