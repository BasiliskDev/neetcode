class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums)-1
        low = 0
        idx = (high+low)//2
        while (high >= low):
            if (nums[idx] > target):
                high = idx - 1
            if (nums[idx] < target):
                low = idx + 1
            if (nums[idx] == target):
                return idx
            idx = (high+low)//2
        return -1
        