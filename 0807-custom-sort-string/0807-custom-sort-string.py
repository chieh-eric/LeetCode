class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        dic = {}
        for i, ch in enumerate(order):
            dic[ch] = i
        def fun(val):
            if val in dic:
                return dic[val]
            return 0
        #print(dic)
        l = list(s)
        l.sort(key=lambda x:fun(x))
        return "".join(l)
        