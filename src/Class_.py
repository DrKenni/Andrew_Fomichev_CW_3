from datetime import datetime


class Transaction():

    def __init__(self, id_trans, date_trans, state, amount, description, to, currency, from_anyone=None):
        self.id_trans = id_trans
        self.date = date_trans
        self.state = state
        self.amount = amount
        self. description = description
        self.to = to
        self.currency = currency
        self.from_anyone = from_anyone

    def __repr__(self):
        """Описание Класса"""
        return "Класс выводящий данные на основе файла json с историей транзакций"

    def __str__(self):
        return "Транзакция"

    def get_id(self):
        """id операции"""
        return self.id_trans

    def get_date(self):
        return self.date

    def get_information(self):
        return (f"{self.date} {self.description}\n"
                f"{self.from_anyone} -> {self.to}\n"
                f"{self.amount} {self.currency}\n")

    def chenge_date(self):
        day_trans = datetime.fromisoformat(self.date)
        return f"{day_trans.day}.{day_trans.month}.{day_trans.year} в {day_trans.hour}:{day_trans.minute}"




