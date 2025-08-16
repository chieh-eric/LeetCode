class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove(st, first, second, score):
            stack = []
            i = 0
            m = len(st)
            out = 0
            # ab first
            while i < m:
                
                if stack and stack[-1] == first and st[i] == second:
                    out += score
                    stack.pop()
                else:
                    stack.append(st[i])
                i += 1
            return ''.join(stack), out

        res = 0
        val1 = val2 = 0
        if x > y:
            s, val1 = remove(s, "a", "b", x)
            _, val2 = remove(s, "b", "a", y)
        else:
            s, val1 = remove(s, "b", "a", y)
            _, val2 = remove(s, "a", "b", x)

        return val1 + val2