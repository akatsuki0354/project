import os

def MainProject():
  while True:
        print("[1] Module")
        print("[2] Activit")
        print("[3] SMS")
        print("[0] Exit")
        choice = int(input("Enter the number 0-3: "))
        if choice == 1:
            Module()
        elif choice  == 2:
            Activity()
        elif choice == 3:
            SMS()
        elif choice == 0:
             print("Exiting...")
             exit()
    
def Module():
        os.system('cls')
        print("[1] Module 1 ")
        print("[2] Module 2")
        print("[3] Module 3")
        print("[0] Back")
        choice = int(input("choose the number: "))
        if choice == 0:
            MainProject()
        elif choice == 1:
            Module_1()
        elif choice == 2:
            Module_2()
        elif choice == 3:
            Module_3()
        else:
            print("Invalid Number please select 0-3")
            Module()
def Module_1():
    os.system('cls')
    print("[1] Module 1.1 Volume of Sphere")
    print("[2] Module 1.2 Temp Conversion")
    print("[3] Module 1.3 Peso-Dollar Conversion")
    print("[4] Module 1.4 Measurement Conversion")
    print("[5] Module 1.5 Two Variables")
    print("[6] Module 1.6 Circumfence of a circle")
    print("[7] Module 1.7 Two Variables declaration")
    print("[8] Module 1.8 Puchase Price")
    print("[9] Module 1.9 Economic order quantity")
    print("[10] Module 1.10 radius of a circle")
    print("[0] Back")
    choice = int(input("choose the number: "))
    while choice != 0:
        if choice == 1:
            Module_1_1()
        elif choice == 2:
            Module_1_2()
        elif choice == 3:
            Module_1_3()
        elif choice == 4:
            Module_1_4()
        elif choice == 5:
            Module_1_5()
        elif choice == 6:
            Module_1_6()
        elif choice == 7:
            Module_1_7()
        elif choice == 8:
            Module_1_8()
        elif choice == 9:
            Module_1_9()
        elif choice == 10:
            Module_1_10()
        else:
            print("Invalid choice, please try again.")
    Module()
            
def Module_1_1():
    os.system('cls')
    pi = 3.1416
    radius = float(input("Enter the radius: "))
    volume = (4 / 3) * pi * radius ** 3
    print("The volume of the sphere is:", volume)
    choice = int(input("choice [1] Continue [0] Back: "))
    
    if choice == 0: 
        Module_1()  
    elif choice == 1:
        Module_1_1()
    else:
        print(f"This number {choice} is not recognized")

def Module_1_2():
    os.system('cls')
    num1 = 9
    num2 = 5
    num3 = 32
    C = float(input("Enter the Celsius degree: "))
    F = (num1 / num2) * C + num3
    print("The equivalent of Celsius degree to Fahrenheit is:", F)
    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0: 
        Module_1()  
    elif choice == 1:
        Module_1_2()
    else:
        print(f"This number {choice} is not recognized")

def Module_1_3():
    os.system('cls')
    D = 53.95
    input_amount = float(input("Enter the dollar amount: "))
    total = input_amount * D
    print("The equivalent in dollar to peso is:", total)
    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_1()
    elif choice == 1:
        Module_1_3()
    else:
        print(f"This number {choice} is not recognized")

def Module_1_4():
    os.system('cls')
    cm = 2.54
    inch = float(input("Enter The inch: "))
    total = inch * cm
    print("The equivalent of inch to cm is:", total)
    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_1()
    elif choice == 1:
        Module_1_4()
    else:
        print(f"This number {choice} is not recognized")

def Module_1_5():
    os.system('cls')
    x = int(input("Enter X:"))
    y = int(input("Enter Y:"))
    s = x
    x = y
    y = s
    print("x =", x, "\n y =", y)
    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_1()
    elif choice == 1:
        Module_1_5()
    else:
        print(f"This number {choice} is not recognized")

