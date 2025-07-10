class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid = set()
        n = len(s)
        def expand(l,r):
            while l >= 0 and r < n and s[l] == s[r]:
                valid.add(s[l:r+1])
                l -= 1
                r += 1
        for i in range(n):
            expand(i,i)
            expand(i,i+1)

        #print(valid)

        for i in range(1,n-1):
            if s[:i] not in valid:
                continue
            for j in range(i+1,n):
                if s[i:j] not in valid:
                    continue
                if s[j:] in valid:
                    return True
        return False
