class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        children = [0]*k
        n = len(cookies)
        self.min_unfair = float('inf')

        def backtrack(i):
            if i == n:
                self.min_unfair = min(self.min_unfair,max(children))
                return

            for j in range(k):
                children[j] += cookies[i]

                if children[j] < self.min_unfair:
                    backtrack(i+1)

                children[j] -= cookies[i]
                if children[j] == 0:
                    break
        backtrack(0)
        return self.min_unfair          
                


                
        