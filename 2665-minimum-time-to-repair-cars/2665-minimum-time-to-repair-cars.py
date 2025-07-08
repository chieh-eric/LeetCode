class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        left = 1
        right = min(ranks)*cars*cars

        def finish(time):
            car = 0
            for m in ranks:
                car += int((time/m)**0.5) 
            return car

        while left < right:
            mid = (left+right) // 2
            valid = finish(mid)

            if valid < cars:
                left = mid + 1
            else:
                right = mid
        return left