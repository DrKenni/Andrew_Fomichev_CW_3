import json
from Class_ import Transaction
from datetime import datetime


def get_inf(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        trans_list = json.load(f)
        return trans_list


def filtering_list(trans_list):
    """ возвращает отсортированный по дате список с 5
    последними выполненными операциями """
    # фильтр списка по "EXECUTED"
    executed_list = [item for item in trans_list if item.get('state') == 'EXECUTED']
    # сортировка по дате
    sorted_list = sorted(executed_list, key=lambda x: x.get('date'), reverse=True)
    return sorted_list[:5]


def make_return(last_five_trans):
    processed_trans = []
    def check_from(where):
        bank_account = "Вклад"
        try:
            num_wallet = operation[where]
            if num_wallet[:4] == "Счет":
                bank_account = f"{num_wallet[:4]} **{num_wallet[-4:]}"
            else:
                bank_account = f"{num_wallet[:-12]} {num_wallet[-12:-10]}** **** {num_wallet[-4:]}"
            return bank_account
        except:
            return bank_account

    for operation in last_five_trans:

        try:
            id_trans = operation["id"]
            state = operation["state"]
            date_full = datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f")
            date_trans = datetime.strftime(date_full, "%d.%m.%Y")
            description = operation["description"]
            from_anyone = check_from("from")
            to = check_from("to")
            amount = operation["operationAmount"]["amount"]
            currency = operation["operationAmount"]["currency"]["name"]
            transaction = Transaction(id_trans, date_trans, state, amount, description, to, currency, from_anyone)
            processed_trans.append(transaction)
        except:
            continue
    return processed_trans


def print_(operations_list):
    for operation in operations_list:
        print(operation.get_information())