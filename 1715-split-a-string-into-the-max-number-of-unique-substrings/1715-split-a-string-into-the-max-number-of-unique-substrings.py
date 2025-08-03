class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        has = set()
        self.max_len = 0
        n = len(s)
        def backtrack(i):
            if i == n:
                self.max_len = max(self.max_len,len(has))
                return

            for j in range(i+1,n+1):
                if s[i:j] in has:
                    continue
                has.add(s[i:j])
                backtrack(j)
                has.remove(s[i:j])
        backtrack(0)
        return self.max_len