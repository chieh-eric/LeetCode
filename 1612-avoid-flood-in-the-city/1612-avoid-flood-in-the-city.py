import bisect
class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        n = len(rains)
        res = [-1]*n
        full = {}
        dry = SortedList()

        for i in range(n):
            lake = rains[i]
            if lake == 0:
                dry.add(i)
                res[i] = 1
                continue
            
            else:
                if lake in full:
                    idx = bisect.bisect_right(dry,full[lake])
                    if idx == len(dry):
                        return []
                    
                    dry_day = dry[idx]
                    res[dry_day] = lake
                    dry.remove(dry_day)
                full[lake] = i
                res[i] = -1
        
        return res


                