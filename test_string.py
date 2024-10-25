string1 = "hello"
string2 = "hello"
string3 = "world"

print(string1 == string2)  # Output: True
print(string1 == string3)  # Output: False
print(string1 < string3)  # Output: True (because 'h' comes before 'w' in alphabetical order)

nama = "wiwid"
nama = "mas" + nama
print(nama)

s1 = "itb u rock"
s2 = "i rule itb"
if len(s1) == len(s2):
    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                print("common letter" + char1)
                break


def get_data(aTuple):
    nums = () # tuples
    words = ()
    for t in aTuple:
        nums = nums + (t[0],) # append
        if t[1] not in words:
            words = words + (t[1],) # append
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    print(nums)
    print(words)
    return (min_n, max_n, unique_words)


print(get_data(((1, "a"), (2, "b"), (3, "c"), (4, "d"), (5, "e"), (6, "f"), (7, "g"), (8, "h"), (9, "i"), (10, "j"))))