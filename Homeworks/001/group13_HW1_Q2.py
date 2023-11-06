List = ['Ayşe: 75-78', 'Berk: 80-60', 'Can: 58-61', 'Didem: 34-45', 'Erdem: 32-37', 'Fatih: 69-75', 'Gül: 54-63']

names = []
averages = []
topThree = []

for i in List:
    # splitting name and number part
    values = i.split(" ")

    # we remove ':' at the end of the name, by adding -1
    name = values[0][:-1]

    # splitting two different number
    examResultString = values[1].split("-")
    examResult1 = int(examResultString[0])
    examResult2 = int(examResultString[1])

    average = (examResult1 + examResult2) / 2

    # appending the current name to our list
    names.append(name)
    # appending average to our list
    averages.append(average)

ordinalNumbers = ["st", "nd", "rd"]

for i in range(3):
    # finding the index of the maximum number from the averages list
    maxAverageIndex = averages.index(max(averages))
    # appending the name to topThree list, using maxAverageIndex inside the names list
    topThree.append(names[maxAverageIndex + i])
    # deleting max number from the averages list in order to find the next maximum number
    del averages[maxAverageIndex]

    print(f"{i + 1}'{ordinalNumbers[i]} student is {topThree[i]}")
