import bisect
class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        #print(nums)
        n = len(nums)
        start_pos = n // 2
        iterate = nums[:start_pos]
        pair = SortedList(nums[start_pos:])

        count = 0
       # print(iterate)
        #print(pair)
        for i in range(len(iterate)):
            idx = pair.bisect_left(iterate[i]*2)
            #print(idx)
            if idx == len(pair):
                return count
            del pair[idx]
            count += 2
        return count