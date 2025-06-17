class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        # ((()))
        stack = []
        depth = 0

        for num in seq:
            if num == "(":
                depth += 1
                stack.append(depth%2)
            else:
                stack.append(depth%2)
                depth -= 1
        return stack
        # (())(())
        # (()())