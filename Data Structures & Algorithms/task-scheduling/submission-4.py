class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        freq.sort()
        maxf = freq.pop()

        idle_time = (maxf-1)*n

        for f in freq:
            idle_time -= min(maxf-1, f)
        
        return max(0,idle_time) + len(tasks)