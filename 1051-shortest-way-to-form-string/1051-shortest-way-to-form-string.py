class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        left = 0
        n = len(target)
        count = 0
        index = 0

        while index < n:
            source_index = 0
            count += 1
            m = len(source)
            used = False
            while source_index < m and index < n:
                if source[source_index] == target[index]:
                    index += 1
                    used = True
                source_index += 1
            if not used:
                return -1
        return count