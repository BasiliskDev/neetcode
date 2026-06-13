class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1 = 0
        idx2 = len(numbers)-1
        add = numbers[idx1] + numbers[idx2]
        while (idx1 <= idx2 and add != target):
            if (add > target):
                idx2 -= 1
            else:
                idx1 += 1
            add = numbers[idx1] + numbers[idx2]
        return [idx1+1, idx2+1]