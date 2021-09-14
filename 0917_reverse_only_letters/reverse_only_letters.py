from collections import deque


def reverse_only_letters(s: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    i = 0
    j = len(s) - 1
    res = list(s)
    while i < j:
        while i < j and not res[i].isalpha():
            i += 1
        while i < j and not res[j].isalpha():
            j -= 1
        res[i], res[j] = res[j], res[i]
        i += 1
        j -= 1
    return "".join(res)


def reverse_only_letters_alt(string: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    stack = deque(x for x in string if x.isalpha())
    return ''.join(stack.pop() if x.isalpha() else x for x in string)
