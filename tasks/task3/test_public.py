import math
import pytest

from .task import build_home_path


class Case:
    def __init__(self, name: str, n: int, m: int, old_path: list,
                 new_path: list):
        self._name = name
        self.n = n
        self.m = m
        self.old_path = old_path
        self.new_path = new_path

    def __str__(self) -> str:
        return 'task3_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=3,
        m=3,
        old_path=[1, 2, 3, 1],
        new_path=[1, 3, 2, 1],
    ),
    Case(
        name='base2',
        n=3,
        m=3,
        old_path=[1, 3, 2, 1],
        new_path=None,
    ),
    Case(
        name='base3',
        n=4,
        m=4,
        old_path=[1, 2, 4, 3, 1],
        new_path=[1, 3, 4, 2, 1]
    ),
    Case(
        name='base5',
        n=10,
        m=17,
        old_path=[1, 2, 5, 10, 9, 6, 3, 2, 4, 8, 10, 7, 6, 1, 3, 4, 5, 8, 7, 9, 1],
        new_path=[1, 2, 5, 10, 9, 6, 3, 2, 4, 8, 10, 7, 6, 1, 9, 7, 8, 5, 4, 3, 1]
    ),
    Case(
        name='base5',
        n=12,
        m=18,
        old_path=[1, 3, 6, 8, 9, 10, 11, 7, 4, 3, 2, 6, 9, 12, 10, 7, 5, 4, 1],
        new_path=[1, 3, 6, 8, 9, 10, 11, 7, 4, 5, 7, 10, 12, 9, 6, 2, 3, 4, 1]
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = build_home_path(
        n=case.n,
        m=case.m,
        old_path=case.old_path,
    )
    assert answer == case.new_path
