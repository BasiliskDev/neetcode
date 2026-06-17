class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        l = 0
        max_chars = 0
        ret = 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            max_chars = max(max_chars, chars[s[r]])
            while (r-l+1 > k + max_chars):
                chars[s[l]] -= 1
                l += 1
            ret = max(ret, r-l+1)
        
        return ret


                

            
                    
        