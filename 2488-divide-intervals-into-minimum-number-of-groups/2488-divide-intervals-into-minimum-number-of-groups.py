class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:(x[0],-x[1]))
        #print(intervals)
        arr = SortedList()
        for left, right in intervals:

            if not arr:
                arr.add(right)
            else:
                idx = arr.bisect_left(left)
                
                if idx == 0:
                    arr.add(right)
                else:
                    arr.pop(idx-1)
                    arr.add(right)
            #print(arr)
        return len(arr)