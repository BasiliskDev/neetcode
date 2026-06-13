class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        digits.append(0)
        idx = 0
        digits[idx] += 1
        while (idx < len(digits)-1 and digits[idx] == 10):
            digits[idx] = 0
            digits[idx+1] += 1
            idx += 1
        if (digits[-1] != 1):
            digits.pop()
        digits.reverse()
        return digits

        