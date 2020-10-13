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
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = build_home_path(
        n=case.n,
        m=case.m,
        old_path=case.old_path,
    )
    assert answer == case.new_path
