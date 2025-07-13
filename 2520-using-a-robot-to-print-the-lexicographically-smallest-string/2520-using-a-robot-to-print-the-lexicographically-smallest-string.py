class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        min_suffix = [""]*n
        cur_min = s[-1]
        for i in range(n-1,0,-1):
            cur_min = min(cur_min,s[i])
            min_suffix[i-1] = cur_min
        #print(min_suffix)
        stack = []
        res = []
        for i in range(n):
            stack.append(s[i])
            while stack and stack[-1] <= min_suffix[i]:
                res.append(stack.pop())
        res.extend(reversed(stack))
        return "".join(res)