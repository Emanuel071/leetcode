string = "abcabcbb"  # Example string
max_count = 0       # Longest sequence of same character
current_count = 0   # Length of current sequence
current_char = ''   # The character we are currently counting

for char in string:
    if char == current_char:
        # Same character as before, increment count
        current_count += 1
    else:
        # New character found
        current_char = char  # Start counting the new character
        current_count = 1     # Reset count to 1 for the new character

    # Update max_count if current sequence is longer
    if current_count > max_count:
        max_count = current_count

print("Max count of consecutive characters:", max_count)