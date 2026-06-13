class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = 10000000000
        curr = (low + high)//2
        while (high >= low):
            hrs = sum([math.ceil(p/curr) for p in piles])
            if (hrs <= h):
                high = curr - 1
            else:
                low = curr + 1
            print(curr)
            curr = (low + high)//2
        return low
            
        