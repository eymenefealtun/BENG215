import random

codon_aminoacide_dict = {}
rna_sequence = ""
start_codon = "aug"
stop_codons = ["uaa", "uag", "uga"]

with open("../Resources/codon-aa-list.txt") as file:
    file.readline()  # reading first line in order not to add the "Aminoacide" and "Codone" strings into our dictionary
    while line := file.readline():
        curret_codon = line.split()[0]
        current_aminoacid = line.split()[1]
        codon_aminoacide_dict[curret_codon] = current_aminoacid
with open("../Resources/seq.txt") as file:
    while line := file.readline():
        curret_line = line.split()
        for i in range(1, len(curret_line)):
            rna_sequence += curret_line[i]

start_codon_index = 0
stop_codon_index = 0


def handleGene(given_codon_aminoacide_dict=codon_aminoacide_dict, given_rna_sequence=rna_sequence):
    requested_aminoacide_region = []
    start_codon_index = 0
    stop_codon_index = 0

    # finding start codone index
    for i in range(0, len(given_rna_sequence), 3):
        cur_seq = given_rna_sequence[i:i + 3]
        if cur_seq == start_codon:
            start_codon_index = i
            break
    # finding stop codone index
    for i in range(start_codon_index, len(given_rna_sequence), 3):
        cur_seq = given_rna_sequence[i:i + 3]
        if cur_seq in stop_codons:
            stop_codon_index = i + 3
            break

    requested_gene = given_rna_sequence[start_codon_index:stop_codon_index]

    requested_aminoacide_region = createAminoacide(requested_gene, given_codon_aminoacide_dict)

    return requested_aminoacide_region, requested_gene

def createAminoacide(requested_gene, given_codon_aminoacide_dict):
    # creating the aminoacide from the dictionary
    requested_aminoacide_region = []
    for i in range(0, len(requested_gene), 3):
        cur_seq = requested_gene[i:i + 3]
        requested_aminoacide_region.append(given_codon_aminoacide_dict[cur_seq.upper()])

    f = open("../Q1/ResultFile.txt", "a")
    f.truncate(0)
    for i in requested_aminoacide_region:
        f.write(i + " ")
    f.close()
    return requested_aminoacide_region

random_mutation_point = random.randint(0, len(handleGene(codon_aminoacide_dict, rna_sequence)[1]) - 1)

def give_random_letter(givenLetter):
    letter_list = ["a", "u", "g", "c"]
    last_list = letter_list.remove(givenLetter)
    temp = letter_list[random.randint(0, len(letter_list) - 1)]
    return temp


def missense_mutation(mutation_point=random_mutation_point, given_rna_sequence=rna_sequence,given_codon_aminoacid_dict=codon_aminoacide_dict):

    rna_sequence = handleGene(given_codon_aminoacid_dict, given_rna_sequence)[1]
    aminoacide_gene = createAminoacide(rna_sequence, given_codon_aminoacid_dict)

    mutated_rna_sequence = rna_sequence[0:random_mutation_point] + give_random_letter(rna_sequence[mutation_point]) + rna_sequence[random_mutation_point + 1: len(rna_sequence)]
    mutated_aminoacide_gene = createAminoacide(mutated_rna_sequence, given_codon_aminoacid_dict)

    # print("aminoacide gene         :", aminoacide_gene)
    # print("mutated aminoacide gene :", mutated_aminoacide_gene)
    # print(aminoacide_gene == mutated_aminoacide_gene)
    # print("rna sequence            :", rna_sequence)
    # print("mutated rna sequence    :", mutated_rna_sequence)
    # print(rna_sequence == mutated_rna_sequence)

    print(f"r.{mutation_point}{rna_sequence[random_mutation_point]}>{mutated_rna_sequence[random_mutation_point]} ")

    for i in range(len(aminoacide_gene)):
        if aminoacide_gene[i] != mutated_aminoacide_gene[i]:
            print(f"p.{aminoacide_gene[i]}{i}{mutated_aminoacide_gene[i]} ")
            return
    print("aminoacide gene is have not changed")


missense_mutation()
