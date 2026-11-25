class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if (sum(cost) > sum(gas)):
            return -1
        begin_idx = 0
        idx = 0
        currgas = 0
        looped = False
        while (idx != begin_idx - 1 and begin_idx < len(gas)):
            currgas += gas[idx] - cost[idx]
            idx += 1
            if (currgas < 0):
                currgas = 0
                if (looped):
                    return -1
                begin_idx = idx
                continue
            if (idx == len(gas)):
                if (begin_idx == 0): 
                    return 0
                idx = 0
                looped = True
        
        return begin_idx if currgas >= 0 else -1

             

        