def Module_1_6():
    os.system('cls')
    pi = 3.1416
    r = float(input("Enter the radius: "))
    c = 2 * pi * r
    print(f"The circumference of the circle is {c}")
    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_1()
    elif choice == 1:
        Module_1_6()
    else:
        print(f"This number {choice} is not recognized")

def Module_1_7():
    os.system('cls')
    x = float(input("Enter the X value: "))
    y = float(input("Enter the Y value: "))
    x = x + y
    y = x - y
    x = x - y
    print("x =", x, ", y =", y)
    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_1()
    elif choice == 1:
        Module_1_7()
    else:
        print(f"This number {choice} is not recognized")

def Module_1_8():
    os.system('cls')
    P = float(input("Enter the purchase price of the item: "))
    Y = float(input("Enter the expected number of years of service: "))
    S = float(input("Enter the expected salvage value of the item: "))
    D = (P - S) / Y
    print("The yearly depreciation is:", D)
    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_1()
    elif choice == 1:
        Module_1_8()
    else:
        print(f"This number {choice} is not recognized")

def Module_1_9():
    os.system('cls')
    num1 = 2
    R = float(input("Enter the yearly production: "))
    S = float(input("Enter the cost per order: "))
    I = float(input("Enter the inventory carrying cost per unit: "))
    EOQ = ((num1 * R * S) / I) ** 0.5
    print("The Economic Order Quantity is:", EOQ)
    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_1()
    elif choice == 1:
        Module_1_9()
    else:
        print(f"This number {choice} is not recognized")

def Module_1_10():
    os.system('cls')
    pi = 3.1416
    r = float(input("Enter the radius: "))
    A = pi * r * r
    print(f"The area of a circle with radius {r} is: {A}")
    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_1()
    elif choice == 1:
        Module_1_10()
    else:
        print(f"This number {choice} is not recognized")


def Module_2():
    os.system('cls')
    print("[1] Module 2.1 Determine Vowel or Consonants")
    print("[2] Module 2.2 Determine Date value")
    print("[3] Module 2.3 Determine Temperature value")
    print("[4] Module 2.4 Determine type of aircraft")
    print("[5] Module 2.5 Determine type of ship")
    print("[6] Module 2.6 Determine Earthquake range")
    print("[7] Module 2.7 Number to words conversion")
    print("[8] Module 2.8 Ordinary numbers to roman numerals")
    print("[9] Module 2.9 Compute and asses tuition fee")
    print("[10] Module 2.10 Grade equivalent")
    print("[0] Back")
    choice = int(input("choose the number: "))
    if choice == 0:
        Module()
    elif choice == 1:
        Module_2_1()
    elif choice == 2:
        Module_2_2()
    elif choice == 3:
        Module_2_3()
    elif choice == 4:
        Module_2_4()
    elif choice == 5:
        Module_2_5()
    elif choice == 6:
        Module_2_6()
    elif choice == 7:
        Module_2_7()
    elif choice == 8:
        Module_2_8()
    elif choice == 9:
        Module_2_9()
    elif choice == 10:
        Module_2_10()
    else:
        print("Invalid choice, please try again.")
def Module_2_1():
    os.system('cls')
    l = input("Enter the letter").lower()
    if l in ("a","e","i","o","u"):
        print("vowels")
    else:
        print("consonant")
    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_2()
    elif choice == 1:
        Module_2_1()
    else:
        print(f"This number {choice} is not recognized")

def Module_2_2():
    os.system('cls')
    month = int(input("Enter month: "))
    days = int(input("Enter days: "))
    year = int(input("Enter Year: "))

    if month == 1:
        print(f"january {days}, {year}")
    elif month == 2:
        print(f"february {days}, {year}")
    elif month == 3:
        print(f"march {days}, {year}")
    elif month == 4:
        print(f"april {days}, {year}")
    elif month == 5:
        print(f"may {days}, {year}")
    elif month == 6:
        print(f"june {days}, {year}")
    elif month == 7:
        print(f"july {days}, {year}")
    elif month == 8:
        print(f"aguast {days}, {year}")
    elif month == 9:
        print(f"september {days}, {year}")
    elif month == 10:
        print(f"october {days}, {year}")
    elif month == 11:
        print(f"november {days}, {year}")
    elif month == 12:
        print(f"december {days}, {year}")
    else:
        print("Invalid month")
    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_2()
    elif choice == 1:
        Module_2_2()
    else:
        print(f"This number {choice} is not recognized")

