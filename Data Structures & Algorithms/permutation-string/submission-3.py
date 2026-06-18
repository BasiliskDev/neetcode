class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False
        sorted_s1 = sorted(s1)
        for r in range(len(s1), len(s2)+1):
            substr = [char for char in s2[r-len(s1):r]]
            if (sorted(substr) == sorted_s1):
                return True
        return False
            

        