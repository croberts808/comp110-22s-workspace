"""File to test our functions in dictionary.py."""

__author__ = "730439833"

from cgitb import small
from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Tests invert on an empty dict."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_simple() -> None:
    """Tests invert on a simple dict."""
    simple_dict: dict[str, str] = {"1": "a", "2": "b", "3": "c"}
    assert invert(simple_dict) == {"a": "1", "b": "2", "c": "3"}


def test_invert_small() -> None:
    """Tests invert on a small dict."""
    small_dict: dict[str, str] = {"Cath": "19"}
    assert invert(small_dict) == {"19": "Cath"}


def test_favorite_color_empty() -> None:
    """Tests favorite_color on an empty dict."""
    empty_dict: dict[str, str] = {}
    assert favorite_color(empty_dict) == ""


def test_favorite_color_small() -> None:
    """Tests favorite_color on a small dict."""
    small_colors: dict[str, str] = {"Cath": "pink", "Mark": "blue", "Peter": "blue"}
    assert favorite_color(small_colors) == "blue"


def test_favorite_color_tie() -> None:
    """Tests favorite_color when there is a tie"""
    tie_colors: dict[str, str] = {"Hinal": "purple", "Krystyna": "light purple"}
    assert favorite_color(tie_colors) == "purple"


def test_count_empty() -> None:
    """Tests count for empty list."""
    empty: list[str] = []
    assert count(empty) == {}


def test_count_simple() -> None:
    """Tests count for simple list with no repeats."""
    simple: list[str] = ["hi", "hello", "hey"]
    assert count(simple) == {"hi": 1, "hello": 1, "hey": 1}


def test_count_repeats() -> None:
    """Tests count for simple list with repeats."""
    repeats: list[str] = ["Cath", "Krystyna", "Hinal", "Cath"]
    assert count(repeats) == {"Cath": 2, "Krystyna": 1, "Hinal": 1}
