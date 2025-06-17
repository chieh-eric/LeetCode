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
                stack.append(depth%2)
            elif seq[i] == ")":
                stack.append(depth%2)
                depth -= 1
       
        return stack
        # (())(())
        # (()())