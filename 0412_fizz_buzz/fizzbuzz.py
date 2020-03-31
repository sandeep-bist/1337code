from typing import List


def fizzBuzz(n: int) -> List[str]:
    """
    Time: O(n)
    Space: O(1) 
    """
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
