class Buyer:
    first_name = ''
    last_name = ''
    patronymic = ''
    phone_number = ''

    def __init__(self, first_name, last_name, patronymic, phone_number):
        self.first_name, self.last_name, self.patronymic, self.phone_number = first_name, last_name, patronymic, phone_number

    def __str__(self):
        return f'Покупатель - {self.first_name} {self.last_name} {self.patronymic} {self.phone_number}'

buyer1 = Buyer('Anna', 'Prokopchuk', 'Viktorovna', '000 000 00 00')
buyer2 = Buyer('Youjin', 'Prokopchuk', 'Pavlovich', '000 000 00 00')

if __name__ == '__main__':
    print(buyer1,'\n', buyer2)