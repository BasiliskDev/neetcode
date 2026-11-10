class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[-1] = 1
        for i in range(n-2, -1, -1):
            max_sub = 0
            for j in range(i+1, n):
                if (nums[j] > nums[i]):
                    max_sub = max(max_sub, dp[j])
            dp[i] = 1 + max_sub
            #print(dp)
        return max(dp)


        