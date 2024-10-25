def do_math_operations():
    a = int(input("input positive number for a:"))
    b = int(input("input positive number for b:"))
    if a > 0 and b > 0:
        if a > 10:
            if b < 10:
                print(a + b)
            else: # b >= 10:
                print(a / b)
        else: # a <= 10
            if b < 10:
                print(a - b)
            else:
                print(a * b)
    else:
        print(f"Input number {a} and {b} is invalid!")


def do_something_else():
    a = int(input("input positive number for a:"))
    b = int(input("input number for b:"))
    result = a
    while b > 0:
        if b > a:
            result += b
        else:
            result -= b
        b = int(input("input number for b:"))

    print(result)
# soal a
do_math_operations()
# soal b
do_something_else()