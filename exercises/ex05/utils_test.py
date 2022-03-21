"""Testing our functions from utils."""

__author__ = "730439833"

from exercises.ex05.utils import only_evens, sub, concat

def test_only_evens_evens() -> None:
    evens: list[int] = [2,4,6,8]
    assert only_evens(evens) == [2,4,6,8]

def test_only_evens_empty() -> None:
    empty: list[int] = []
    assert only_evens(empty) == []

def test_only_evens_random() -> None:
    random: list[int] = [1,2,3,4]
    assert only_evens(random) == [2,4]

def test_sub_empty() -> None:
    empty: list[int] = []
    assert sub(empty, 3, 8) == []

def test_sub_random() -> None:
    random: list[int] = [1,2,3,4,5,6,7]
    assert sub(random, 2, 5) == [3,4,5]

def test_sub_easy() -> None:
    easy: list[int] = [1,2,3,4,5,6,7]
    assert sub(easy, 0,7) == [1,2,3,4,5,6,7]

def test_concat_empty() -> None:
    empty1: list[int] = []
    empty2: list[int] = []
    assert concat(empty1, empty2) == []

def test_concat_easy() -> None:
    easy1: list[int] = [1,2,3]
    easy2: list[int] = [4,5,6,7]
    assert concat(easy1, easy2) == [1,2,3,4,5,6,7]

def test_concat_bad() -> None:
    bad1: list[int] = [1]
    bad2: list[int] = [2]
    assert concat(bad1, bad2) == [1,2]

    
