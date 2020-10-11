def removeDuplicateLetters(s: str) -> str:
    """
    Time: O(n)
    Space: O(1)
    """
    seen = set()
    last = {c: i for i, c in enumerate(s)}
    stack = []
    for i, c in enumerate(s):
        if c not in seen:
            while stack and c < stack[-1] and last.get(stack[-1]) > i:
                seen.remove(stack.pop())
            seen.add(c)
            stack.append(c)
    res = ""
    for c in stack:
        res += c
    return res
