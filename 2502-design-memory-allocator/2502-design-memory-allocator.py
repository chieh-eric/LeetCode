class Allocator(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.arr = [0]*n
        

    def allocate(self, size, mID):
        """
        :type size: int
        :type mID: int
        :rtype: int
        """
        idx = self.findFit(size)
        if idx == -1:
            return -1
        for i in range(idx, idx+size):
            self.arr[i] = mID
        #print(self.arr)
        return idx
    
    def findFit(self, size):
        index = 0
        while index < len(self.arr):
            count = 0
            start = index
            while count < size and index < len(self.arr) and self.arr[index] == 0:
                count += 1
                index += 1
            if count == size:
                return start
            index += 1
        return -1
        
    def freeMemory(self, mID):
        """
        :type mID: int
        :rtype: int
        """
        count = 0
        for i, val in enumerate(self.arr):
            if val == mID:
                self.arr[i] = 0
                count += 1
        return count

        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)