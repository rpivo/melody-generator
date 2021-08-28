from src.main import generate_melody


def test_generate_melody_returns_a_list():
    result = generate_melody()
    assert isinstance(result, list)
