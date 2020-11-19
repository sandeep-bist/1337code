def decodeString(s: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    stack = [["", 1]]
    num = ""
    for ch in s:
        if ch.isdigit():
            num += ch
        elif ch == '[':
            stack.append(["", int(num)])
            num = ""
        elif ch == ']':
            substr, times = stack.pop()
            stack[-1][0] += substr * times
        else:
            stack[-1][0] += ch
    return stack[0][0]