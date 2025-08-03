class MyCalendar(object):

    def __init__(self):
        self.events = SortedList()

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        
        idx = self.events.bisect_left((startTime,))
        for i in range(max(0, idx - 1), min(len(self.events), idx + 1)):
            s, e = self.events[i]
            if not (s >= endTime or e <= startTime):
                return False
        
        self.events.add((startTime, endTime))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)