def Module_2_3():
    os.system('cls')
    temp = int(input("Enter the temp: "))
    if temp < 0:
        print("Ice")
    elif temp >= 0 and temp <= 100:
        print("Water")
    else:
        print("Steam")
    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_2()
    elif choice == 1:
        Module_2_3()
    else:
        print(f"This number {choice} is not recognized")

def Module_2_4():
    os.system('cls')
    kh = int(input("Enter the Kh: "))
    m = int(input("Enter the m: "))

    if kh > 1100 and m > 52:
        print("Civilian Aircraft")
    elif kh < 1100 and m < 52:
        print("Military Aircraft")
    elif kh > 500 and m > 20:
        print("Military Aircraft")
    elif kh < 500 and m < 20:
        print("Its a bird")
    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_2()
    elif choice == 1:
        Module_2_4()
    else:
        print(f"This number {choice} is not recognized")

def Module_2_5():
    os.system('cls')
    letter = input("Choose letter B, C, D, F\nEnter The le [0] Back / [1] Continuetter: ").lower()

    if letter == 'b':
        print("Battleship")
    elif letter == 'c':
        print("Cruiser")
    elif letter == 'd':
        print("Destroyer")
    elif letter == 'f':
        print("Frigate")
    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_2()
    elif choice == 1:
        Module_2_5()
    else:
        print(f"This number {choice} is not recognized")

def Module_2_6():
    os.system('cls')
    N = float(input("Enter The Number: "))

    if N < 5.0:
        print("Little or no damage")
    elif 5.0 <= N < 5.5:
        print("Some Damage")
    elif 5.5 <= N < 6.5:
        print("Serious damage")
    elif 6.5 <= N < 7.5:
        print("Disaster")
    else:
        print("Catastrophe")
    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_2()
    elif choice == 1:
        Module_2_6()
    else:
        print(f"This number {choice} is not recognized")

def Module_2_7():
    os.system('cls')
    number = int(input("Enter the number up to 3000: "))
    if number > 3000:
        print("Cannot handle more than 3000")

    hundreds = number % 1000
    thousands = number - hundreds
    tens = hundreds % 100
    ones = tens % 10
    hundreds -= tens
    tens -= ones

    if thousands == 1000:
        print("one thousand", end=" ")
    elif thousands == 2000:
        print("two thousand", end=" ")
    elif thousands == 3000:
        print("three thousand", end=" ")

    if hundreds == 100:
        print("one hundred", end=" ")
    elif hundreds == 200:
        print("two hundred", end=" ")
    elif hundreds == 300:
        print("three hundred", end=" ")
    elif hundreds == 400:
        print("four hundred", end=" ")
    elif hundreds == 500:
        print("five hundred", end=" ")
    elif hundreds == 600:
        print("six hundred", end=" ")
    elif hundreds == 700:
        print("seven hundred", end=" ")
    elif hundreds == 800:
        print("eight hundred", end=" ")
    elif hundreds == 900:
        print("nine hundred", end=" ")

    if 11 <= tens + ones <= 19:
        if tens + ones == 11:
            print("eleven")
        elif tens + ones == 12:
            print("twelve")
        elif tens + ones == 13:
            print("thirteen")
        elif tens + ones == 14:
            print("fourteen")
        elif tens + ones == 15:
            print("fifteen")
        elif tens + ones == 16:
            print("sixteen")
        elif tens + ones == 17:
            print("seventeen")
        elif tens + ones == 18:
            print("eighteen")
        elif tens + ones == 19:
            print("nineteen")
    else:
    
        if tens == 10:
            print("ten", end=" ")
        elif tens == 20:
            print("twenty", end=" ")
        elif tens == 30:
            print("thirty", end=" ")
        elif tens == 40:
            print("forty", end=" ")
        elif tens == 50:
            print("fifty", end=" ")
        elif tens == 60:
            print("sixty", end=" ")
        elif tens == 70:
            print("seventy", end=" ")
        elif tens == 80:
            print("eighty", end=" ")
        elif tens == 90:
            print("ninety", end=" ")

    
        if ones == 1:
            print("one")
        elif ones == 2:
            print("two")
        elif ones == 3:
            print("three")
        elif ones == 4:
            print("four")
        elif ones == 5:
            print("five")
        elif ones == 6:
            print("six")
        elif ones == 7:
            print("seven")
        elif ones == 8:
            print("eight")
        elif ones == 9:
            print("nine")

    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_2()
    elif choice == 1:
        Module_2_7()
    else:
        print(f"This number {choice} is not recognized")

