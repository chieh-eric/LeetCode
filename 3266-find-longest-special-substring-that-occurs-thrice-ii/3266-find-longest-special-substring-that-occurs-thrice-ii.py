class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Use two pointer the scan the string
        res = []
        dic = {}
        n = len(s)
        i = 0
        valid = set()
        while i < n:
            ch = s[i]
            j = i
            while j < n and s[j] == ch:
                j += 1

            length = j - i
            for m in range(1,length + 1):
                if (s[i],m) not in dic:
                    dic[(s[i],m)] = 0
                dic[(s[i],m)] += length - m + 1
                if dic[(s[i],m)] >= 3:
                    valid.add(m)

            
            res.append((ch,length))
            
            i = j
            
        
        res.sort(key=lambda x:x[1],reverse = True)
        return max(max(valid) if valid else -1,res[0][1]-2 if res and res[0][1] - 2 > 0 else -1)
            