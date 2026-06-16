class Solution:
    def maxArea(self, heights: List[int]) -> int:
        idx1 = 0
        idx2 = len(heights)-1
        ret = 0
        while (idx1 < idx2):
            ret = max(ret, min(heights[idx1], heights[idx2]) * (idx2 - idx1))
            if (heights[idx1] < heights[idx2]):
                idx1 += 1
            else:
                idx2 -= 1
        return ret
        