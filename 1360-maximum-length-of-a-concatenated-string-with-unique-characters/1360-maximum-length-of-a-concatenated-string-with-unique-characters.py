class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        
        self.max_len = 0
        new_arr = []
        for word in arr:
            c = Counter()
            good = True
            for ch in word:
                if ch in c:
                    good = False
                    break
                c[ch] += 1
            if good:
                new_arr.append(word)
        arr = new_arr
        n = len(arr)
        def backtrack(i,count):
            if i == n:
                self.max_len = max(self.max_len, sum(count.values()))
                return
            add = True
            backtrack(i+1,count)
            temp = count.copy()
            for ch in arr[i]:
                if ch in count:
                    add = False
                temp[ch] += 1
            
            if add:
                backtrack(i+1,temp)
        backtrack(0,Counter())
        return self.max_len