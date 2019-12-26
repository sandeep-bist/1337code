from collections import Counter
from typing import List


def total_fruit(tree: List[int]) -> int:
    """
    In a row of trees, the i-th tree produces fruit with type tree[i].
    You start at any tree of your choice, then repeatedly perform the
    following steps:
    Add one piece of fruit from this tree to your baskets.  If you cannot,
    stop.
    Move to the next tree to the right of the current tree.  If there is
    no tree to the right, stop.
    Note that you do not have any choice after the initial choice of
    starting tree: you must perform step 1, then step 2, then back to
    step 1, then step 2, and so on until you stop.
    You have two baskets, and each basket can carry any quantity of fruit,
    but you want each basket to only carry one type of fruit each.
    What is the total amount of fruit you can collect with this procedure?
    """
    res = i = 0
    count = Counter()
    for j, e in enumerate(tree):
        count[e] += 1
        while len(count) > 2:
            count[tree[i]] -= 1
            if count[tree[i]] == 0:
                del count[tree[i]]
            i += 1
        res = max(res, j - i + 1)
    return res


arr = [1, 2, 1]
print(total_fruit(arr))  # 3
arr2 = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
print(total_fruit(arr2))  # 5
