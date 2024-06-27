class Person:
    def __init__(self, name) -> None:
        self.name = name

    def greet(self):
        print(f"Hallo mein Name ist {self.name}")

class Student(Person):
    def __init__(self, name, mat_id) -> None:
        super().__init__(name)
        self.mat_id = mat_id

    def greet(self):
        print(f"Hallo ich bin {self.name} und meine MatNr ist {self.mat_id}")

if __name__ == "__main__":
    s : Person = Person("Franz")
    s2 : Person = Student("Maria", "007")
    s.greet()
    s2.greet()