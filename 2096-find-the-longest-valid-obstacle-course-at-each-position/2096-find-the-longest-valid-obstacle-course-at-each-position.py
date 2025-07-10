import bisect
class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """
        order = []
        n = len(obstacles)
        ans = []
        for i in range(n):
            idx = bisect.bisect_right(order,obstacles[i])
            if idx == len(order):
                order.append(obstacles[i])
            else:
                order[idx] = obstacles[i]
                
            
            ans.append(idx+1)
        
        return ans