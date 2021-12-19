from HW2_2 import Student, student1


class Group:
    students = []  # [1, 2, 3]
                   # 0-1 1-2 2-3

    def add(self, student: Student):
        self.students.append(student)

    def delete(self, index):
        self.students.pop(index)

    def get_student_by_last_name (self, last_name):
        for student in self.students:
            if last_name == student.last_name:
                return student
        return


    def __str__(self):
        result = ''
        for student in self.students:
            result += student.__str__() + '\n'
        return result

group1 = Group()
group1.add(student1)
group1.add(Student('ivan', 'ivanov', 'ivanovich', '000 000'))

if __name__ == '__main__':
    print(group1)
    print(group1.get_student_by_last_name('Prokopchuk'))
    print(group1.get_student_by_last_name('Dziuba'))
    group1.delete(0)
    print(group1.get_student_by_last_name('Prokopchuk'))

