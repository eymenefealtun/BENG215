def example():
    for d in range(3, 11):
        print(d)


# example()

def example_break():
    for i in range(3, 11):
        break
        print('dolar yine arrtti')
        if i == 5:
            print('dolar cildirdi:', i)
        elif i == 7:
            print('Dolar nereye:', i)
        else:
            print(f'Dolar {i} lira oldu!:')


# example_break()

def example_continue():
    for i in range(0, 6):
        if (i == 3):
            continue
        print(f'Number of people: {i}')


# example_continue()

def example_list():
    total = 0
    people = 0
    donations = [123, 54, 12, 6, 2, 45, 745, 8678, 23]
    for amount in donations:
        people += 1
        total += amount
        if total >= 1000:
            print('enough amount of donation collected')
            break
        print(f'Total donated amount is now {total}')


# example_list()


def example_motif_finder():
    def example_generate_random_sequence():
        import random
        seq = ''
        bases = ['A', 'T', 'G', 'C']
        for i in range(0, 1000):
            seqi = random.randint(0, 3)
            seq = seq + bases[seqi]
        return seq

    TF_motif = 'ATGC'
    seq_list = []
    for j in range(5):
        seq_list.append(example_generate_random_sequence())

    print(seq_list)
    k = 0
    for j in seq_list:
        motif_count = 0
        k += 1
        for i in range(len(j)):
            if (TF_motif == j[i:i + len(TF_motif)]):
                motif_count += 1
                print('Seq NO: ', k)
                print(f'Motif no: {motif_count}')
                print('found a bindig site at position', i)


# example_motif_finder()

def example_find_method():
    val = ['abc', 'bbc', 'ddd']
    print(val[0].find("bc"))

#example_find_method()
