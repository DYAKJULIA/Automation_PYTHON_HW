import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# ПОЗИТИВНОЕ ТЕСТИРОВАНИЕ


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("    skypro", "skypro"),
    ("  hello world", "hello world"),
    ("        python", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("skypro", "s", True),
    ("hello world", "s", False),
    ("1python1", "1", True),
])
def test_contains_positive(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("skypro", "s", "kypro"),
    ("hello world", " world", "hello"),
    ("1python1", "1", "python"),
])
def test_delete_symbol_positive(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected


# НЕГАТИВНОЕ ТЕСТИРОВАНИЕ

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "skypro"),
    ("", ""),
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("", "", True),
    ("   ", " ", True),
    ("", " ", False),
])
def test_contains_positive(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("", "", ""),
    ("   ", " ", ""),
    ("phyton", " ", "phyton"),
])
def test_delete_symbol_positive(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected
