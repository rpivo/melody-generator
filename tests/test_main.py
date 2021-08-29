from src.main import generate_melody, get_random_number_between_one_and_eight


def test_generate_melody_returns_a_list():
    result = generate_melody()
    assert isinstance(result, list)


def test_generate_melody_returns_a_list_containing_eight_numbers():
    result = generate_melody()
    assert len(result) == 8


def test_get_random_number_between_one_and_eight_returns_an_integer():
    result = get_random_number_between_one_and_eight()
    assert type(result) is int
