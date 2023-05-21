import pytest

from src.modules.state import UNFILTERED_LIST
from src.modules.store import store


def test_store_valid_inputs():
    """
    Tests if a valid colour range format and colour were passed correctly
    """
    UNFILTERED_LIST.clear()

    store("00-05", "BLUE")
    store("11-20", "YELLOW")
    store("11-20", "YelloW")

    assert len(UNFILTERED_LIST) == 3
    assert UNFILTERED_LIST[0] == {"colour": "BLUE", "colour_range": (0, 5)}
    assert UNFILTERED_LIST[1] == {"colour": "YELLOW", "colour_range": (11, 20)}


def test_store_wrong_colour():
    """
    Tests if a valid number format but an invalid colour won't be added to the memory store, and if an error is raised
    """

    UNFILTERED_LIST.clear()

    with pytest.raises(Exception):
        store("00-03", "VIOLET")
        assert len(UNFILTERED_LIST) == 0


def test_store_wrong_number_format():
    """
    Tests if an invalid number format and invalid colour won't be added to the memory store, and if an error is raised
    """
    UNFILTERED_LIST.clear()

    with pytest.raises(Exception):
        store("00-100", "BLUE")
        assert len(UNFILTERED_LIST) == 0
