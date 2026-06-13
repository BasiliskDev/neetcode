class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ""
        for i in range(len(s)):
            idx1 = i
            idx2 = i
            curr = ""
            while (idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]):
                #print(s[idx1] + " " + s[idx2])
                curr = s[idx1:idx2+1]
                idx1 -= 1
                idx2 += 1
            if (len(curr) > len(ret)):
                ret = curr
            idx1 = i
            idx2 = i+1
            while (idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]):
                #print(s[idx1] + " " + s[idx2])
                curr = s[idx1:idx2+1]
                idx1 -= 1
                idx2 += 1
            if (len(curr) > len(ret)):
                ret = curr
        return ret
            
        

                    
        