class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        right = sum(task[1] for task in tasks)
        left = 0

        tasks.sort(key = lambda x:(x[1]-x[0]),reverse = True)
        
        def finish(val):
            #print(tasks)
            for task in tasks:
                if val >= task[1]:
                    val -= task[0]
                else:
                    return False
            return True
        
        while left < right:
            mid = (left+right) // 2
            res = finish(mid)

            if not res:
                left = mid + 1
            else:
                right = mid
        return left
            
