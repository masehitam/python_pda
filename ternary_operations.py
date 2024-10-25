a = 3
b = 2
print("A") if a > b else print("=") if a == b else print("B")

x = "welcome"
try:
    #if condition returns False, AssertionError is raised:
    assert x == "hello", "x should be 'hello'"
except:
    print("error boi")
