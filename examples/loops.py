x = 10

while x <= 20:
    print(x)
    x += 1  # x = x + 1

print("After while:", x)


greeting = "hello"
for character in greeting:

    print(character)

for byte in greeting.encode("utf-8"):  # iterating on bytes object
    if byte > 105:
        break
    print(byte)

for nr in range(10, 21, 3):
    if nr == 13:
        continue
    print(nr)
