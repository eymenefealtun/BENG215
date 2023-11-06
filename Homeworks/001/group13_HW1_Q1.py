my_str = 'TR29abcdqxw10Casd1923yhdf23askdjl04ajdfguj19akflk05ssfıj30lkhu08akdf'

# I created a value to calculate sums of the digits in the my_str.
sum_up = 0
# To calculate the average of the digits I need to find out how many digits in the string. Therefore I created a variable.
counter = 0

# I created a for loop and checked the strings if they're digits.
for i in my_str:
    if i.isdigit() == True:
        # I increase the digit counter by 1, if I found a string
        counter += 1
        # If i is a digit, I add the int value of i to sum_up variable.
        sum_up += int(i)

# I print the sum of the digits in the string.
print("Sum of the digits in the my_str is : {}".format(sum_up))

avg = sum_up / counter

# I print the average of the digits in the string.
print("Average of the digits in the my_str is : {}".format(avg))