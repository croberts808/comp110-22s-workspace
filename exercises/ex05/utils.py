"""Creating functions for lists."""

__author__ = "730439833"


def only_evens(hello: list[int]) -> list[int]:
    return_list: list[int] = list()
    i: int = 0
    while i < len(hello):
        if hello[i] % 2 == 0:
            return_list.append(hello[i])
        i += 1
    return return_list


def sub(hi: list[int], a: int, b: int) -> list[int]:
    sub: list[int] = list()
    i: int = 0
    while i < len(hi):
        if i >= a and i < b:
            sub.append(hi[i])
        i += 1
    return sub


def concat(hey: list[int], hola: list[int]) -> list[int]:
    concat: list[int] = list()
    i: int = 0
    while i < len(hey):
        concat.append(hey[i])
        i += 1
    j: int = 0
    while j < len(hola):
        concat.append(hola[j])
        j += 1
    return concat




