class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        valid = set()
        n = len(s)
        self.max_len = 0
        def backtrack(valid,index):
            
            if index == n:
                self.max_len = max(self.max_len,len(valid))
                return

            for i in range(index+1,n+1,1):
                if s[index:i] not in valid:
                    valid.add(s[index:i])
                    backtrack(valid,i)
                    valid.remove(s[index:i])
        backtrack(set(),0)
        return self.max_len