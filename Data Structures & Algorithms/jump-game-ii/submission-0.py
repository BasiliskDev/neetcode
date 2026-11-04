class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        dp[len(nums)-1] = 0
        #print(nums)
        for i in range(len(dp)-2, -1, -1):
            #print(f"current index: {i}, max step: {nums[i]}")
            for j in range(i, min(len(dp), i+nums[i]+1)):
                if (dp[j] >= 0):
                    if (dp[i] != -1):
                        #print(f"current min steps: {dp[j]}" )
                        dp[i] = min(dp[i], dp[j] + 1)
                    else:
                        #print(f"first min step: {dp[j]}")
                        dp[i] = dp[j] + 1
                    
            #print(dp)
        return dp[0]
        