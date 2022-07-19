import pytest

from tasks.hard.delete_brackets import shortener


@pytest.mark.parametrize(
    "text, expected", [
        ('Падал(лишнее (лишнее) лишнее) прошлогодний снег (лишнее)', 'Падал прошлогодний снег'),
        ('(лишнее(лишнее))Падал прошлогодний (лишнее(лишнее(лишнее)))снег', 'Падал прошлогодний снег'),
    ]
)
def test_count_words(text, expected):
    assert shortener(text) == expected