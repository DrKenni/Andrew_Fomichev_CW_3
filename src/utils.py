import json
from src.transactions import Transactions
from datetime import datetime


def get_inf(json_file):
    """Открывет json фаил и преобразует его в Python словарь
    json_file - путь до файла
    :return - словарь с транзакциями пользоватеря
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        trans_list = json.load(f)
        return trans_list


def filtering_list(trans_list):
    """Возвращает отсортированный по дате список с 5
    последними выполненными операциями
    trans_list - словарь с транзакциями пользоватеря
    :return - список выполненых транзакций и отсортированных по дате
    """
    # фильтр списка по "EXECUTED"
    executed_list = [item for item in trans_list if item.get('state') == 'EXECUTED']
    # сортировка по дате
    sorted_list = sorted(executed_list, key=lambda x: x.get('date'), reverse=True)
    return sorted_list[:5]


def make_return(last_five_trans):
    """Создает экземпляры транзакций,
    обрабатывает данные и переводит в читаемый формат
    last_five_trans: список выполненых транзакций и отсортированных по дате
    :return - список с экземплярами класса Transaction
    """
    processed_trans = []
    def check_from(where):
        """Подфункция шифрующая номера карт и счетов,
        проверяет на наличие отправителя "from"
         """
        bank_account = "Вклад в"
        try:
            num_wallet = operation[where]
            if num_wallet[:4] == "Счет":
                bank_account = f"{num_wallet[:4]} **{num_wallet[-4:]}"
            else:
                bank_account = f"{num_wallet[:-12]} {num_wallet[-12:-10]}** **** {num_wallet[-4:]}"
            return bank_account
        except:
            return bank_account
    # создаю экземпляры класса
    for operation in last_five_trans:

        try:
            id_trans = operation["id"]
            change_date = datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f")
            date_trans = datetime.strftime(change_date, "%d.%m.%Y")
            state = operation["state"]
            amount = operation["operationAmount"]["amount"]
            description = operation["description"]
            to = check_from("to")
            from_anyone = check_from("from")
            currency = operation["operationAmount"]["currency"]["name"]
            transaction = Transactions(id_trans, date_trans, state, amount, description, to, currency, from_anyone)
            processed_trans.append(transaction)
        except:
            continue
    return processed_trans


def print_(operations_list):
    """Итерируется по классам списка и выводит информацию о транзакции"""
    for operation in operations_list:
        print(operation.get_information())