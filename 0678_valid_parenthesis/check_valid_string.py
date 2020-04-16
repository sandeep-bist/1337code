from typing import List


def check_valid_string(s: str) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    curr_min = curr_max = 0
    for i in s:
        if i == "(":
            curr_min += 1
            curr_max += 1
        elif i == ")":
            curr_max -= 1
            curr_min = max(curr_min - 1, 0)
        else:
            curr_max += 1
            curr_min = max(curr_min - 1, 0)
        if curr_max < 0:
            return False
    return not curr_min


def check_valid_string_dfs(s: str) -> bool:
    """
    Time: O(3**n) !!
    Space: O(3**n)
    """
    return dfs(s, 0, [])


def dfs(s: str, index: int, arr: List[str]):
    if index == len(s):
        stack = []
        for i in arr:
            if i == "(":
                stack.append(i)
            else:
                if not len(stack) or stack[-1] != "(":
                    return False
                stack.pop()
        return len(stack) == 0
    if s[index] == "(":
        return dfs(s, index + 1, arr + ["("])
    elif s[index] == ")":
        return dfs(s, index + 1, arr + [")"])
    else:
        return (dfs(s, index + 1, arr) or
                dfs(s, index + 1, arr + ["("]) or
                dfs(s, index + 1, arr + [")"]))
