class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        m = len(colors)
        colors.extend(colors)
      
        prev = -1
        left = count = 0
        for i in range(m+k-1):
            if prev == colors[i]:
                left = i
            
            while  i - left + 1 > k:
                
                left += 1
                
            if i - left + 1 == k:
                count += 1
            prev = colors[i]
        return count
