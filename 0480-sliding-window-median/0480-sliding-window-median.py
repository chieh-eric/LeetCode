class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        arr = SortedList()
        left = 0 
        n = len(nums)
        res = []
        for right in range(n):
            
            arr.add(nums[right])
            if len(arr) > k:
                arr.remove(nums[left])
                left += 1
            
            if len(arr) == k:
                if k % 2:
                    res.append(float(arr[k//2]))
                else:
                    mid = k // 2
                    res.append((float(arr[mid]) + arr[mid-1])/2)
        return res
        