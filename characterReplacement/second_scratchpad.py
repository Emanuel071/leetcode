sample = "CCCACCCC"
sample2 = "AAAAAGGG"
given = 4

current_char = ''   # The character we are currently seing

for i in range(len(sample)):
    current_char = sample[i]
    print(f"i: {i}, sample[i]: {sample[i]}, current_char: {current_char}")
    

