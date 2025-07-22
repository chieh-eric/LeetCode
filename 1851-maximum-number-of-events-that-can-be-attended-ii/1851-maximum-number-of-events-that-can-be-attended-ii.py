import bisect
class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Use dp to solve this problem, dp(index,count) means untill the index event, what's the maximum value with remain available count 
        events.sort(key=lambda x:x[0])
        start_day = [days[0] for days in events]
        n = len(events)
        memo = {}
        def dp(index,count):
            if index == n or count == 0:
                return 0
            
            if (index,count) in memo:
                return memo[(index,count)]
            idx = bisect.bisect_right(start_day,events[index][1])
            pick = dp(idx,count-1) + events[index][2]
            no_pick = dp(index+1,count)
            max_val = max(pick,no_pick)
            memo[(index,count)] = max_val
            return max_val

        return dp(0,k)