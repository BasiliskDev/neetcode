class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_nums = {}
        for num in nums:
            unique_nums[num] = unique_nums.get(num, 0) + 1
        sorted_nums = sorted(unique_nums.keys(), key=lambda x: unique_nums[x], reverse=True)
        return sorted_nums[:k]
        