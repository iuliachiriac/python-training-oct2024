import random
from datetime import date


class Person:
    count = 0  # class variable
    MIN_YEAR = 1900

    def __init__(self, name, date_of_birth):
        self.name = name  # instance variable
        self.date_of_birth = date_of_birth
        self._increment_count()

    @property
    def date_of_birth(self):  # getter
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):  # setter
        if not (isinstance(value, date) and value.year >= self.MIN_YEAR):
            raise ValueError("Invalid date of birth.")
        self._date_of_birth = value

    @property
    def age(self):
        return self.years_since(self.date_of_birth)

    @classmethod
    def _increment_count(cls):  # class method
        cls.count += 1

    @staticmethod
    def years_since(date_start):  # static method
        today = date.today()
        years = today.year - date_start.year
        if (date_start.month, date_start.day) > (today.month, today.day):
            years -= 1
        return years

    def greet(self, greeting, end="\n"):  # instance method
        print(f"{greeting.capitalize()}! I am {self.name}.", end=end)

    def __str__(self):
        return (f"{self.__class__.__name__} object ({self.name}; "
                f"{self.date_of_birth})")

    def __lt__(self, other):
        return self.date_of_birth > other.date_of_birth


class Student(Person):
    count = 0

    def __init__(self, name, date_of_birth, university):
        super().__init__(name, date_of_birth)
        self.university = university

    def greet(self, greeting):
        super().greet(greeting, end=" ")
        print(f"I study at {self.university}.")

    def get_grade(self, subject):
        return random.randint(2, 10)


if __name__ == "__main__":
    p1 = Person("Anna", date(2005, 5, 1))
    p2 = Person("Mike", date(1981, 6, 12))

    print(p1.name, p1.date_of_birth)
    print(p2.name, p2.date_of_birth)

    try:
        p2.date_of_birth = date(1884, 5, 1)
    except ValueError as ex:
        print(ex)
    print("Date of birth is unchanged:", p2.date_of_birth)

    p1.name = "Jane"  # set attribute
    print(p1.name)  # get attribute
    # del p1.name  # del attribute

    print(Person.count, p1.count, p1.count is Person.count)

    p1.greet("hi")
    p2.greet("hello")

    print(p1.__dict__)
    print(p1, str(p1), repr(p1))

    print(f"{p1.name} is younger than {p2.name}:", p1 < p2)

    print(Person.years_since(date(1918, 12, 1)))
    print(f"{p1.name}'s age is:", p1.age)

    s1 = Student("Anna Smith", date(2001, 8, 12), "MIT")
    s1.greet("hello")
    print(s1, s1.age, s1.university)
    print(f"{s1.name} got a {s1.get_grade('History')} in History.")

    print(Person.count, Student.count)

    print(isinstance(s1, Student),
          isinstance(s1, Person),
          issubclass(Student, Person),
          issubclass(Student, object))

    attr = "age"
    if hasattr(s1, attr):
        print(getattr(s1, attr))
