def remove_duplicates(string):
    result = ""
    seen = set()
    for char in string:
        if char not in seen:
            seen.add(char)
            result += char
    return result

input_str = input("Enter a string: ")
output_str = remove_duplicates(input_str)
print("String after removing duplicates:", output_str)
