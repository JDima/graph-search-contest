import math
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
        name='base1',
        n=5,
        G=[
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 1, 1, 0],
        ],
        cycle=None,
    ),
    Case(
        name='base2',
        n=5,
        G=[
            [0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 0, 0, 0],
        ],
        cycle=[[1, 3, 2], [1, 3, 5]],
    ),
    Case(
        name='base3',
        n=5,
        G=[
            [0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 1, 1, 0],
        ],
        cycle=[[1, 4, 2], [1, 3, 2], [1, 5, 2]],
    ),
    Case(
        name='base4',
        n=5,
       G=[
            [0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 0, 0, 0],
        ],
        cycle=[[2, 3, 5], [1, 3, 5]],
    ),
    Case(
        name='base5',
        n=3,
        G=[
            [0, 1, 1],
            [0, 0, 1],
            [0, 0, 0]
        ],
        cycle=None,
    ),
    Case(
        name='base6',
        n=3,
        G=[
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0]
        ],
        cycle=[[1, 2, 3]],
    ),
    Case(
        name='base8',
        n=4,
        G=[
            [0, 1, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 0]
        ],
        cycle=[[1, 3, 4], [1, 2, 4]],
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = find_cycle(
        n=case.n,
        G=[[bool(elem) for elem in line] for line in case.G],
    )
    if case.cycle is None:
        assert answer is None
    else:
        assert len(answer) == 3
        for i in range(len(answer) - 1):
            assert case.G[answer[i] - 1][answer[i + 1] - 1] == 1
        assert case.G[answer[-1] - 1][answer[0] - 1] == 1
