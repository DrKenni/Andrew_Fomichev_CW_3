from src.utils import *
from src.main import FILE_TRANSACTION


def test_get_inf():
    assert type(get_inf(FILE_TRANSACTION)) == list


