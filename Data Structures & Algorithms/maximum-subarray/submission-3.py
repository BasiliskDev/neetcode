class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = -100000000000
        ret = -100000000000
        for i in range(len(nums)):
            curr = curr + nums[i] if (curr + nums[i]) > nums[i] else nums[i]
            ret = max(curr, ret)
        return max(curr, ret)
            
