number = int(input("Enter the number up to 3000: "))
if number > 3000:
    print("Cannot handle more than 3000")
else:
    thousands = number - (number % 1000)
    hundreds = number % 1000 - (number % 100)
    tens = number % 100 - (number % 10)
    ones = number % 10

    if thousands == 1000:
        print("M", end="")
    elif thousands == 2000:
        print("MM", end="")
    elif thousands == 3000:
        print("MMM", end="")
        
    if hundreds == 100:
        print("C", end="")
    elif hundreds == 200:
        print("CC", end="")
    elif hundreds == 300:
        print("CCC", end="")
    elif hundreds == 400:
        print("CD", end="")
    elif hundreds == 500:
        print("D", end="")
    elif hundreds == 600:
        print("DC", end="")
    elif hundreds == 700:
        print("DCC", end="")
    elif hundreds == 800:
        print("DCCC", end="")
    elif hundreds == 900:
        print("CM", end="")

    if tens == 10:
        print("X", end="")
    elif tens == 20:
        print("XX", end="")
    elif tens == 30:
        print("XXX", end="")
    elif tens == 40:
        print("XL", end="")
    elif tens == 50:
        print("L", end="")
    elif tens == 60:
        print("LX", end="")
    elif tens == 70:
        print("LXX", end="")
    elif tens == 80:
        print("LXXX", end="")
    elif tens == 90:
        print("XC", end="")

    if ones == 1:
        print("I")
    elif ones == 2:
        print("II")
    elif ones == 3:
        print("III")
    elif ones == 4:
        print("IV")
    elif ones == 5:
        print("V")
    elif ones == 6:
        print("VI")
    elif ones == 7:
        print("VII")
    elif ones == 8:
        print("VIII")
    elif ones == 9:
        print("IX")
    elif ones == 0:
        print()
