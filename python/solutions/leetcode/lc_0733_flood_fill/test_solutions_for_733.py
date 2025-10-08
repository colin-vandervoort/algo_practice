from dataclasses import dataclass
from typing import Any, List
import pytest

from . import dfs


@dataclass
class Case:
    desc: str
    image: List[List[int]]
    sr: int
    sc: int
    color: int
    expect: Any


def idfn(val):
    if isinstance(val, Case):
        return val.desc


test_cases = [
    Case(
        desc="3x3 only recolor center",
        image=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        sr=1,
        sc=1,
        color=2,
        expect=[[0, 0, 0], [0, 2, 0], [0, 0, 0]],
    ),
    Case(
        desc="3x3 only recolor outside",
        image=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        sr=0,
        sc=0,
        color=2,
        expect=[[2, 2, 2], [2, 1, 2], [2, 2, 2]],
    ),
]


@pytest.mark.parametrize("case", test_cases, ids=idfn)
def test_old_solution(case):
    sol = dfs.Solution()  # noqa: F841
    assert sol.floodFill(case.image, case.sr, case.sc, case.color) == case.expect
