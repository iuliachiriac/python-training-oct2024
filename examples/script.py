"""This module exemplifies basic Python concepts"""

print("hello world")

x = 5
print(x + 7)
print(x)

# explicit line joining (using "\")
command = "/Users/iulia/PycharmProjects/python-training-oct2024/.venv/bin/py" \
          "thon /Users/iulia/PycharmProjects/python-training-oct2024/script.py "
print(command)

# implicit line joining
print(
    'apples',
    'bananas',
    'oranges',
    'pears',
    'peaches',
    'cherries',
)

# if x > 10:
#     print("greater than 10")

triple_quote_str = """Newlines
included"""
print(triple_quote_str)

print("She said \"hello\"")
print("Backslash must be escaped with itself to be included in a string: \\")
print("Newline: \ntest")
