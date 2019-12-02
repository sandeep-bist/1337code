def is_palindrome(x: int) -> bool:
    s = str(x)
    return s == s[::-1]


print(is_palindrome(121))  # True
print(is_palindrome(-121))  # False
print(is_palindrome(10))  # False
print(is_palindrome(12344321))  # True
