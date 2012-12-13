import random
import string

file = open("generated_data.csv", "w")
letter_array = [c for c in string.lowercase]

for i in range(1, 10000):
    random.shuffle(letter_array)
    pattern = letter_array[:random.randint(8, 12)]
    label = random.randint(0,1)
    pattern.append(str(label))
    file.write(",".join(pattern)+"\n")
