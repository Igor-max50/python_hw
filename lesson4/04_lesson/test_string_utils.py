import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# ---------------------------------------------------------------------------------------------------------

@pytest.fixture
def utils():
    return StringUtils()

@pytest.mark.parametrize("input_string, symbol, count, expected_output", [
    ("aaaabbbb", "a", 2, "aabbbb"),  # Удаляем 'a' дважды
    ("hello world", "l", 3, "heo word"),  # Удаляем 'l' трижды
    ("banana", "a", 2, "bnna")  # Удаляем 'a' дважды
])
def test_delete_symbol_count_positive(utils, input_string, symbol, count, expected_output):
    result = input_string
    for _ in range(count):
        result = utils.delete_symbol(result, symbol)
    assert result == expected_output


# -------------------------------------------------------------------------------------------------
# Позитивный тест
@pytest.mark.positive
def test_delete_symbol_positive(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result
    # Позитивные проверки:
    assert string_utils.delete_symbol("skypro", "s") == "kypro"

# Негативный тест
@pytest.mark.negative
def test_delete_symbol_negative(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result
    assert string_utils.delete_symbol("skypro", "s") == "skypro"

# ------------------------------------------------------------------------------------------

# Позитивный тест
@pytest.fixture
def utils():
    return StringUtils()

# Например, проверим удаление одного символа
@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("SkyPro", "k", "SyPro"),  # Пример из документации
    ("hello world", "l", "heo word"),  # Удаляем все 'l'
    ("12345", "2", "1345"),  # Удаляем цифру '2'
    ("apple pie", "p", "ale ie")  # Удаляем 'p'
])
def test_delete_symbol_positive(utils, input_string, symbol, expected_output):
    result = utils.delete_symbol(input_string, symbol)
    assert result == expected_output
