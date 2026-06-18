class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, hasht = {}, {}

        for char in t:
            hasht[char] = hasht.get(char, 0) + 1
        
        good = 0
        l = 0
        res = [0, 0]
        resLen = float("infinity")

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in hasht and window[s[r]] <= hasht[s[r]]:
                good += 1

            while good >= len(t):
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1

                if s[l] in hasht and window[s[l]] < hasht[s[l]]:
                    good -= 1

                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""