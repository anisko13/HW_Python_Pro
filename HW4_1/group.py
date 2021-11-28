class Group:
    students = []  # [1, 2, 3]
                   # 0-1 1-2 2-3

    def add(self, student):
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