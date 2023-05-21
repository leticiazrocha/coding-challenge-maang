import re
from src.modules.state import COLOURS, UNFILTERED_LIST


def get(num_range: str) -> str:
    """
    The function returns a colour based on the chosen ranges according to the colour priority. If new ranges are
    appended and an overlap occurs, the function might update the colour returned as per priority.
    """
    # Transform the string 'num_range' into an integer if format '00' is correct
    try:
        assert re.match(r"\d{2}$", num_range)
        num_range = int(num_range)
        filtered_list = []

        for item in UNFILTERED_LIST:
            # Check if the num_range is in the colour_range and append colour
            if item['colour_range'][0] <= num_range <= item['colour_range'][1]:
                filtered_list.append(item['colour'])

        # Returns GREY if no colour is appended
        if len(filtered_list) == 0:
            return "GREY"
        else:
            # Sort filtered_list according to the dictionary 'COLOURS' priority
            sorted_list = sorted(
                filtered_list,
                key=lambda colour: COLOURS[colour],
                reverse=False
            )
            return sorted_list[0]
    except AssertionError as get_error:
        raise Exception(f'Invalid input format, {get_error}')
