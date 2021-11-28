from HW4_1.student import Student
from HW4_1.exceptions import GroupException
from HW4_1.group import Group as ParentGroup


class Group(ParentGroup):

    def add(self, student):
        if len(self.students) == 10:
            raise GroupException('Too much students in class')
        super().add(student)


if __name__ == '__main__':
    group = Group()
    for i in range(11):
        group.add(Student('ivan', 'ivanov', 'ivanovich', '000 000'))