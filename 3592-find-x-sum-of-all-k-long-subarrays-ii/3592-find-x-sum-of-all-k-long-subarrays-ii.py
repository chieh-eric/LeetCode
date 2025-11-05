from sortedcontainers import SortedList
from collections import defaultdict

class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        freq = defaultdict(int)

        top = SortedList()
        bottom = SortedList()
        total = [0]
        ans = []

        def add_element(num):
            old_freq = freq[num]
            freq[num] += 1
            old_key = (-old_freq, -num)
            new_key = (-freq[num], -num)

            if old_freq > 0:
                if old_key in top:
                    top.remove(old_key)
                    total[0] -= old_freq*num
                elif old_key in bottom:
                    bottom.remove(old_key)
            
            bottom.add(new_key)
            rebalance()
        
        def rebalance():

            while len(top) < x and bottom:
                move_up = bottom.pop(0)
                top.add(move_up)
                total[0] += (-move_up[0]*-move_up[1])
            
            while len(top) > x:
                move_down = top.pop(-1)
                bottom.add(move_down)
                total[0] -= (-move_down[0]*-move_down[1])
            
            while top and bottom and top[-1] > bottom[0]:
                weak_top = top.pop()
                strong_bottom = bottom.pop(0)
                top.add(strong_bottom)
                bottom.add(weak_top)
                total[0] += (-weak_top[0]*weak_top[1] + strong_bottom[0]*strong_bottom[1])

        def remove(num):
            old_freq = freq[num]
            freq[num] -= 1
            old_key = (-old_freq, -num)
            new_freq = freq[num]
            new_key = (-freq[num], -num)

            if old_key in top:
                top.remove(old_key)
                total[0] -= old_freq*num
            elif old_key in bottom:
                bottom.remove(old_key)
            
            if new_freq > 0:
                bottom.add(new_key)
            else:
                del freq[num]
            
            rebalance()
        
        n = len(nums)
        for i in range(k):
            add_element(nums[i])
        ans.append(total[0])

        for i in range(k, n):
            remove(nums[i-k])
            add_element(nums[i])
            ans.append(total[0])
        return ans
