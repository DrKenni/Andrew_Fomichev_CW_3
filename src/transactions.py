class Transactions():
    """Создает экземпляры с данными о транзакции"""
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
        return f"Транзакция №{self.id_trans}"

    def __str__(self):
        return "Транзакция"

    def get_id(self):
        """id транзакции"""
        return self.id_trans

    def get_date(self):
        """Дата транзакции"""
        return self.date

    def get_information(self):
        """Выводит информанию на основе полученных данных о транзакции"""
        return (f"{self.date} {self.description}\n"
                f"{self.from_anyone} -> {self.to}\n"
                f"{self.amount} {self.currency}\n\n")
