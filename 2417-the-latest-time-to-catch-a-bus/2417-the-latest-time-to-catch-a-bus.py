class Solution(object):
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        """
        :type buses: List[int]
        :type passengers: List[int]
        :type capacity: int
        :rtype: int
        """
        buses.sort()
        passengers.sort()
        pa = set(passengers)
        i = 0 # For passengers
        n = len(passengers)

        count = 0
        t = 0
        for bus in buses:
            count = 0
            while i < n and passengers[i] <= bus and count < capacity:
                count += 1
                i += 1
        
        last_bus = buses[-1]
        if count < capacity:
            t = last_bus
        else:
            t = passengers[i-1]
        
        while t in pa:
            t -= 1
        return t