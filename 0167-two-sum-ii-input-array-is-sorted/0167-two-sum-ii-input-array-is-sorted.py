import bisect
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        for i in range(n):
            cur = numbers[i]
            idx = bisect.bisect_left(numbers,target-cur, i+1,n)
            if idx < n and numbers[idx] + cur == target:
                return [i+1, idx+1]