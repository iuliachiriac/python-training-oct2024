def my_func():
    """Simple function printing a message"""
    print("hello world")


print(my_func.__doc__, my_func.__name__, type(my_func), sep=" / ")


def get_greeting():
    return "hello world"


greeting = get_greeting()
print(greeting + "!")


# nr is a required argument / step is a default/optional argument
def decrement(nr, step=1):
    return nr - step


print(decrement(10))
print(decrement(10, 2))  # call with positional arguments
print(decrement(10, step=2))
print(decrement(step=2, nr=10))  # call with keyword arguments


def varargs(*args, name="N/A", **kwargs):
    print(args, type(args))
    print(name)
    print(kwargs, type(kwargs), end="\n\n")


varargs()
varargs(10)
varargs(10, 20, 30, 40, name="Anna")

varargs(age=20, height=1.8)
varargs(10, 20, 30, 40, name="Anna", age=20, height=1.8)

l = [100, 10, 10.4, 'hello', 3, 5]
varargs(l)
varargs(*l)

person = {'name': 'Jane', 'age': 62}
varargs(**person)  # varargs(name="Jane", age=62)
