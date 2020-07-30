from typing import List


def word_break(s: str, wordDict: List[str]) -> List[str]:
    """
    Time: O(n**2)
    Space: O(n**2)
    """
    def helper(s, memo={}):
        if s in memo:
            return memo[s]
        if not s:
            return []
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                result_of_the_rest = helper(s[len(word):], memo)
                for item in result_of_the_rest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res
    return helper(s)
