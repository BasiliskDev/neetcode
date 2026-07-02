class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        def backtrack(nums, idx, currset):
            if (idx == len(nums)):
                ret.add(tuple(currset))
                return
            currset.append(nums[idx])
            backtrack(nums, idx+1, currset)
            currset.pop()
            backtrack(nums, idx+1, currset)
        backtrack(nums, 0, [])
        return [list(x) for x in list(ret)]
        