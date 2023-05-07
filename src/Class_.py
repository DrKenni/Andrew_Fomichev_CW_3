

class Transaction():

    def __init__(self, id_trans, date, state, amount, description, from_anyone, to):
        self.id_trans = id_trans
        self.date = date
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




