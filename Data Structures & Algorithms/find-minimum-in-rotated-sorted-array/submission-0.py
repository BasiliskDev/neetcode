class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1
        ans = 1000000
        while (lo <= hi):
            mid = lo + (hi-lo)//2
            ans = min(ans, nums[mid])
            if (nums[lo] <= nums[hi]):
                return min(ans, nums[lo])
            if (nums[lo] <= nums[mid]):
                lo = mid + 1
            else:
                hi = mid - 1
        return nums[lo]
        




