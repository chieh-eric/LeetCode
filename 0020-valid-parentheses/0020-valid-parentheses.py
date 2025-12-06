class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paren = {}
        paren[")"] = "("
        paren["}"] = "{"
        paren["]"] = "["

        stack = []
        for ch in s:
            if ch not in paren:
                stack.append(ch)
            else:
                target = paren[ch]
                if not stack or stack.pop() != target:
                    return False
        return len(stack) == 0