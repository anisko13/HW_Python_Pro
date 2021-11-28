class Human:
    first_name = ''
    last_name = ''
    patronymic = ''
    phone_number = ''

    def __init__(self, first_name, last_name, patronymic, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.phone_number = first_name, last_name, patronymic, phone_number

    def get_info(self):
        return f'Описание человека - {self.first_name} {self.last_name} {self.patronymic} {self.phone_number}'


class Student(Human):

    def get_info(self):
        return f'Описание студента - {self.first_name} {self.last_name} {self.patronymic} {self.phone_number}'

    def __str__(self):
        return f'Описание студента - {self.first_name} {self.last_name} {self.patronymic} {self.phone_number}'
