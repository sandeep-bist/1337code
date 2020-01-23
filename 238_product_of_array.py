from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """
    Given an array nums of n integers where n > 1,  return an array output
    such that output[i] is equal to the product of all the elements of nums
    except nums[i].
    """
    size = len(nums)
    res = [1] * size
    pi = pj = 1
    for i in range(size):
        j = -1 - i
        res[i] *= pi
        res[j] *= pj
        pi *= nums[i]
        pj *= nums[j]
    return res


arr = [1, 2, 3, 4]
print(product_except_self(arr))  # [24,12,8,6]
