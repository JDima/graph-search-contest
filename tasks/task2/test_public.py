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
        name='base',
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
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = news_dissemination(
        n=case.n,
        m=case.m,
        groups=case.groups,
    )
    assert answer == case.number_of_people
