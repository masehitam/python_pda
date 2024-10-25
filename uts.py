def dict_list(L, n: int):
    numbers = {}
    for i in L:
        try:
            e = int(i)
            if e < n:
                if numbers.get(e) is None:
                    numbers[e] = 1
                else:
                    numbers[e] += 1
        except:
            print("e is not a number")

    return (numbers, len(numbers))


print(dict_list([1, 2, 3, 'e', 2, 3, 1, 3, 4, 5], 4))


def sum_digit(x: int) -> int:
    if x < 10:
        return x

    return int(str(x)[-1]) + sum_digit(int(str(x)[:-1]))

def sum_digit2(x: int) -> int:
    if x == 0:
        return 0

    return (x % 10) + sum_digit(x // 10)

print(sum_digit(75))    # Output: 12
print(sum_digit(123))   # Output: 6
print(sum_digit(2222))  # Output: 8
