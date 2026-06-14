class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while (len(stack) > 0 and stack[-1][0] < t):
                idx = stack.pop()[1]
                ret[idx] = i - idx
            stack.append([t, i])
        return ret


        