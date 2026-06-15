class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ret = 0
        hasht = {}
        for num in nums:
            hasht[num] = 1
        
        for num in nums:
            if (num-1 in hasht):
                continue
            else:
                x = num
                curr = 0
                while (x in hasht):
                    curr += 1
                    x += 1
                ret = max(curr, ret)
        
        return ret
                
                    


        