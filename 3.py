file_path = "files/№3.txt"

tgt = "POLIKARPOV"

f = open(file_path).readline()

sequence = list()
sequence_max = 0

for letter in f:
    if letter in tgt:
        sequence.append(letter)
    else:
        count_r = sequence.count("R")
        sequence_max = max(sequence_max, len(sequence)) if count_r > 1 else sequence_max
        sequence = list()


print(sequence_max)
