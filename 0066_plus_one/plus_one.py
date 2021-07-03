class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while digits[i] == 9:
            digits[i] = 0
            i -= 1
        if i < 0:
            return [1] + digits
        digits[i] += 1
        return digits
    
    
    def plusOneComprehensions(self, digits: List[int]) -> List[int]:
        num = int("".join([str(s) for s in digits]))
        return [s for s in str(num + 1)]