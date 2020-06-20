from math import factorial

def get_permutation(n: int, k: int) -> str:
    """
    Time: O(n**2)
    Space: O(n)
    """
    numbers = [i for i in range(1, n+1)]
    permutation = ''
    k -= 1
    while n > 0:
        n -= 1
        index, k = divmod(k, factorial(n))
        permutation += str(numbers[index])
        numbers.remove(numbers[index])
    return permutation