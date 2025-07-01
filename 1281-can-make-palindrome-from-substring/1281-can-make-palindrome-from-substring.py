from collections import defaultdict
class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(s)
        dic_list = [None] * n
        cur_dic = defaultdict(int)
        for i in range(n):
            cur_dic[s[i]] += 1
            dic_list[i] = cur_dic.copy()

        def find(left, right, tolerant):
            
            ret = dic_list[right].copy()
            if left != 0:
                for key in dic_list[left-1]:
                    ret[key] -= dic_list[left-1][key]
            odd = 0
            for key in ret:
                if ret[key] % 2:
                    odd += 1
            if odd > tolerant*2 + 1:
                return False
            return True


        res = []
        for l, r, k in queries:
            res.append(find(l,r,k))
        return res