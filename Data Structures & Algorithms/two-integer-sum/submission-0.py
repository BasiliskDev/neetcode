class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasht = {}
        for idx, num in enumerate(nums):
            if (target - num in hasht):
                return [hasht[target-num], idx]
            else:
                hasht[num] = idx

        