from typing import List


def partition(s: str) -> List[List[str]]:
    """
    Time: O(n * 2**n)
    Space: O(n ** 2)
    """
    def isPalindrome(start_ind, end_ind):
        while start_ind <= end_ind:
            if s[start_ind] != s[end_ind]: return False
            start_ind += 1
            end_ind -=1
        return True
    
    def dfs(start_ind: int, path: List[List[str]]):
        if start_ind >= len(s):
            res.append(path)
        for l in range(len(s) - start_ind):
            if isPalindrome(start_ind, start_ind + l):
                dfs(start_ind + l + 1, path + [s[start_ind:start_ind + l + 1]] )
    
    res = []
    dfs(0,[])
    return res