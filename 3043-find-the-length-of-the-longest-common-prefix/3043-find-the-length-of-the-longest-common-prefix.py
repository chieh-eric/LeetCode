class Node():
    def __init__(self):
        self.children = {}

class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        # 1
        # 0
        # 0
        tree1 = Node()
        for val in arr1:
            word = str(val)
            cur = tree1
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = Node()
                cur = cur.children[ch]

        tree2 = Node()
        for val in arr2:
            word = str(val)
            cur = tree2
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = Node()
                cur = cur.children[ch]
        
        self.max_depth = 0
        def dfs(pos1, pos2, d):
            self.max_depth = max(self.max_depth, d)
            for child1 in pos1.children:
                for child2 in pos2.children:
                    if child1 == child2:
                        dfs(pos1.children[child1], pos2.children[child2],d+1)
        dfs(tree1, tree2, 0)
        return self.max_depth





        # 1
        # 0
        # 0
        # 0

