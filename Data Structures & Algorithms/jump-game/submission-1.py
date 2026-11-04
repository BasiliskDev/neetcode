class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[len(nums)-1] = True
        #print(nums)
        for i in range(len(dp)-2, -1, -1):
            #print(f"current index: {i}, max step: {nums[i]}")
            for j in range(i, min(len(dp), i+nums[i]+1)):
                if (dp[j]):
                    dp[i] = True
                    break
            #print(dp)
        return dp[0]