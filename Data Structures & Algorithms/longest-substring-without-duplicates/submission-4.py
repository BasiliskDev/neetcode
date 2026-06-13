class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx1 = 0
        idx2 = 0
        chars = {}
        ret = 0
        while (idx2 < len(s)):
            print(chars)
            print(idx1)
            print(idx2)
            if (s[idx2] in chars.keys() and chars[s[idx2]] >= idx1):
                ret = max(ret, idx2 - idx1)
                idx1 = chars[s[idx2]] + 1
            
            chars[s[idx2]] = idx2
            idx2 += 1
        ret = max(ret, idx2 - idx1)
        return ret
            

            
        