import pytest

from src.modules.get import get
from src.modules.store import store
from src.modules.state import UNFILTERED_LIST


def test_get_valid_input():
    """
    Tests if a valid number format was passed correctly
    """
    UNFILTERED_LIST.clear()

    store("02-05", "BLUE")
    store("35-60", "RED")
    store("11-20", "YelloW")

    assert get('19') == 'YELLOW'
    assert get('99') == 'GREY'
    assert get('55') == 'RED'


def test_empty_list_grey():
    """
    Tests if the function returns GREY when the given number is outside all colour ranges
    """
    UNFILTERED_LIST.clear()

    store("02-05", "BLUE")
    store("35-60", "RED")
    store("11-20", "YelloW")

    assert get('01') == 'GREY'


def test_get_sorted_list():
    """
    Tests if the function applies a priority colour in case of range overlap
    """
    UNFILTERED_LIST.clear()

    store("02-20", "BLUE")
    store("15-60", "YellOW")
    store("79-99", "RED")

    assert get('16') == 'YELLOW'


def test_get_invalid_input():
    """
    Tests if the function raises an error in case an invalid input is passed
    """
    with pytest.raises(Exception):
        get('1')
        get('1a')
        get('999')
        get('')