def Module_2_8():
    os.system('cls')
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

    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_2()
    elif choice == 1:
        Module_2_8()
    else:
        print(f"This number {choice} is not recognized")

def Module_2_9():
    os.system('cls')
    amount = float(input("Enter Tuition Fee Amount: "))

    print("Please Select Payment Plan")
    print("1. Cash")
    print("2. Two Installment")
    print("3. Three Installment")
    print("0. Exit")

    input_choice = int(input("Enter your choice: "))

    discount10Percent = amount * 0.10
    discount5Percent = amount * 0.05
    interest5Percent = amount * 0.05

    if input_choice == 1:
        print("Cash")
        print(f"Your Total Tuition Fee is: {amount - discount10Percent}")
    elif input_choice == 2:
        print("Two Installments")
        print(f"Your Total Tuition Fee is: {amount - discount5Percent}")
    elif input_choice == 3:
        print("Three Installments")
        print(f"Your Total Tuition Fee is: {amount + interest5Percent}")
    elif input_choice == 0:
        print("Thank You for Using the Program")
        print("Exiting the Program")
    else:
        print("Invalid Input Please Try Again")

    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_2()
    elif choice == 1:
        Module_2_9()
    else:
        print(f"This number {choice} is not recognized")

def Module_2_10():
    os.system('cls')
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
    
    choice = int(input("choice [1] Continue [0] Back: "))
    if choice == 0:
        Module_2()
    elif choice == 1:
        Module_2_10()
    else:
        print(f"This number {choice} is not recognized")


def Module_3():
    os.system('cls')
    print("[1] Module 3.1 Calculate looping sequence number")
    print("[2] Module 3.2 Produce Number sequence")
    print("[3] Module 3.3 Produce Number sequence (reverse order)")
    print("[4] Module 3.4 Calculate factorial value")
    print("[5] Module 3.5 Fibonacci  sequence numbers")
    print("[6] Module 3.6 Calculate power value")
    print("[7] Module 3.7 Sum of square of numbers")
    print("[8] Module 3.8 Calculate sum of sequence of numbers")
    print("[9] Module 3.9 Reverse input numbers")
    print("[10] Module 3.10 Sum of power N")

    choice = int(input("Choose the number: "))
    while choice != 0:
        if choice == 1:
            Module_3_1()
        elif choice == 2:
            Module_3_2()
        elif choice == 3:
            Module_3_3()
        elif choice == 4:
            Module_3_4()
        elif choice == 5:
            Module_3_5()
        elif choice == 6:
            Module_3_6()
        elif choice == 7:
            Module_3_7()
        elif choice == 8:
            Module_3_8()
        elif choice == 9:
            Module_3_9()
        elif choice == 10:
            Module_3_10()
        else:
            print("Invalid choice, please try again.")
    Module()
def Module_3_1():
    os.system('cls')
    n = int(input("Enter the number: "))
    for i in range(1, n + 1):
        print(f"{i} * {i} = {(i * i)}")

    choice = int(input("\nEnter choice [0] Back / [1] Continue: "))
    if choice == 0: 
        Module_3()
    elif choice == 1:
        Module_3_1()
    else:
        print(f"This number {choice} is not recognized")

