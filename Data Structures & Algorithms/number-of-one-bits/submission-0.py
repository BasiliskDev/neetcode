class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        for i in range(32, -1, -1):
            if (n - 2**i >= 0):
                n = n - 2**i
                ones += 1
        return ones