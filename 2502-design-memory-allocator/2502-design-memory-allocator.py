import bisect
from collections import defaultdict
class Allocator(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.free = [[0, n-1]]
        self.allocated = defaultdict(list)
        

    def allocate(self, size, mID):
        """
        :type size: int
        :type mID: int
        :rtype: int
        """
        for index, (i,j) in enumerate(self.free):
            available = j - i + 1
            if available < size:
                continue
            
            start = i
            end = i + size
            if size == available:
                self.free.pop(index)
            else:
                self.free[index][0] = end

            self.allocated[mID].append([start, end - 1])
            return start
        return -1
    
    def _insert_free_block(self, l, r):
        pos = bisect.bisect_left(self.free,[l,r])

        if pos > 0 and self.free[pos-1][1] + 1 >= l:
            l = min(l, self.free[pos-1][0])
            r = max(r, self.free[pos-1][1])
            self.free.pop(pos-1)
            pos -= 1
        
        if pos < len(self.free) and self.free[pos][0] <= r + 1:
            l = min(l, self.free[pos][0])
            r = max(r, self.free[pos][1])
            self.free.pop(pos)

        self.free.insert(pos, [l,r])

    def freeMemory(self, mID):
        """
        :type mID: int
        :rtype: int
        """
        if mID not in self.allocated:
            return 0
        count = 0
        for l, r in self.allocated[mID]:
            count += (r-l+1)
            self._insert_free_block(l,r)
        del self.allocated[mID]
        return count


        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)