def Module_3_2():
    os.system('cls')
    n = int(input("Enter the number: "))
    x, y = 1, n
    while x < n + 1:
        print(f"{x}{y}", end="")
        x += 1
        y -= 1

    choice = int(input("\nEnter choice [0] Back / [1] Continue: "))
    if choice == 0: 
        Module_3()
    elif choice == 1:
        Module_3_2()
    else:
        print(f"This number {choice} is not recognized")

def Module_3_3():
    os.system('cls')
    n = int(input("Enter the number: "))
    x, y = 1, n
    while x < n + 1:
        print(f"{y}{x}", end="")
        x += 1
        y -= 1

    choice = int(input("\nEnter choice [0] Back / [1] Continue: "))
    if choice == 0: 
        Module_3()
    elif choice == 1:
        Module_3_3()
    else:
        print(f"This number {choice} is not recognized")

def Module_3_4():
    os.system('cls')
    n = int(input("Enter the number: "))
    total = 1
    for i in range(1, n + 1):
        print(f"{i}", end="")
        total *= i
        if i < n:
            print(" * ", end="")
    print(" =", total)

    choice = int(input("\nEnter choice [0] Back / [1] Continue: "))
    if choice == 0: 
        Module_3()
    elif choice == 1:
        Module_3_4()
    else:
        print(f"This number {choice} is not recognized")

def Module_3_5():
    os.system('cls')
    n = int(input("enter the number: "))
    x = 1
    y = 1
    t = 0
    for i in range(1, n):
        t = x + y
        x = y
        y = t
        print(x)

    choice = int(input("\nEnter choice [0] Back / [1] Continue: "))
    if choice == 0: 
        Module_3()
    elif choice == 1:
        Module_3_5()
    else:
        print(f"This number {choice} is not recognized")

def Module_3_6():
    os.system('cls')
    n1 = int(input("Enter base Number: "))
    n2 = int(input("Enter Exponent Number: "))
    total = 1
    for i in range(1, n2 + 1):
        total *= n1
        print(n1, end=" ")
        if i < n2:
            print("*", end=" ")
    print("=", total)

    choice = int(input("\nEnter choice [0] Back / [1] Continue: "))
    if choice == 0: 
        Module_3()
    elif choice == 1:
        Module_3_6()
    else:
        print(f"This number {choice} is not recognized")

def Module_3_7():
    os.system('cls')
    n = int(input("Enter the Number: "))
    total = 0
    for i in range(1, n + 1):
        total += i * i
        print(f"{i}^2", end="")
        if i < n:
            print(" + ", end="")
    print(" =", total)

    choice = int(input("\nEnter choice [0] Back / [1] Continue: "))
    if choice == 0: 
        Module_3()
    elif choice == 1:
        Module_3_7()
    else:
        print(f"This number {choice} is not recognized")


def Module_3_8():
    os.system('cls')
    n = int(input("Enter the number: "))
    total = 0
    for i in range(1, n + 1):
        print(i, end="")
        if i < n:
            print(" + ", end="")
        total += i  
    print(" =", total)

    choice = int(input("\nEnter choice [0] Back / [1] Continue: "))
    if choice == 0: 
        Module_3()
    elif choice == 1:
        Module_3_8()
    else:
        print(f"This number {choice} is not recognized")


def Module_3_9():
    os.system('cls')
    n = int(input("Enter the Number: "))
    for i in range(1, n + 1):
        print(n * "*")

    choice = int(input("\nEnter choice [0] Back / [1] Continue: "))
    if choice == 0: 
        Module_3()
    elif choice == 1:
        Module_3_9()
    else:
        print(f"This number {choice} is not recognized")


