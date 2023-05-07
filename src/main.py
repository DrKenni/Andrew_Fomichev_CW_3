import os
from utils import *

DATA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_TRANSACTION = os.path.join(DATA, "data", 'operations.json')


def main():
    try:
        trans_list_all = get_inf(FILE_TRANSACTION)
        last_five_trans = filtering_list(trans_list_all)
        processed_trans = make_return(last_five_trans)
        print_(processed_trans)
    except FileNotFoundError:
        print("Файл не найден")


if __name__ == "__main__":
    main()
