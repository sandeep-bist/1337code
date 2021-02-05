def simplifyPath(path: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    stack = []
    for p in path.split("/"):
        if p == "..":
            if stack:
                stack.pop()
        elif p and p != ".":
            stack.append(p)
    return "/" + "/".join(stack)