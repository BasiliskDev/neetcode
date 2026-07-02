class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = set()
        def backtrack(currlist):
            nonlocal ret, nums, target
            if (sum(currlist) > target):
                return
            elif (sum(currlist) == target):
                x = currlist.copy()
                x.sort()
                ret.add(tuple(x))
            else:
                for num in nums:
                    currlist.append(num)
                    backtrack(currlist)
                    currlist.pop()
        backtrack([])
        return [list(x) for x in list(ret)]
        