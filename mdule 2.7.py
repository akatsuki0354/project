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
    print("M")
elif thousands == 2000:
    print("MM")
elif thousands == 3000:
    print("MMM")

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
