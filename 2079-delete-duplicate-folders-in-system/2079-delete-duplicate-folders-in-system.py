from collections import defaultdict
class TrieNode():
    def __init__(self, name=""):
        self.name = name
        self.children = {}
        self.is_deleted = False

class Solution(object):
    def deleteDuplicateFolder(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: List[List[str]]
        """
        root = TrieNode()
        
        for path in paths:
            cur = root
            for ch in path:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode(ch)
                cur = cur.children[ch]
        
        sig2node = defaultdict(list)
        
        # Retrun the string format of the current node representation 
        def searilize(node):
            if not node.children:
                return ()
            
            items = []
            for name in sorted(node.children):
                child = node.children[name]
                items.append((name, searilize(child)))
            sig = tuple(items)
            sig2node[sig].append(node)
            return sig
        searilize(root)
        #print(sig2node)

        for sig, nodes in sig2node.items():
            if sig and len(nodes) > 1:
                for node in nodes:
                    #print("hi")
                    #print(node)
                    node.is_deleted = True
        
        ans = []
        def dfs(node, path):

            for name, child in node.children.items():
                if child.is_deleted:
                    continue
                new_path = path + [name]
                ans.append(new_path)
                dfs(child, new_path)

        dfs(root,[])
        return ans
            