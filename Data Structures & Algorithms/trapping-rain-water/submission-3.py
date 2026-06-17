class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height)-1
        leftMax = height[left]
        rightMax = height[right]
        ret = 0
        while (left < right):
            if (leftMax < rightMax):
                left += 1
                leftMax = max(height[left], leftMax)
                ret += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(height[right], rightMax)
                ret += rightMax - height[right]
        
        return ret