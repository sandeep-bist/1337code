def is_valid(s: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
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
