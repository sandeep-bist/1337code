from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    """
    if not len(strs):
        return ""
    for i, e in enumerate(strs[0]):
        # Vertical scanning.
        for str in strs[1:]:
            if i >= len(str) or str[i] != e:
                return strs[0][:i]
    return strs[0]


def longest_common_prefix_zip(strs: List[str]) -> str:
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    """
    res = []
    for x in zip(*strs):
        if len(set(x)) == 1:
            res.append(x[0])
        else:
            break
    return "".join(res)


arr = ["flower", "flow", "flight"]
print(longest_common_prefix(arr))  # fl
print(longest_common_prefix_zip(arr))  # fl

arr = ["dog", "racecar", "car"]
print(longest_common_prefix(arr))  # ""
print(longest_common_prefix_zip(arr))  # ""
