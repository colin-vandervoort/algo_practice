from dataclasses import dataclass
from typing import Any
import pytest

from . import initial_approach


@dataclass
class Case:
    desc: str
    expect: Any

    def __str__(self):
        return f"sol()={self.expect}"


def idfn(val):
    if isinstance(val, Case):
        return val.desc


test_cases = []


@pytest.mark.parametrize("case", test_cases, ids=idfn)
def test_initial_approach(case):
    sol = initial_approach.Solution()  # noqa: F841
