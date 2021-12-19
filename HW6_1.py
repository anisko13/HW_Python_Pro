from HW2_2 import Student
from HW2_3 import Group as ParentGroup


class GroupIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index = self.index + 1
            return self.wrapped[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


class Group(ParentGroup):
    def __iter__(self):
        return GroupIterator(self.students)


if __name__ == '__main__':
    group = Group()
    for i in range(11):
        group.add(Student('ivan', 'ivanov', 'ivanovich', '000 000'))
    for student in group:
        print(student)
