class Person():
    def __init__(self, first_name, last_name, hobbies=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.hobbies = hobbies

        def __str__(self):
            return f"{self.first_name} {self.last_name}"


person1 = Person("Miles", "Morales", "run, ski, soccer, code")

print(
    person1.hobbies)
