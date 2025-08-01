import bisect
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ages.sort()
        total = 0
        for age in ages:
            if age <= 14:
                continue
            low = (age//2 + 7) + 1
            low_index = bisect.bisect_left(ages,low)
            high_index = bisect.bisect_right(ages,age)
            total += (high_index-low_index-1)
            #print(total)
        return total
