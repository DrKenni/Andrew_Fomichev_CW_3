import os
from src.utils import *
# Абсолютный путь до json файла
ROOT_FILE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_TRANSACTION = os.path.join(ROOT_FILE, "data", 'operations.json')


def main():
    """Основной код программы"""
    trans_list_all = get_inf(FILE_TRANSACTION)
    last_five_trans = filtering_list(trans_list_all)
    processed_trans = make_return(last_five_trans)
    print_(processed_trans)


if __name__ == "__main__":
    main()
