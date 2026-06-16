class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        hasht = {}
        for idx, num in enumerate(nums):
            hasht[num] = idx
        ret = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = -1 * (nums[i] + nums[j]) 
                if (diff in hasht and hasht[diff] != i and hasht[diff] != j):
                    ls = [nums[i], nums[j], diff]
                    ls.sort()
                    ret.add(tuple(ls))
                    
        return [list(x) for x in ret]