def Module_3_10():
    os.system('cls')
    n = int(input("Enter the number: "))
    total = 0
    for i in range(1, n + 1):
        total += i ** i
        print(f"{i}^2", end="")
        if i < n:
            print(" + ", end="")
    print(" =", total)

    choice = int(input("\nEnter choice [0] Back / [1] Continue: "))
    if choice == 0: 
        Module_3()
    elif choice == 1:
        Module_3_10()
    else:
        print(f"This number {choice} is not recognized")

def Activity():
    os.system('cls')
    print("[1] Python First-Program")
    print("[2] Pink-Form")
    print("[3] GWA")
    print("[4] Simple Calculator")
    print("[5] NumberType")
    print("[6] gender_seperation")
    print("[0] Back")
    choice = int(input("Enter the number 0 - 8: "))
    if choice == 1:
        FirstProgram()
    elif choice == 2:
        PinkForm()
    elif choice == 3:
        GWA()
    elif choice == 4:
        SimpleCalculator()
    elif choice == 5:
        NumberType()
    elif choice == 6:
        GenderSeperation()
    elif choice == 0:
        MainProject()
        
def FirstProgram():
    os.system('cls')
    print("Hello World")
def PinkForm():
    os.system('cls')
    print("                                              Immaculate Conception I-College of Arts and Technology                                            ")
    print("┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐")
    print("│ STUDENT NAME         NAME (Last, Given, Middle)                        TERM                             SCHOOL YEAR                          │")
    print("│ 2024-0050-IC         GREGORIO, FRANCO, MIRARZA                           1                                2024-2025                          │")
    print("├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤")
    print("│ COURSE                       SECTION                                  YEAR LEVEL                        ACADEMIC STATUS                      │")
    print("│   BSIS                       BSIS 1-2                                     1                             IRREGULAR                            │")
    print("├──────────────────────────────────────────────────────────────────┬─────────────────────────────────────────┬─────────────────────────────────┤")
    print("│    CLASS IDSUB NO.CODE     TITLE                            UNITS│ TOTAL:                                  │MODE OF PAYMENT                  │")
    print("│                                                                  │                                         │                                 │")
    print("│    BSIS 1-2   C-EN1  PURPOSIVE COMMUNICATION                    3│ Registration Fee                1,000.00│ FULL PAYMENT                    │")
    print("│                                                                  │                                         │                                 │")
    print("│    BSIS 1-2   C-HUM ART APPRECIATION                            3│ Total Tuition Fee              10,500.00│ 1st Payment            15,900.00│")
    print("│                                                                  │                                         │                                 │")
    print("│    BSIS 1-2   CC2    COMPUTER PROGRAMMING 1 (FUND OF            3│ Stud. Dev/Lab/ComSys/Etc            0.00│ 2nd Payment                 0.00│")
    print("│                                                                  │                                         │                                 │")
    print("│    BSIS 1-2   TH 1   SALVATION HISTORY                          3│ Total Misc. Fee                 4,400.00│ 3rd Payment                 0.00│")
    print("│                                                                  │                                         │                                 │")
    print("│    BSIS 1-2   NSTP 1 CWSTS 1                                    3│ Other Fee                           0.00│ 4th Payment                 0.00│")
    print("│                                                                  │                                         │                                 │")
    print("│                                                                  │ AMOUNT DUE                     15,900.00│ 5th Payment                 0.00│")
    print("│                                                                  │                                         │                                 │")
    print("│                                                                  │ Discount Fee                      00.00 │ 6th Payment                 0.00│")
    print("│                                                                  │                                         │                                 │")
    print("│                                                                  │ Other Discount Fee                0.00  │ TOTAL:                          │")
    print("│                                                                  │                                         │                                 │")
    print("│                                                                  │ TOTAL DISCOUNTS                   0.00  │                                 │")
    print("│                                                                  │                                         │                                 │")
    print("│                                                                  │ Special Class                     0.00  │                                 │")
    print("│                                                                  │                                         │                                 │")
    print("│                                                                  │ NET AMOUNT DUE                 15,900.00│                                 │")
    print("│                                                                  │                                         │                                 │")
    print("│                                                                  ├─────────────────────────────────────────┼─────────────────────────────────┤")
    print("│                                                                  │                                         │                                 │")
    print("│                                                                  │ CONTRACT:                               │STUDENT'S NAME & SIGNATURE       │")
    print("│                                                                  │                                         │                                 │")
    print("│                                                                  │  Upon admission at the ICICAT, I hereby │                                 │")
    print("│                                                                  │promise to obey all the existing rules   │                                 │")
    print("│                                                                  │                                         │                                 │")
    print("│                                                                  │and regulation established by the        │                                 │")
    print("├───────────────────────────────────────┬──────────────────────────┤                                         │                                 │")
    print("│ DATE                                  │ TOTAL                    │authorities of this                      │     KEYLYN S.D. ZANO            │")
    print("│       7/09/24                         │                 15       │                                         │                                 │")
    print("|                                       │                          │institution                              │           Assessed By           │")
    print("└───────────────────────────────────────┴──────────────────────────┴─────────────────────────────────────────┴─────────────────────────────────┘")

