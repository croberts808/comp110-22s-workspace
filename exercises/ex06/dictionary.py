"""Exercise to start working with dictionaries."""

__author__ = "730439833"


def invert(start: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values in a dictionary.ff"""
    result: dict[str, str] = {}
    for key in start:
        value: str = start[key]
        if value in result:
            raise KeyError("Key already in result.")
        else:
            result[value] = key
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Determines the favorite color is a dictionary of people and colors."""
    favorite: str = ""
    colors_dict: dict[str, int] = {}
    for key in colors:
        if colors[key] in colors_dict:
            colors_dict[colors[key]] += 1
        else:
            colors_dict[colors[key]] = 1

    count: int = 0
    for key in colors_dict:
        if colors_dict[key] > count:
            count = colors_dict[key]
            favorite = key
    return favorite
        

def count(begin: list[str]) -> dict[str, int]:
    """Determines the number of times an item shows up in the list."""
    return_dict: dict[str, int] = {}
    for item in begin:
        if item in return_dict:
            return_dict[item] += 1
        else:
            return_dict[item] = 1
    return return_dict

        
