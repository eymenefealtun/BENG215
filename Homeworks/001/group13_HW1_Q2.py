List = ['Ayşe: 75-78', 'Berk: 80-60', 'Can: 58-61', 'Didem: 34-45', 'Erdem: 32-37', 'Fatih: 69-75', 'Gül: 54-63']


def extractStudentNumbersFromList(givenList):
    names = []
    averages = []
    topThree = []

    for i in givenList:
        values = i.split(" ")

        name = values[0][:-1]  # we remove ':' at the end of the name, by adding -1

        examResultString = values[1].split("-")
        examResult1 = int(examResultString[0])
        examResult2 = int(examResultString[1])

        average = (examResult1 + examResult2) / 2

        names.append(name)
        averages.append(average)

    ordinalNumbers = ["st", "nd", "rd"]

    for i in range(3):
        maxAverageIndex = averages.index(max(averages))
        topThree.append(names[maxAverageIndex + i])
        del averages[maxAverageIndex]

        print(f"{i + 1}'{ordinalNumbers[i]} student is {topThree[i]}")

extractStudentNumbersFromList(List)
