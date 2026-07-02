class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def bt(idxs):
            if (len(idxs) == len(nums)):
                currptation = []
                for idx in idxs:
                    currptation.append(nums[idx])
                ret.append(currptation)
            else:
                for i in range(len(nums)):
                    if (i not in idxs):
                        tmp = idxs.copy()
                        tmp.append(i)
                        bt(tmp)
        bt([])
        return ret
                

        