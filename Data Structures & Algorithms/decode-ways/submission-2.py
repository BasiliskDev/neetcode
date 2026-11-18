class Solution:
    def numDecodings(self, s: str) -> int:
        prev_seen = {}
        def decode(idx):
            if (idx in prev_seen):
                return prev_seen[idx]
            if (idx == len(s)):
                return 1
            totalsum = 0
            if (idx + 1 <= len(s)):
                if (int(s[idx]) > 0 and int(s[idx]) <= 9):
                    totalsum += decode(idx+1)
            if (idx + 2 <= len(s)):
                twodigits = s[idx:idx+2]
                if (int(twodigits) > 9 and int(twodigits) <= 26):
                    totalsum += decode(idx+2)
            prev_seen[idx] = totalsum
            return totalsum
        return decode(0)

            
        