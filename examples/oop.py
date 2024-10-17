from datetime import date


class Person:
    count = 0  # class variable

    def __init__(self, name, date_of_birth):
        self.name = name  # instance variable
        self.date_of_birth = date_of_birth
        Person.count += 1

    def greet(self, greeting):  # instance method
        print(f"{greeting.capitalize()}! I am {self.name}.")


if __name__ == "__main__":
    p1 = Person("Anna", date(2005, 5, 1))
    p2 = Person("Mike", date(1981, 6, 12))

    print(p1.name, p1.date_of_birth)
    print(p2.name, p2.date_of_birth)

    print(Person.count, p1.count, p1.count is Person.count)

    p1.greet("hi")
    p2.greet("hello")
