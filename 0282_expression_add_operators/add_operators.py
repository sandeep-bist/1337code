from typing import List


def add_operators(num: str, target: int) -> List[str]:
    """
    Time: O(n**3)
    Space: O(n**2)
    """
    def dfs(index = 0, path = '', curr = 0, prev = None):            
        if index == len(num):
            if curr == target:
                res.append(path)
            return
        for i in range(index, len(num)):
            tmp, s = int(num[index: i + 1]), num[index: i + 1]
            if i == index or (i > index and num[index] != '0'):
                if prev is None:
                    dfs(i + 1, s, tmp, tmp)
                else:
                    dfs(i + 1, path + '+' + s, curr + tmp, tmp)
                    dfs(i + 1, path + '-' + s, curr - tmp, -tmp)
                    dfs(i + 1, path + '*' + s, curr - prev + prev * tmp, prev * tmp)
    res = []
    dfs()
    return res