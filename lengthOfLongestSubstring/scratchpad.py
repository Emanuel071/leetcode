
string = "abcabcbb"
current_char = ''
char_count = 0
max_count = 0


for i in range(len(string)):
    if string[i] != current_char:
        current_char = string[i]
        char_count = 1
    else:
        char_count += 1
    if char_count > max_count:
        max_count = char_count  
print("Max count of consecutive characters:", max_count)
