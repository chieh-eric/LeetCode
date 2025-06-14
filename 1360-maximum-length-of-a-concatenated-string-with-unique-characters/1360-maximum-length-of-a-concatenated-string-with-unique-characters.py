class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        cur_mask = 0
        self.count = 0
        n = len(arr)
        def dfs(mask,index):
            self.count = max(self.count,bin(mask).count('1'))
            if index >= n :
                return
        
            
            for i in range(index,n):
                new_mask = 0
                valid = True
                for ch in arr[i]:
                    bit = (1 << (ord(ch)-ord('a')))
                    if bit & new_mask > 0:
                        valid = False
                        break
                    new_mask |= bit

                if not valid or (new_mask & mask) > 0:
                    continue
                new_mask = new_mask | mask
                dfs(new_mask,i+1)
        dfs(0,0)
        return self.count