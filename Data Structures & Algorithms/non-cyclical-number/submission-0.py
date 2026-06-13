class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        while (n != 1):
            if (n in seen):
                return False
            seen.append(n)
            new = 0
            while (n > 0):
                new += (n%10)**2
                n = n // 10
            n = new
        return True
        


        