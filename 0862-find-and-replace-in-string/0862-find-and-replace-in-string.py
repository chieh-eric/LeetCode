class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        res = []
        n = len(s)
        k = len(indices)
        combine = sorted([(indices[i],sources[i],targets[i]) for i in range(k)])
        i = left = 0
        while i < k and left < n:
            #print(combine)
            m = len(combine[i][1])
            if s[combine[i][0]:combine[i][0]+m] == combine[i][1]:
                res += s[left:combine[i][0]]
                res += combine[i][2]
                left = combine[i][0]+m
            i += 1
        res += s[left:]
        #print(res)
        return "".join(res)

        
        