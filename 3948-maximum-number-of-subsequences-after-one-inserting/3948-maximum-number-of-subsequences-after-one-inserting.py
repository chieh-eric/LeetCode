class Solution(object):
    def numOfSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        prefix_l = [0]*n
        suffix_t = [0]*n

        add_prefix_l = [1]*n
        add_suffix_t = [1]*n
        

        count = 0
        for i in range(n):
            if s[i] == "L":
                count += 1
            prefix_l[i] = count
            add_prefix_l[i] += count
        count = 0
        for i in range(n-1,-1,-1):
            if s[i] == "T":
                count += 1
            suffix_t[i] = count
            add_suffix_t[i] += count
            
      

        add_c = 0
        add_t_total = add_c_total = add_l_total = 0
        for i in range(n):
            if s[i] == "C":
                add_l_total += add_prefix_l[i]*suffix_t[i]
                add_t_total += prefix_l[i]*add_suffix_t[i]
                add_c_total += prefix_l[i]*suffix_t[i]
            add_c = max(add_c,prefix_l[i]*suffix_t[i])
        return max(add_l_total,add_t_total,add_c_total+add_c)
            
            