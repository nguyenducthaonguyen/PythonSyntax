class Student(object):
    def __init__(self, id: int, name: str, age: int, address: str):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
    def __str__(self):
        return f'{self.id} {self.name} {self.age} {self.address}'

class StudentManager(object):
    def __init__(self):
        self.students = []


    def add(self, student):
        self.students.append(student)

    def find_by_id(self, id):
        for student in self.students:
            if student.id == id:
                return student
        return None

    def remove(self, id):
        student = self.find_by_id(id)
        if student:
            self.students.remove(student)
            print(f"removed {student.name}")
            return student
        else:
            print("student not found")
            return None

    def update(self, student):
        student_data = self.find_by_id(student.id)
        if student_data:
            student_data.name = student.name
            student_data.age = student.age
            student_data.address = student.address
            print(f"updated {student.name}")
            return True
        else:
            print("student not found")
            return False

    def find_all(self):
        for student in self.students:
            print(student)

def main():
    manager = StudentManager()
    manager.add(Student(1, "Nguyen", 28, "Da Nang"))
    manager.add(Student(2, "Phuc", 31, "Quang Nam"))
    manager.add(Student(3, "Nguyen", 28, "Da Nang"))
    manager.find_all()
    manager.remove(1)
    manager.find_all()
    manager.update(Student(2, "Minh", 28, "Da Nang"))
    manager.find_all()

if __name__ == "__main__":
    main()


