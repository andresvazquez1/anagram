print("*"*20)
print("Anagram checker")
print("*"*20)

first_str = input("Enter the first string:")
second_str = input("Enter the second string:")

first_str = [c for c in first_str.lower() if c.isalpha()]
second_str = [c for c in second_str.lower() if c.isalpha()]

is_anagram = sorted(first_str) == sorted(second_str) \
    if first_str or second_str else False

print("The strings are anagrams." if is_anagram else "The strings are not anagrams.")
