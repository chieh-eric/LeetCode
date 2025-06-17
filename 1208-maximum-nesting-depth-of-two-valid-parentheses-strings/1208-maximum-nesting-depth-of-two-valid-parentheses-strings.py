class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        # ((()))
        stack = []
        n = len(seq)
        depth = 0

        for i in range(n):
            if seq[i] == "(":
                depth += 1
                stack.append(depth)
            elif seq[i] == ")":
                stack.append(depth)
                depth -= 1
        res = []
        for i in range(n):
            res.append(stack[i]%2)
        return res
        # (())(())
        # (()())