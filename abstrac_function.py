def print_stars():
    n = int(input("Enter a number: "))
    for i in range(n):
        print("*" * (i + 1))

def reverse_string(word) -> str:
    return word[::-1]

def reverse_string_concat(s1 : str, s2 : str):
    return reverse_string(s1) + reverse_string(s2)

def loop_gen_string(s : str, n : int):
    for _ in range(n):
        print(f"The new string generated is {s} with {n} loops")

# 3
# print_stars()
# 4
word = input("Enter a word: ")
# a
# print(reverse_string(word))
secondWord = input("Enter a second word: ")
# b
# print(reverse_string_concat(word, secondWord))
# c
nLoops = int(input("Enter number of loops: "))
loop_gen_string(reverse_string_concat(word, secondWord), nLoops)