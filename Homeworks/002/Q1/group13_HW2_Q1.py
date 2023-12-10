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
    requested_gene = ""
    requested_aminoacide_region = []

    # finding start codone index
    for i in range(0, len(given_rna_sequence),3):
        cur_seq = given_rna_sequence[i:i + 3]
        if cur_seq == start_codon:
            start_codon_index = i
            break
    # finding stop codone index
    for i in range(start_codon_index, len(given_rna_sequence),3):
        cur_seq = given_rna_sequence[i:i + 3]
        if cur_seq in stop_codons:
            stop_codon_index = i + 3
            break

    requested_gene = given_rna_sequence[start_codon_index:stop_codon_index]

    # creating the aminoacide from the dictionary
    for i in range(0, len(requested_gene),3):
        cur_seq = requested_gene[i:i+3]
        requested_aminoacide_region.append(given_codon_aminoacide_dict[cur_seq.upper()])

    f = open("../Q1/ResultFile.txt", "a")
    f.truncate(0)
    for i in requested_aminoacide_region:
        f.write(i+" ")
    f.close()


    print(f"requested gene: {requested_gene}")
    print(f"requested aminoacide: {requested_aminoacide_region}")


handleGene()
