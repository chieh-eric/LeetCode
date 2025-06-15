class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        root = TrieNode()
        n = len(nums)
        count = 0
        for i in range(n):
            cur = 0
            sub = []
            node = root
            for j in range(i,n):
                if nums[j] % p == 0:
                    cur += 1
                if cur > k:
                    break
                sub.append(nums[j])
                if nums[j] not in node.children:
                    node.children[nums[j]] = TrieNode()
                    count += 1

                node = node.children[nums[j]]
        return count