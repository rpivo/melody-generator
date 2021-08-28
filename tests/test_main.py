from src.main import generate_melody


def test_generate_melody():
    result = generate_melody()
    assert result == [0, 0, 0, 0, 0, 0, 0, 0]
