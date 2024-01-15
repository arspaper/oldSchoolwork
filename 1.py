file_path = "files/№1.txt"


num_max = 0
digits = list()

tgt = "ITKLAS"

f = open(file_path).readline()

sequence = list()
sequence_max = 0

for a in f:
    if a.isdigit():
        if len(digits) == 0:
            digits.append(a)
        else:
            if int(digits[0]) % 2 == 0 and int(a) % 2 == 0:  # EVEN
                digits.append(a)
            elif int(digits[0]) % 2 != 0 and int(a) % 2 != 0:  # ODD
                digits.append(a)
    else:
        num_max = max(num_max, len(digits))
        digits = list()

for letter in f:
    if letter in tgt:
        sequence.append(letter)
    else:
        sequence_max = max(sequence_max, len(sequence))
        sequence = list()


print(num_max, sequence_max)
