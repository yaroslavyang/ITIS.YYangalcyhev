class Subscriber:
    def __init__(self, surname="", name="", middle_name="", birthday="01.01.0000", sex="",
                 connection_date="01.01.0000", balance=0, tariff=""):
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.birthday = birthday
        self.sex = sex
        self.connection_date = connection_date
        self.balance = balance
        self.tariff = tariff

    def __str__(self):
        return f'Фамилия: {self.surname}\n' \
               f'Имя: {self.name}\n' \
               f'Отчество: {self.middle_name}\n' \
               f'Дата рождения: {self.birthday}\n' \
               f'Пол: {self.sex}\n' \
               f'Дата подключения: {self.connection_date}\n' \
               f'Баланс: {self.balance}\n' \
               f'Тариф: {self.tariff}\n'

sub = Subscriber("Иванов", "Иван", "Иванович", "01.01.2000", sex="М", connection_date="22.06.2021", balance=347,
                 tariff="Базовый")
print(str(sub))