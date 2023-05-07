from datetime import datetime

class Transaction():

    def __init__(self, id_trans, date_trans, state, amount, description, to, from_anyone=None):
        self.id_trans = id_trans
        self.date = date_trans
        self.state = state
        self.amount = amount
        self. description = description
        self.to = to
        self.from_anyone = from_anyone

    def __repr__(self):
        """Описание Класса"""
        return "Класс выводящий данные на основе файла json с историей транзакций"

    def __str__(self):
        return "Транзакция"

    def get_id(self):
        """id операции"""
        return self.id_trans

    def hide_numb(self):
        list_ = self.to.split(" ")
        for i in list_:
            if i.isalpha():
                print(i, end=" ")
            else:
                if len(i) > 16:
                    return f"**{i[-4:]}"
                else:
                    return f"{i[:-12]} {i[-12:-10]}** **** {i[-4:]}"

    def chenge_date(self):
        day_trans = datetime.fromisoformat(self.date)
        return f"{day_trans.day}.{day_trans.month}.{day_trans.year} в {day_trans.hour}:{day_trans.minute}"


today = Transaction(12341234, "2019-01-05T00:52:30.108534", "EXECUTED", {"amount": "92688.46", "currency": {"name": "USD", "code": "USD"}}, "Открытие вклада", "Счет 49304996510329747621")

print(today.hide_numb())

