from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1
        small = 1000000
        while (lo <= hi):
            mid = lo + (hi-lo)//2
            small = min(small, nums[mid])
            if (nums[lo] <= nums[hi]):
                small = min(small, nums[lo])
            if (nums[lo] <= nums[mid]):
                lo = mid + 1
            else:
                hi = mid - 1

        idx = -1
        for idx1 in range(len(nums)):
            if (nums[idx1] == small):
                idx = idx1
        

        arr1 = nums[:idx]
        print(arr1)
        arr2 = nums[idx:]
        print(arr2)

        i = bisect_left(arr1, target)
        if i < len(arr1) and arr1[i] == target:
            return i

        j = bisect_left(arr2, target)
        if j < len(arr2) and arr2[j] == target:
            return j + len(arr1)

        return -1