import pytest

from tasks.standart.variables.deposit import calculate_deposit


@pytest.mark.parametrize(
    "summa, years, expected", [
        (123, 2, 148),
        (1000, 5, 1610),
        (1500, 3, 1996),
    ]
)
def test_cockroach_speed(summa, years, expected):
    assert int(calculate_deposit(summa, years)) == expected
