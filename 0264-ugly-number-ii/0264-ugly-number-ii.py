class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        index = [1, 1, 1]
        next_val = [2, 3, 5]
        prime = [2, 3, 5]
        arr = [1]

        for _ in range(1,n):
            min_val = min(next_val)
            arr.append(min_val)

            for i in range(3):
                if next_val[i] == min_val:
                    next_val[i] = arr[index[i]] * prime[i]
                    index[i] += 1

        return arr[-1]

        

        

        