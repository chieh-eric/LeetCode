class MyCalendar(object):

    def __init__(self):
        self.events = SortedList()

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        
        for s, e in self.events:
            if not (e <= startTime or s >= endTime):
                return False
        self.events.add((startTime,endTime))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)