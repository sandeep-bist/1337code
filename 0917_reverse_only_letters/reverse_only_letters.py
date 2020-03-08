from collections import deque


def reverse_only_letters(string: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    i, j = 0, len(string) - 1
    string = list(string)
    while i < j:
        if string[i].isalpha() and string[j].isalpha():
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
        if not string[j].isalpha():
            j -= 1
        if not string[i].isalpha():
            i += 1
    return "".join(string)


def reverse_only_letters_alt(string: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    stack = deque(x for x in string if x.isalpha())
    return ''.join(stack.pop() if x.isalpha() else x for x in string)