def GWA():
    os.system('cls')
    CC3 = float(input("Enter CC3 Grade: "))
    NSTP2 = float(input("Enter NSTP2 Grade: "))
    CNS1 = float(input("Enter CNS1 Grade: "))
    CSS2 = float(input("Enter CSS2 Grade: "))
    
    GWAGrandes = (CC3 + NSTP2 + CNS1 + CSS2) / 4
    print(GWAGrandes)
    choice = int(input("\nEnter choice [0] Back / [1] Continue: "))
    if choice == 0: 
        Activity()
    elif choice == 1:
        GWA()
    else:
        print(f"This number {choice} is not recognized")

def SimpleCalculator():
    os.system('cls')
    while True:
        print("Choose Operator")
        print("[1]: ADDITION")
        print("[2]: SUBTRACTION")
        print("[3]: MULTIPLICATION")
        print("[4]: DIVISION")
        print("[0]: Back")
        choice = int(input("Choose Operator: "))
        
        if choice in [1,2,3,4]:
            num1 = float(input("Enter Number 1: "))
            num2 = float(input("Enter Number 2: "))
            num3 = float(input("Enter Number 3: "))
            num4 = float(input("Enter Number 4: "))
            
            if choice == 1:
                print("Total: ", (num1 + num2 + num3 + num4))

            elif choice == 2:
                print("Total: ", (num1 - num2 - num3 - num4))

            elif choice == 3:
                print("Total: ", (num1 * num2 * num3 * num4))

            elif choice == 4:
                 if num2 == 0:
                    print("Division by 0 is not calculated")
                 else:
                     print("Total: ", (num1 / num2 / num3 / num4))
            elif choice == 0:
                Activity()
        else:
            print("please enter the available number")
        choice = int(input("\nEnter choice [0] Back / [1] Continue: "))
        if choice == 0: 
            Activity()
        elif choice == 1:
            SimpleCalculator()
        else:
            print(f"This number {choice} is not recognized")   
        
        
def NumberType():
    os.system('cls')
    n = int(input("Enter the number:"))
    
    if n > 0:
        print("positive")
    elif n < 0:
        print("negative")
    else:
        print("Zero")
    
    choice = int(input("\nEnter choice [0] Back / [1] Continue: "))
    if choice == 0: 
        Activity()
    elif choice == 1:
        SimpleCalculator()
    else:
        print(f"This number {choice} is not recognized")   
def GenderSeperation():
    os.system('cls')
    boys = []
    girls = []
    n = int(input("Enter the number of characters: "))
    for i in range(1, n + 1):
        name = input(f"Enter name #{i}: ").strip().lower()
        if name[0] in ["a", "b", "c"]:
            boys.append(name)
        else:
            girls.append(name)
        print("Girls: ", girls)
        print("Boys: ", boys)
    choice = int(input("\nEnter choice [0] Back / [1] Continue: "))
    if choice == 0: 
        Activity()
    elif choice == 1:
        GenderSeperation()
    else:
        print(f"This number {choice} is not recognized")   
        
MainProject()