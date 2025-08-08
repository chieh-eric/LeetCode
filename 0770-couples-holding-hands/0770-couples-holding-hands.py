class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row)
        mapper = {}
        slot = 0
        for i in range(0,n,2):
            mapper[row[i]] = (slot,i+1)
            mapper[row[i+1]] = (slot,i)
            slot += 1
        #print(mapper)
        visited = [False]*(n//2)

        total = 0
        for i in range(n):
            if not visited[mapper[row[i]][0]]:
                start = i
                count = 1
                while not visited[mapper[row[start]][0]]:
                    visited[mapper[row[start]][0]] = True
                    nxt_slot = nxt_index = -1
                    if row[start] % 2:
                        nxt_slot, nxt_index = mapper[row[start] - 1]
                    else:
                        nxt_slot, nxt_index = mapper[row[start] + 1]
                    if not visited[nxt_slot]:
                        count += 1
                    start = nxt_index
                total += count - 1
        return total