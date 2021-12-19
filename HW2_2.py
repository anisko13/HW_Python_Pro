from HW2_1 import Human


class Student(Human):

    def get_info(self):
        return f'Описание студента - {self.first_name} {self.last_name} {self.patronymic} {self.phone_number}'
    def __str__(self):
        return f'Описание студента - {self.first_name} {self.last_name} {self.patronymic} {self.phone_number}'



student1 = Student('Yana', 'Prokopchuk', 'Viktorovna', '000 000 00 00')


if __name__ == '__main__':
    print(student1.get_info())