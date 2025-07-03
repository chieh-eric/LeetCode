class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        n = len(s)
        def remove_pair(st, first, second, score):
            stack = []
            ret = 0
            for ch in st:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    ret += score
                else:
                    stack.append(ch)
            return "".join(stack), ret

        
        if x > y:
            st, p1 = remove_pair(s, "a", "b", x)
            _, p2 = remove_pair(st, "b", "a", y)
        else:
            st, p1 = remove_pair(s, "b", "a", y)
            _, p2 = remove_pair(st, "a", "b", x)

        return p1 + p2