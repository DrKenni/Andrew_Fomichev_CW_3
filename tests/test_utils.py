import src.transactions
from src.utils import *
from src.main import FILE_TRANSACTION


def test_get_inf():
    assert type(get_inf(FILE_TRANSACTION)) == list


def test_filtering_list():
    trans_list = get_inf(FILE_TRANSACTION)
    assert type(filtering_list(trans_list)) == list

    for trans in filtering_list(trans_list):
        assert type(trans) == dict
        assert trans['state'] == "EXECUTED"


def test_make_return():
    trans_list = get_inf(FILE_TRANSACTION)
    filt_list = filtering_list(trans_list)
    for item in make_return(filt_list):
        assert type(item) is src.transactions.Transactions

    assert make_return(filt_list)[0].get_id() == 863064926
    assert make_return(filt_list)[0].get_date() == "08.12.2019"
    assert make_return(filt_list)[0].get_information() == ('08.12.2019 Открытие вклада\n'
                                                            'Вклад в -> Счет **5907\n'
                                                            '41096.24 USD\n')
    assert str(make_return(filt_list)[0]) == "Транзакция"
    assert make_return(filt_list)[0].__repr__() == f"Транзакция №863064926"

