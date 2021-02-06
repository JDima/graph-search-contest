import math
import pytest

from .task import news_dissemination


class Case:
    def __init__(self, name: str, n: int, m: int, groups: list,
                 number_of_people: list):
        self._name = name
        self.n = n
        self.m = m
        self.groups = groups
        self.number_of_people = number_of_people

    def __str__(self) -> str:
        return 'task2_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=7,
        m=5,
        groups=[
            [2, 5, 4],
            [],
            [1, 2],
            [1],
            [6, 7],
        ],
        number_of_people=[4, 4, 1, 4, 4, 2, 2],
    ),
    Case(
        name='base2',
        n=1,
        m=5,
        groups=[
            [],
            [],
            [],
            [],
            [],
        ],
        number_of_people=[1],
    ),
    Case(
        name='base3',
        n=7,
        m=5,
        groups=[
            [2, 5, 4],
            [2, 5, 4],
            [2, 5, 4],
            [2, 5, 4],
            [2, 5, 4],
        ],
        number_of_people=[1, 3, 1, 3, 3, 1, 1],
    ),
    Case(
        name='base4',
        n=8,
        m=5,
        groups=[
            [1, 2, 3, 4, 5, 6, 7, 8],
            [],
            [],
            [],
            [],
        ],
        number_of_people=[8, 8, 8, 8, 8, 8, 8, 8],
    ),
    Case(
        name='base5',
        n=9,
        m=7,
        groups=[
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [6, 7],
            [4, 5],
            [2, 3]
        ],
        number_of_people=[8, 8, 8, 8, 8, 8, 8, 8, 1],
    ),
    Case(
        name='base6',
        n=3,
        m=0,
        groups=[],
        number_of_people=[1, 1, 1],
    ),
    Case(
        name='base7',
        n=11,
        m=4,
        groups=[
            [1, 2, 8, 9],
            [3, 4, 5],
            [4, 6, 7],
            [1, 8, 9, 10, 11]
        ],
        number_of_people=[6, 6, 5, 5, 5, 5, 5, 6, 6, 6, 6],
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = news_dissemination(
        n=case.n,
        m=case.m,
        groups=case.groups,
    )
    assert answer == case.number_of_people
