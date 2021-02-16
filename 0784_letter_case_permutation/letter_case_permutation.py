from typing import List


def letterCasePermutation(S: str) -> List[str]:
    """
    Time: O(2**n)
    Space: O(n)
    """
    def dfs(i: int, curr: str, arr: List[str]):
        if i == len(S):
            arr.append(curr)
            return
        if S[i].isalpha():
            dfs(i + 1, curr + S[i].lower(), arr)
            dfs(i + 1, curr + S[i].upper(), arr)
        else:
            dfs(i + 1, curr + S[i], arr)
    res = []
    dfs(0, "", res)
    return res