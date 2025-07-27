import bisect
class Solution(object):
    def closestRoom(self, rooms, queries):
        """
        :type rooms: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        rooms.sort(key=lambda x:(-x[1]))
        queries = sorted([(size, preId,idx) for idx, (preId, size) in enumerate(queries)],reverse=True)
        n = len(rooms)
        res = [-1]*len(queries)
        sortlist = SortedList()
        i = 0
        for min_size, preId, idx in queries:
            
            while i < n and rooms[i][1] >= min_size:
                sortlist.add(rooms[i][0])
                i += 1
            
            m = len(sortlist)
            if m == 0:
                continue
            target_idx = sortlist.bisect_left(preId)

            if target_idx >= m:
                res[idx] = sortlist[-1]
            elif target_idx == 0:
                res[idx] = sortlist[0]
            else:
                small = sortlist[target_idx-1]
                large = sortlist[target_idx]
                diff_s = abs(small - preId)
                diff_l = abs(large - preId)

                if diff_s == diff_l:
                    res[idx] = small
                elif diff_s > diff_l:
                    res[idx] = large
                else:
                    res[idx] = small

        return res