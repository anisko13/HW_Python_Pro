from HW2_2 import Student
from HW2_3 import Group as ParentGroup


class GroupException(Exception):
    pass


class Group(ParentGroup):

    def add(self, student: Student):
        if len(self.students) == 10:
            raise GroupException('Too much students in class')
        super().add(student)


if __name__ == '__main__':
    group = Group()
    for i in range(11):
        group.add(Student('ivan', 'ivanov', 'ivanovich', '000 000'))
