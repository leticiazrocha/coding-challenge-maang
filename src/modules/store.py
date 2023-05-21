import re
from src.modules.state import COLOURS, UNFILTERED_LIST


def store(colour_range: str, colour: str):
    """
    When the function is called, it checks if the arguments are valid and have correct formats.
    Then, it appends each of the transformed inputs (range and upper case 'colour' string) to a list of dictionaries
    without considering colour priorities.
    """
    try:
        # Check if 'colour_range' is in a valid format using RegEx
        assert re.match(r"\d{2}-\d{2}$", colour_range)

        # Check if 'colour' is valid and is in 'COLOURS' dictionary
        assert colour.upper() in COLOURS.keys()

        # Transform the 'colour_range' string into a tuple of 2 integers if format is correct
        colour_range = tuple(map(int, colour_range.split('-')))
        colour = colour.upper()

        # Append 'colour_range' and 'colour' to an unfiltered dictionary
        UNFILTERED_LIST.append({
            'colour': colour,
            'colour_range': colour_range
        })
    except AssertionError as store_error:
        raise Exception(f'Invalid input format, {store_error}')
