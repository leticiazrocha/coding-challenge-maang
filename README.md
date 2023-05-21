# Intern (Software Engineer) - Coding Challenge - MAANG company

## Challenge Description

### Aim
Create an in-memory store which can store ranges of integers with an associated colour and return a colour
for a given integer.

### Success Criteria
Create an implementation to a standard which represents how I code with proof that my code works.

## Solution Notes
### Requirements Ticklist
| Requirement              | Status  | Notes                                                                                                                                                                                                                          |
|--------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| main.py                  | &#9745; | Runs the examples provided on the challenge instructions.                                                                                                                                                                      |
| `store()`                | &#9745; | Transforms the function parameters (strings) into new formats (tuples and all upper case strings), and append both to a list of dictionaries in state.py.                                                                      |
| `get()`                  | &#9745; | Transforms the function parameter (string) into an integer, and checks if it falls within the stored ranges in state.py.<br/> If it does, the function returns a colour according to the priority. Otherwise, it returns GREY. |
| Unit Tests for `store()` | &#9745; | Tests valid inputs, invalid colour and invalid number format.                                                                                                                                                                  |
| Unit Tests for `get()`   | &#9745; | Tests valid input, invalid input, empty list (GREY is returned) and priority colour given range overlap.                                                                                                                       |

### How to Run
#### Considerations
I successfully ran this script on a macOS machine with Python 3.8 - the following instructions assumes you have either
a Linux or macOS with Python 3.8 (or above) installed.

To run the examples as per the instructions I was given, run the following commands:
```shell
pip install -r requirements.txt | pip3 install -r requirements.txt

python -m pytest -v | python3 -m pytest -v

python src/main.py | python3 src/main.py
```
