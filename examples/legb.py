X = 100


def my_func(a):
    b = 2

    # define variable at local level with the same name as global variable
    # it's still shadowing, still not recommended
    # X = 1

    # change global variable
    # global X
    # X = 0

    def inner(c):
        d = 22

        # shadowing name from outer scope
        # a = 0

        # changing value for a variable from outer scope
        # nonlocal a
        # a = 0

        print("=== inside inner ===")
        print("Local names:", c, d)
        print("Enclosing names:", a, b, inner)
        print("Global names:", X, my_func, MyClass)
        print("Built-in names:", len, int, None, NameError)

    inner(11)

    print("=== inside my_func ===")
    print("Local names:", a, b, inner)
    print("Global names:", X, my_func, MyClass)
    print("Built-in names:", len, int, None, NameError)


class MyClass:
    pass


if __name__ == "__main__":
    # sum = 0  # shadowing is not recommended

    my_func(1)
    # print(a, b, inner)  # cannot access local names outside function

    print("=== global ===")
    print("Global names:", X, my_func, MyClass)
    print("Built-in names:", len, int, None, NameError)
