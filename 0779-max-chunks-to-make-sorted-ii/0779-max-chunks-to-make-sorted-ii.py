from collections import defaultdict
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # sorted_arr 
        # 1,2,3,4,4
        # 2,1,3,4,4

        # 1,2,3,4,5
        # 5,4,3,2,1

        sorted_arr = sorted(arr)
        chunks = 0
        sorted_dic = defaultdict(int)
        dic = defaultdict(int)
        keys = {}
        n = len(arr)

        for i in range(n):
            dic[arr[i]] += 1
            sorted_dic[sorted_arr[i]] += 1
            keys[arr[i]] = True
            keys[sorted_arr[i]] = True
            # Compare
            valid = True
            for key in keys:
                if key not in dic or key not in sorted_dic:
                    valid = False
                    break
                if dic[key] != sorted_dic[key]:
                    valid = False
                    break
            if valid:
                dic = defaultdict(int)
                sorted_dic = defaultdict(int)
                keys = {}
                chunks += 1
            
        return chunks
                
        
