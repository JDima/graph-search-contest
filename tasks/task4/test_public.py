import math
import pytest

from .task import harmonious_graph


class Case:
    def __init__(self, name: str, n: int, m: int, edges: list,
                 count_new_edges: int):
        self._name = name
        self.n = n
        self.m = m
        self.edges = edges
        self.count_new_edges = count_new_edges

    def __str__(self) -> str:
        return 'task4_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=14,
        m=8,
        edges=[
            (1, 2),
            (2, 7),
            (3, 4),
            (6, 3),
            (5, 7),
            (3, 8),
            (6, 8),
            (11, 12),
        ],
        count_new_edges=1,
    ),
    Case(
        name='base2',
        n=200000,
        m=3,
        edges=[
            (7, 9),
            (9, 8),
            (4, 5),
        ],
        count_new_edges=0,
    ),
    Case(
        name='base3',
        n=20,
        m=3,
        edges=[
            (7, 9),
            (9, 8),
            (4, 5)
        ],
        count_new_edges=0,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = harmonious_graph(
        n=case.n,
        m=case.m,
        edges=case.edges,
    )
    assert answer == case.count_new_edges
