from string_utils import StringUtils
string_utils = StringUtils()


def test_capitalize():
# Позитивные проверки:
    assert string_utils.capitalize("skypro") == "Skypro"
    assert string_utils.capitalize("  hello") == "  hello"
    assert string_utils.capitalize("535")

# Негативный проверки:
    assert string_utils.capitalize("") == ""
    assert string_utils.capitalize("  ") == "  "
    assert string_utils.capitalize("1234xz") == "1234xz"


def test_delete_symbol_negative():
    assert string_utils.delete_symbol("SkyPro", "z") == "SkyPro"
    assert string_utils.delete_symbol("", "o") == ""
    assert string_utils.delete_symbol("SkyPro", "1234") == "SkyPro"
