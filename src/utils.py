import json


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



