class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        properties.sort(key=lambda x:(-x[0],x[1]))
        
        i = 1
        n = len(properties)
        max_val = properties[0][1]
        count = 0
        #print(properties)
        while i < n:
            if max_val > properties[i][1]:
                count += 1
            max_val = max(max_val, properties[i][1])
            i += 1
        return count