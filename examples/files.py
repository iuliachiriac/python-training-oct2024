with open("comparisons.py", "r") as f:
    for line in f:
        print(line, end="")


with open("out.txt", "a+") as f:
    f.write("hello\n")
    f.write("hello world\n")
    f.writelines(["hi\n", "bye\n"])

    f.seek(0)
    print(f.read())
