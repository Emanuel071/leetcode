sample = "CCCACCCC"
sample2 = "AAAAAGGG"
given = 4


dictonary_of_letters = {}

for i in range(len(sample)):
    print(f"i: {i}, sample[i]: {sample[i]}")

    if sample[i] not in dictonary_of_letters:
        dictonary_of_letters[sample[i]] = 1
    else:
        dictonary_of_letters[sample[i]] += 1

for j in dictonary_of_letters:
    print(f"j: {j}")
    if dictonary_of_letters[j] <= given:
        sample = sample.replace(j, '')
print(dictonary_of_letters)