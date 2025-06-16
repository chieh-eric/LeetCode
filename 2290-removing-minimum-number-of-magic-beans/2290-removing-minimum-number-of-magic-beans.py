class Solution(object):
    def minimumRemoval(self, beans):
        """
        :type beans: List[int]
        :rtype: int
        """
        # Two choice: 
        # 1. Clean all value other than the biggest one
        #
        min_count = float('inf')
        beans.sort()
        n = len(beans)
        
        total = sum(beans)

        for i, bean in enumerate(beans):
            min_count = min(min_count,total - bean*(n-i))
        return min_count