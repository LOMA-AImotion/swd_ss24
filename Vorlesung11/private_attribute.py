class StudyCourse:
    def __init__(self, name, students) -> None:
        self.__students = students 
        self.name = name

    def add_student(self, mat_nr : str):
        self.__students.append(mat_nr)

    def __repr__(self) -> str:
        return f"{self.name}: {self.__students}"

if __name__ == "__main__":
    swd = StudyCourse("SWD", ["a", "b", "c"])
    print(swd)
    print(swd.name)
    swd.name = "MAT1"
    #print(swd.__students)
    # das funktioniert nicht: swd.__students.append("e")
    swd.add_student("d")
    print(swd)