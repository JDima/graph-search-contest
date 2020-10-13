import pytest

from .task import find_cycle


class Case:
    def __init__(self, name: str, n: int, G: list, cycle: list):
        self._name = name
        self.n = n
        self.G = G
        self.cycle = cycle

    def __str__(self) -> str:
        return 'task5_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        n=5,
        G=[
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 1, 1, 0],
        ],
        cycle=[1, 3, 2],
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = find_cycle(
        n=case.n,
        G=case.G,
    )
    assert answer == case.cycle
