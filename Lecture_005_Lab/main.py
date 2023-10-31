def example_pen_money():
    pens = ['black', 'red', 'blue', 'green']
    numberOfPens = [7, 9, 8, 6]
    price = [10, 12, 7, 9]
    t_price = 0
    count = 0
    iterations = 0
    for i in range(len(pens)):
        for j in range(numberOfPens[i]):
            t_price += price[i]
            if (t_price <= 200):
                count += 1
                print(f"Student bought {pens[i]} pen for {str(price[i])} liras")
                print(f'Student bought {str(count)} pens')
                print(f'total price {str(t_price)}')
            else:
                break


# example_pen_money()


# write a script to find the numbers which are  multple of 7 and multiple of 5 but not 3
def example_02():
    validNumbers = []
    for i in range(1000):
        if (i % 7 == 0 and i % 5 == 0 and i % 3 != 0):
            validNumbers.append(i)

    for valid in validNumbers:
        print(valid)

    print("Number of valid ones: " + str(len(validNumbers)))

example_02()
