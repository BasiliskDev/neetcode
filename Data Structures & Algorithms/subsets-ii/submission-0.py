class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        def bt(idx, ls):
            ret.append(ls.copy())

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue

                ls.append(nums[i])
                bt(i + 1, ls)
                ls.pop()
        bt(0, [])
        return ret
        
        