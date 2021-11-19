class Human:
    first_name = ''
    last_name = ''
    patronymic = ''
    phone_number = ''

    def __init__(self, first_name, last_name, patronymic, phone_number):
        self.first_name, self.last_name, self.patronymic, self.phone_number = first_name, last_name, patronymic, phone_number

    def get_info(self):
        return f'Описание человека - {self.first_name} {self.last_name} {self.patronymic} {self.phone_number}'

human1 = Human('Anna', 'Prokopchuk', 'Viktorovna', '000 000 00 00')
human2 = Human('Youjin', 'Prokopchuk', 'Pavlovich', '000 000 00 00')
print(human1.get_info())
print(human2.get_info())
