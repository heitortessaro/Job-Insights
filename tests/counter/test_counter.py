import pytest
from unittest.mock import mock_open, patch
from src.counter import count_ocurrences


@pytest.fixture
def jobs_text():
    return """ Testing text with 3 Python python PythOn,
            2 Javascript JavaScript and 1 Trybe"""


def test_counter(jobs_text):
    # more about patch:
    # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch
    # quick guide:
    # https://docs.python.org/3/library/unittest.mock.html#quick-guide
    # mock_open:
    # https://docs.python.org/3/library/unittest.mock.html#mock-open
    with patch("builtins.open", mock_open(read_data=jobs_text)):
        assert count_ocurrences("/fake/path/fake.csv", "python") == 3
        assert count_ocurrences("/fake/path/fake.csv", "javascript") == 2
        assert count_ocurrences("/fake/path/fake.csv", "trybe") == 1
