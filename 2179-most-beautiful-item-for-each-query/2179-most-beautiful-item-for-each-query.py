import bisect
class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        items.sort(key=lambda x:(x[0],-x[1]))
        cur_beauty = 0
        for i, (price, beauty) in enumerate(items):
            cur_beauty = max(cur_beauty, beauty)
            items[i] = (price,cur_beauty)
        res = []
        n = len(items)
        for query in queries:
            idx = bisect.bisect_right(items,(query,))
            if idx == n:
                res.append(items[n-1][1])
            else:  
                if idx > 0 and items[idx][0] != query:
                    idx -= 1
                

                if items[idx][0] <= query:
                    res.append(items[idx][1])
                else:
                    res.append(items[idx-1][1] if idx -1 > 0 else 0)
           
            
        return res