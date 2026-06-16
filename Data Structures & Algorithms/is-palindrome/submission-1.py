class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''.join([c for c in s if (c.isalpha() or c.isdigit())]).lower()
        print(new_str)
        idx1 = 0
        idx2 = len(new_str)-1
        while idx1 <= idx2:
            if new_str[idx1] != new_str[idx2]:
                return False
            idx1 += 1
            idx2 -= 1
        return True 
        