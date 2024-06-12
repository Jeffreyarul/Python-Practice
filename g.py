class Student:
    def __init__(self, regno, name, cgpa):
        self.regno = regno
        self.name = name
        self.cgpa = cgpa

    def get_regno(self):
        return self.regno

    def get_name(self):
        return self.name

    def get_cgpa(self):
        return self.cgpa

    def set_cgpa(self, new_cgpa):
        self.cgpa = new_cgpa

student1 = Student(regno="2021001", name="Alice", cgpa=8.5)
student2 = Student(regno="2021002", name="Bob", cgpa=9.0)

print(f"Student 1 Report:")
print(f"Registration Number: {student1.get_regno()}")
print(f"Name: {student1.get_name()}")
print(f"CGPA: {student1.get_cgpa()}")

print(f"Student 2 Report:")
print(f"Registration Number: {student2.get_regno()}")
print(f"Name: {student2.get_name()}")
print(f"CGPA: {student2.get_cgpa()}")
