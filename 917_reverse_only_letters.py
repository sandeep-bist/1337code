from collections import deque


def reverse_only_letters(string: str) -> str:
    """
    Given a string, return the "reversed" string where all characters that
    are not a letter stay in the same place, and all letters reverse their
    positions.
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
    Alternate solution.
    """
    stack = deque(x for x in string if x.isalpha())
    return ''.join(stack.pop() if x.isalpha() else x for x in string)


print(reverse_only_letters("ab-cd"))  # "dc-ba"
print(reverse_only_letters("a-bC-dEf-ghIj"))  # "j-Ih-gfE-dCba"
print(reverse_only_letters("Test1ng-Leet=code-Q!"))  # "Qedo1ct-eeLg=ntse-T!"
