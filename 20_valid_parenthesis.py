def isValid(s: str) -> bool:
    """
    Given a string containing just the characters '(', ')', '{', '}', '[' and
    ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.
    """
    map = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    stack = []
    for c in s:
        if c in map:
            if not stack or stack.pop() != map[c]:
                return False
        else:
            stack.append(c)
    return len(stack) == 0


print(isValid("]"))  # False
print(isValid("()[]{}"))  # True
print(isValid("(]"))  # False
print(isValid("([)]"))  # False
print(isValid("{[]}"))  # True
