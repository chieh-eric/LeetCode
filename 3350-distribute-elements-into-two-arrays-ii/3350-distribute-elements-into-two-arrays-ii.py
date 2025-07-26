class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        sort_arr1 = SortedList()
        sort_arr1.add(nums[0])
        sort_arr2 = SortedList()
        sort_arr2.add(nums[1])
        n1 = 1
        n2 = 1
        for i in range(2,n):
            idx1 = sort_arr1.bisect_right(nums[i])

            idx2 = sort_arr2.bisect_right(nums[i])

            if n2 - idx2 > n1 - idx1:
                arr2.append(nums[i])
                sort_arr2.add(nums[i])
                n2 += 1
            elif n1 - idx1 > n2 - idx2:
                arr1.append(nums[i])
                sort_arr1.add(nums[i])
                n1 += 1
            else:
                if n1 > n2:
                    arr2.append(nums[i])
                    sort_arr2.add(nums[i])
                    n2 += 1
                else:
                    arr1.append(nums[i])
                    sort_arr1.add(nums[i])
                    n1 += 1
     
        return arr1 + arr2
                
