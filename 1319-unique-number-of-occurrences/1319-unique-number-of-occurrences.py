class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = Counter(arr)
        val = {}
        for key in count:
            if count[key] in val:
                return False
            val[count[key]] = True
        return True
