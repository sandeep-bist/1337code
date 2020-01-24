from collections import Counter


def frequency_sort(s: str) -> str:
    """
    Given a string, sort it in decreasing order based on the frequency of
    characters.
    """
    return ("".join(char * times for char, times in Counter(s).most_common()))


print(frequency_sort("tree"))  # "eert"
