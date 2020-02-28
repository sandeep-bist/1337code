from typing import List


def find_content_children(g: List[int], s: List[int]) -> int:
    """
    Assume you are an awesome parent and want to give your children some
    cookies. But, you should give each child at most one cookie. Each
    child i has a greed factor gi, which is the minimum size of a cookie
    that the child will be content with; and each cookie j has a size sj.
    If sj >= gi, we can assign the cookie j to the child i, and the child
    i will be content. Your goal is to maximize the number of your content
    children and output the maximum number.
    """
    g.sort()
    s.sort()
    res = 0
    while len(s):
        if not g:
            break
        c = s.pop(0)
        if c >= g[0]:
            g.pop(0)
            res += 1
    return res


print(find_content_children([1, 2, 3], [1, 1]))  # 1
print(find_content_children([1, 2], [1, 2, 3]))  # 2
