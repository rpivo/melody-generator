from src.main import generate_melody, get_random_number_between_zero_and_eight, get_zero_or_eight

# generate_melody()


def test_generate_melody_returns_a_list():
    result = generate_melody()
    assert isinstance(result, list)


def test_generate_melody_returns_a_list_containing_eight_numbers():
    result = generate_melody()
    assert len(result) == 8


# get_random_number_between_zero_and_eight()


def test_get_random_number_between_zero_and_eight_returns_an_integer():
    result = get_random_number_between_zero_and_eight()
    assert type(result) is int


def test_get_random_number_between_zero_and_eight_returns_an_integer_greater_than_or_equal_to_zero():
    result = get_random_number_between_zero_and_eight()
    assert result >= 0


def test_get_random_number_between_zero_and_eight_returns_an_integer_less_than_or_equal_to_eight():
    result = get_random_number_between_zero_and_eight()
    assert result <= 8


# get_zero_or_eight()


def test_get_zero_or_eight_returns_an_integer():
    result = get_zero_or_eight()
    assert type(result) is int


def test_get_zero_or_eight_returns_either_zero_or_eight():
    result = get_zero_or_eight()
    assert result == 0 or result == 8
