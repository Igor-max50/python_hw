import pytest
from string_utils import StringUtils
string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("t_vod, t_result",[
    ("hello", "Hello"),
    ("Hello", "Hello"),
    ("hello my friends", "Hello my friends")
])
def test_positive_capitalize(t_vod, t_result):
    capital = StringUtils()
    assert capital.capitalize(t_vod) == t_result

@pytest.mark.negative
@pytest.mark.parametrize("t_vod, t_result", [
    (" ", " "),
    ("123fa", "123fa"),
    ("", "")
])
def test_negative_capitalize(t_vod, t_result):
    capital = StringUtils()
    assert capital.capitalize(t_vod) == t_result
#--------------------------------------------------------------------------------------------------

@pytest.mark.positive
@pytest.mark.parametrize("t_vod, t_result",[
    ("   123", "123"),
    ("   Hello", "Hello"),
    ("  friends", "friends")
])
def test_positive_trim(t_vod, t_result):
    tri = StringUtils()
    assert tri.trim(t_vod) == t_result

@pytest.mark.negative
@pytest.mark.parametrize("t_vod, t_result",[
    ("123", "123"),
    ("Hello", "Hello"),
    ("friends", "friends")
])
def test_negative_trim(t_vod, t_result):
    tri = StringUtils()
    assert tri.trim(t_vod) == t_result

#-------------------------------------------------------------------------------------------------------

def test_contains_positive():
# Позитивные проверки:
    assert string_utils.contains("Skypro", "S") == True
    assert string_utils.contains("Hello", "H") == True
    assert string_utils.contains("friends", "f") == True

def test_contains_negative():
# Негативные проверки:
    assert string_utils.contains("Skypro", "g") == False
    assert string_utils.contains("Skypro", "f") == False
    assert string_utils.contains("Skypro", "d") == False

#-----------------------------------------------------------------------------------------------------


@pytest.mark.parametrize("t_vod, t_result, expected_output", [
    ("SkyPro", "k", "SyPro"),
    ("hello world", "l", "heo word"),
    ("12345", "2", "1345"),
    ("apple pie", "p", "ale ie")
])
def test_delete_symbol_positive(t_vod, t_result, expected_output):
    res = string_utils.delete_symbol(t_vod, t_result)
    assert res == expected_output


@pytest.mark.parametrize("t_vod, t_result, expected_output", [
    ("    ", "k", "    "),
    ("SkyPro", "d", "SyPro"),
    ("", "l", ""),
])
def test_delete_symbol_negative(t_vod, t_result, expected_output):
    res = string_utils.delete_symbol(t_vod, t_result)
    assert res == expected_output