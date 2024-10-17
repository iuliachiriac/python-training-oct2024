import functools


def make_pretty(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        print('I got decorated')
        return func(*args, **kwargs)

    return inner_func


@make_pretty
def ordinary():
    print("I am ordinary")

# Decorating with @ is syntactic sugar for:
# ordinary = make_pretty(ordinary)  # ordinary = make_pretty.<locals>.inner_func


ordinary()  # make_pretty.<locals>.inner_func()


@make_pretty
def greet(name):
    print(f"Hello, {name}!")


greet("Anna")  # make_pretty.<locals>.inner_func("Anna")


@make_pretty
def decrement(nr, step=1):
    """Decrements nr by step"""
    return nr - step


result = decrement(10, step=2)  # make_pretty.<locals>.inner_func(10, step=2)
print("Decrement result:", result)

print("Function names:", decrement.__name__, greet.__name__)
help(decrement)
