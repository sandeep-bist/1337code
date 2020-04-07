from typing import List


def depth_sum(nested_list: List[NestedInteger]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    res = [0]
    for i in nested_list:
        if i.isInteger():
            res[0] += i.getInteger()
        else:
            dfs(i, 2, res)
    return res[0]


def dfs(arr: List[NestedInteger], level: int, res: List[0]):
    for i in arr.getList():
        if i.isInteger():
            res[0] += level * i.getInteger()
        else:
            dfs(i, level + 1, res)


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
