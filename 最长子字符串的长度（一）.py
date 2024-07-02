def get_max_even_o_substring_length(s):
    # Initialize a counter for the number of 'o' characters
    o_count = 0
  
    # Count the number of 'o' characters in the input string
    for c in s:
        if c == 'o':
            o_count += 1

    # If the count of 'o' is even, the entire string is the longest valid substring
    if o_count % 2 == 0:
        return len(s)
    else:
        # If the count of 'o' is odd, remove one character to make it even
        return len(s) - 1

# Read the input string
s = input()

# Get the result and print it
print(get_max_even_o_substring_length(s))
