class Solution(object):
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        need = (neededApples+3)/4
        # 1 -> 1,2 ; 2 -> 1,2,2,3,4 ; 3 -> 1, 2, 3,
    
        def find(k):
            return  2 * k * (k + 1) * (2 * k + 1)
        
        left = 0
        right = 10**6

        while left < right:
            mid = (left+right) // 2
            if find(mid) < neededApples:
                left = mid + 1
            else:
                right = mid
        return 8 *left


        #
        # 0

        # 1
        # 1,1 
        # 1,0

        # 2
        # 1,2 2,2
        # 1,1 2,1
        # 1,0 2,0