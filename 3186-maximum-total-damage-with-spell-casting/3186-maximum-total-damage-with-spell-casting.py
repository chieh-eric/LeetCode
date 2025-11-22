class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        # Sort the power list
        # Use binary search
        # arr = [(0,0),(1,2),(3,3), (4,6)]
        arr = SortedList()
        arr.add((0,0))
        freq = Counter(power)
        max_val = 0
        cur_max = 0
        
        for key in sorted(freq):
            add_val = key * freq[key]
            target_key = key - 2
            #print(target_key)
            idx = arr.bisect_left((target_key, -float('inf'))) - 1
            if idx < 0:
                idx = 0
            #print(idx)
            cur_max = max(cur_max,  arr[idx][1] + add_val)
            arr.add((key, cur_max))
            max_val = max(max_val, arr[-1][1])
            
        #print(sorted(power))
        #print(arr)
        return max_val


        

        