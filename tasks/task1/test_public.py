import pytest

from .task import find_new_map


class Case:
    def __init__(self, name: str, n: int, old_capital: int, new_capital: list,
                 old_map: list, new_map: list):
        self._name = name
        self.n = n
        self.old_capital = old_capital
        self.new_capital = new_capital
        self.old_map = old_map
        self.new_map = new_map

    def __str__(self) -> str:
        return 'task1_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=3,
        old_capital=2,
        new_capital=3,
        old_map=[2, 2],
        new_map=[2, 3],
    ),
    Case(
        name='base2',
        n=6,
        old_capital=2,
        new_capital=4,
        old_map=[6, 1, 2, 4, 2],
        new_map=[6, 4, 1, 4, 2],
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = find_new_map(
        n=case.n,
        old_capital=case.old_capital,
        new_capital=case.new_capital,
        old_map=case.old_map,
    )
    assert answer == case.new_map
