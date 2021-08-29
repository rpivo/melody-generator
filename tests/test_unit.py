from src.main import generate_melody, get_random_number_between_zero_and_seven, get_zero_or_seven

# generate_melody()


def test_generate_melody_returns_a_list():
    result = generate_melody()
    assert isinstance(result, list)


def test_generate_melody_returns_a_list_containing_eight_numbers():
    result = generate_melody()
    assert len(result) == 8


def test_generate_melody_returns_a_list_with_the_first_item_being_either_zero_or_seven():
    result = generate_melody()
    assert result[0] == 0 or result[0] == 7


# get_random_number_between_zero_and_seven()


def test_get_random_number_between_zero_and_seven_returns_an_integer():
    result = get_random_number_between_zero_and_seven()
    assert type(result) is int


def test_get_random_number_between_zero_and_seven_returns_an_integer_greater_than_or_equal_to_zero():
    result = get_random_number_between_zero_and_seven()
    assert result >= 0


def test_get_random_number_between_zero_and_seven_returns_an_integer_less_than_or_equal_to_seven():
    result = get_random_number_between_zero_and_seven()
    assert result <= 7


# get_zero_or_seven()


def test_get_zero_or_seven_returns_an_integer():
    result = get_zero_or_seven()
    assert type(result) is int


def test_get_zero_or_seven_returns_either_zero_or_seven():
    result = get_zero_or_seven()
    assert result == 0 or result == 7
