my_str = 'TR29abcdqxw10Casd1923yhdf23askdjl04ajdfguj19akflk05ssfıj30lkhu08akdf'

def handleDigitsInsideString(givenString):
    sum = 0
    numberOfDigit = 0
    average = 0

    for i in givenString:
        if (i.isdigit()):
            numberOfDigit += 1
            sum += int(i)

    average = sum / numberOfDigit

    print(f"sum: {sum}")
    print(f"average: {average}")

handleDigitsInsideString(my_str)
