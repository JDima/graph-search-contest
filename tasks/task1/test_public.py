import math
import pytest

from .task import find_new_map


class Case:
    def __init__(self, name: str, n: int, old_capital: int, new_capital: int,
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
    Case(
        name='base3',
        n=5,
        old_capital=2,
        new_capital=3,
        old_map=[2, 1, 2, 2],
        new_map=[3, 1, 2, 2],
    ),
    Case(
        name='base4',
        n=5,
        old_capital=2,
        new_capital=5,
        old_map=[2, 1, 2, 2],
        new_map=[2, 5, 1, 2],
    ),
    Case(
        name='base5',
        n=2,
        old_capital=1,
        new_capital=2,
        old_map=[1],
        new_map=[2],
    ),
    Case(
        name='base6',
        n=6,
        old_capital=2,
        new_capital=2,
        old_map=[6, 1, 2, 4, 2],
        new_map=[6, 1, 2, 4, 2],
    ),
    Case(
        name='base7',
        n=4,
        old_capital=3,
        new_capital=2,
        old_map=[3, 3, 3],
        new_map=[3, 2, 3],
    ),
    Case(
        name='base8',
        n=8,
        old_capital=2,
        new_capital=4,
        old_map=[2, 6, 1, 6, 2, 1, 7],
        new_map=[4, 1, 6, 6, 2, 1, 7],
    ),
    Case(
        name='base9',
        n=9,
        old_capital=3,
        new_capital=8,
        old_map=[2, 3, 3, 3, 3, 6, 7, 8],
        new_map=[2, 3, 6, 3, 3, 7, 8, 8],
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
