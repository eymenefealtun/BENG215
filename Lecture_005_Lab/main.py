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


# example_02()

def example_03_splitting_to_list():
    tempList = input("Enter list of names:").split(" ")

    for i in range(len(tempList)):
        print(f"name {i}:{tempList[i]}")


# example_03_splitting_to_list()


def example_generate_random_sequence():
    import random
    seq = ''
    bases = ['A', 'T', 'G', 'C']
    for i in range(0, 1000):
        seqi = random.randint(0, 3)
        seq = seq + bases[seqi]
    return seq


def example_04_CpG_island_finder():
    seq = example_generate_random_sequence()
    window_size = 50
    slide_size = 5
    CpG_threshold = 0.1
    print(seq)
    for i in range(0, len(seq), slide_size):
        CpG_count = seq[i:i + window_size].count('CG')
        CpG_fraction = CpG_count / window_size
        if CpG_fraction > CpG_threshold:
            print(f'CpG island found at position {i}, Fraction {CpG_fraction}')


# example_04_CpG_island_finder()


def example_05_gene_finder():
    seq = example_generate_random_sequence()
    print(seq)
    start_codon = 'ATG'
    stop_codons = ['TAG', 'TAA', 'TGA']
    result_gene = ''

    for i in range(len(seq)):
        if (start_codon == seq[i:i + len(start_codon)]):
            gene_start_position = i
            print(f'Gene found at position {i}')
            for j in range(gene_start_position, len(seq), 3):
                if (seq[j:j + len(start_codon)] in stop_codons):
                    gene_stop_position = j
                    print(f'Gene is coded up to position {gene_stop_position}')
                    result_gene = seq[gene_start_position:gene_stop_position + len(start_codon)]
                    return result_gene
            break


# example_05_gene_finder()


def example_06_CpG_island_finder_inside_gene():
    seq = example_generate_random_sequence()
    start_codon = 'ATG'
    stop_codons = ['TAG', 'TAA', 'TGA']
    result_gene = ''

    for i in range(len(seq)):
        if (start_codon == seq[i:i + len(start_codon)]):
            gene_start_position = i
            for j in range(gene_start_position, len(seq), 3):
                if (seq[j:j + len(start_codon)] in stop_codons):
                    gene_stop_position = j
                    result_gene = seq[gene_start_position:gene_stop_position + len(start_codon)]

    window_size = 50
    slide_size = 5
    CpG_threshold = 0.1
    numberOfIslandFound = 0
    print(result_gene)
    for i in range(0, len(result_gene), slide_size):
        CpG_count = result_gene[i:i + window_size].count('CG')
        CpG_fraction = CpG_count / window_size
        if CpG_fraction > CpG_threshold:
            numberOfIslandFound += 1
            print(f'CpG island found at position {i} inside of the given gene, Fraction {CpG_fraction}')
    if numberOfIslandFound == 0:
        print('no island was found inside of the given gene')


# example_06_CpG_island_finder_inside_gene()

def example_guess_the_name():
    name = 'Anakin'
    guess = input('Write the name you think that true:')
    pos = 0

    while guess != name and pos < len(name):
        print("Nope, that's not it young Padawan! Hint: letter ", end='')
        print(pos + 1, " is", name[pos] + ". ", end='')
        guess = input("Guess again:")
        pos += 1

    if pos == len(name) and name != guess:
        print("Too bad, you couldn't get it. The name was", name + "." + "You cannot be a Jedi :(")
    else:
        print("\nGreat you got it in", pos + 1, "quesses! May the Force be with you!")


# example_guess_the_name()


def example_probability_game():
    ballDictionary = {'blue': 7, 'red': 7, 'green': 7}

    def get_number_of_item_by_color(color):
        return (list(ballDictionary.values())[list(ballDictionary.keys()).index(color)])

    requestedBallColour = input('What color is the ball you just drew from the bag?')
    prob = 0

    while (requestedBallColour != 'quit' and sum(list(ballDictionary.values())) > 0):
        if (requestedBallColour.lower() == 'blue' and get_number_of_item_by_color('blue') != 0):
            prob = get_number_of_item_by_color('blue') / sum(list(ballDictionary.values()))
            print(f'Selection: {requestedBallColour} | probability: {prob}')
            ballDictionary['blue'] -= 1
        elif (requestedBallColour.lower() == 'red' and get_number_of_item_by_color('red') != 0):
            prob = get_number_of_item_by_color('red') / sum(list(ballDictionary.values()))
            print(f'Selection: {requestedBallColour} | probability: {prob}')
            ballDictionary['red'] -= 1
        elif (requestedBallColour.lower() == 'green' and get_number_of_item_by_color('green') != 0):
            prob = get_number_of_item_by_color('green') / sum(list(ballDictionary.values()))
            print(f'Selection: {requestedBallColour} | probability: {prob}')
            ballDictionary['green'] -= 1
        elif (requestedBallColour.lower() == 'quit'):
            break
        else:
            print('Please draw a ball in another colour!')
        requestedBallColour = input('What color is the ball you just drew from the bag?')

example_probability_game()
