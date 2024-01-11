import main
import re


def __count_letters(password):
    return len([char for char in password if char.isalpha()])


def __count_numbers(password):
    return len([char for char in password if char.isdigit()])


def __count_symbols(password):
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    return len([char for char in password if char in symbols])


def __assert_password_is_random_order(num_letters, num_symbols, num_numbers, password):
    # password should not be ordered by letters, symbols, and numbers. it should be in random order. test will fail if it matches the pattern.
    search = re.search(f"^([A-Za-z]{{{num_letters}}})([!#$%&()*+]{{{num_symbols}}})([0-9]{{{num_numbers}}})$", password)
    assert not search


def test_gen_password_with_four_letters_two_symbols_two_numbers():
    password = main.gen_password(4, 2, 2)
    num_letters, num_symbols, num_numbers = __count_letters(password), __count_symbols(password), __count_numbers(
        password)
    assert num_letters == 4 and num_symbols == 2 and num_numbers == 2
    assert len(password) == 8
    __assert_password_is_random_order(4, 2, 2, password)


def test_gen_password_with_no_letters_two_symbols_two_numbers():
    password = main.gen_password(0, 2, 2)
    num_letters, num_symbols, num_numbers = __count_letters(password), __count_symbols(password), __count_numbers(
        password)
    assert num_letters == 0 and num_symbols == 2 and num_numbers == 2
    assert len(password) == 4
    __assert_password_is_random_order(num_letters, num_symbols, num_numbers, password)


def test_gen_password_with_four_letters_no_symbols_two_numbers():
    password = main.gen_password(4, 0, 2)
    num_letters, num_symbols, num_numbers = __count_letters(password), __count_symbols(password), __count_numbers(
        password)
    assert num_letters == 4 and num_symbols == 0 and num_numbers == 2
    assert len(password) == 6
    __assert_password_is_random_order(num_letters, num_symbols, num_numbers, password)


def test_gen_password_with_four_letters_two_symbols_no_numbers():
    password = main.gen_password(4, 2, 0)
    num_letters, num_symbols, num_numbers = __count_letters(password), __count_symbols(password), __count_numbers(
        password)
    assert num_letters == 4 and num_symbols == 2 and num_numbers == 0
    assert len(password) == 6
    __assert_password_is_random_order(num_letters, num_symbols, num_numbers, password)


def test_gen_password_empty_string():
    password = main.gen_password(0, 0, 0)
    assert password == ""
