def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count

text = "Hello, World!"
print("Number of vowels:", count_vowels(text))

#B
def reverse_string(input_string):
    return input_string[::-1]

text = "Hello, World!"
reversed_text = reverse_string(text)
print("Reversed string:", reversed_text)
