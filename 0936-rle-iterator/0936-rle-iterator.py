class RLEIterator(object):

    def __init__(self, encoding):
        """
        :type encoding: List[int]
        """
        n = len(encoding)
        self.arr = []
        self.index = 0
        for i in range(0,n,2):
            if encoding[i] != 0:
                self.arr.append((encoding[i],encoding[i+1]))

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        prev = 0
        #print(n)
        for i in range(self.index,len(self.arr)):
            count += self.arr[i][0]
            if count > n:
                self.arr[i] = (self.arr[i][0]-(n-prev), self.arr[i][1])
                self.index = i
                return self.arr[i][1]
            elif count == n:
                print("fuck")
                self.index = i + 1
                return self.arr[i][1]
            self.index = i  + 1
            prev += self.arr[i][0]
        return -1
                
            
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)