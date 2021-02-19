def minRemoveToMakeValid(s: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    stack = []
    tmp = list(s)
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                tmp[i] = ""
    for i in stack:
        tmp[i] = ""
    return "".join(tmp)