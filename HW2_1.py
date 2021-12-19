class Human:
    first_name = ''
    last_name = ''
    patronymic = ''
    phone_number = ''

    def __init__(self, first_name, last_name, patronymic, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.phone_number = phone_number

    def get_info(self):
        return f'Описание человека - {self.first_name} {self.last_name} {self.patronymic} {self.phone_number}'

human1 = Human('Anna', 'Prokopchuk', 'Viktorovna', '000 000 00 00')
human2 = Human('Youjin', 'Prokopchuk', 'Pavlovich', '000 000 00 00')

if __name__ == '__main__':
    print(human1.get_info())
    print(human2.get_info())

