import bisect
class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.arr = [[] for _ in range(length)]
        self.snapId = 0
        #print(self.arr)

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.arr[index] and self.arr[index][-1][0] == self.snapId:
            self.arr[index][-1] = (self.snapId,val)
        else:
            self.arr[index].append((self.snapId,val))
        #print(self.arr)

    def snap(self):
        """
        :rtype: int
        """
        ret = self.snapId
        self.snapId += 1
        return ret

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        history = self.arr[index]
        idx = bisect.bisect_right(history,(snap_id,float('inf'))) - 1
        if idx >= 0:
            return self.arr[index][idx][1]
        return 0
        
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)