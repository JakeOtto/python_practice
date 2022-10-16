# why pytest found no tests

import pytest

MESSAGE = """
    You are running `pytest` in the wrong directory.
    If you are trying to run the drills tests, do this:
    ; cd drills
    ; pytest
    If you are trying to run the program tests, do this:
    ; cd program
    ; pytest
"""    


def test_wrong_dir():
    pytest.fail(MESSAGE)

