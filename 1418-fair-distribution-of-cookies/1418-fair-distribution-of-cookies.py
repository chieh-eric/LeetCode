class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cookies)
        self.min_val = float('inf')
        status = [0]*k

        def backtrack(index):
            if index == n:
                self.min_val = min(self.min_val, max(status))
                return
            
            for i in range(k):
                status[i] += cookies[index]
                if status[i] < self.min_val:
                    backtrack(index+1)
                status[i] -= cookies[index]
        backtrack(0)
        return self.min_val
      