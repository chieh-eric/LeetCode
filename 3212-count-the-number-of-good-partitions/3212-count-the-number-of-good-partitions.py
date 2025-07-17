from collections import defaultdict
class Solution(object):
    def numberOfGoodPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        def calculate(count):
            return 2**(count-1)

        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)

        n = len(nums)
        valid = set()
        group = 0
        i = 0
        while i < n:
            if nums[i] not in valid:
                valid.add(nums[i])
                group += 1
                right_most_pos = pos[nums[i]][-1]

                while i < right_most_pos:
                    if nums[i] not in valid:
                        valid.add(nums[i])
                        right_most_pos = max(right_most_pos,pos[nums[i]][-1])
                    i += 1
            i += 1
        #print(group)
        return calculate(group) % mod