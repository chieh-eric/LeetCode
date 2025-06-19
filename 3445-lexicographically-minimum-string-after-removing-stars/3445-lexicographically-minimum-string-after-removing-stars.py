from collections import defaultdict
class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = defaultdict(list)
        n = len(s)
        deleted_index = set()
        for i in range(n):
            if s[i] == "*":
                deleted_index.add(i)
                if dic:
                    deleted_index.add(dic[min(dic)].pop())
                    if not dic[min(dic)]:
                        del dic[min(dic)]

            else:
                dic[ord(s[i])].append(i)
        res = []
        for i in range(n):
            if i in deleted_index:
                continue
            res.append(s[i])

        return ''.join(res)