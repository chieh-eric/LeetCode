class ListNode():
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.cur = 1
            
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        self.update(key)
        return self.dic[key].val
        
    def update(self, key):
        prev_node = self.dic[key].prev
        nxt_node = self.dic[key].next
        prev_node.next = nxt_node
        nxt_node.prev = prev_node

        last_node = self.tail.prev
        last_node.next = self.dic[key]
        self.dic[key].next = self.tail
        self.dic[key].prev = last_node
        self.tail.prev = self.dic[key]

    def insert(self, key, value):
        self.dic[key] = ListNode(key,value)
        last_node = self.tail.prev
        last_node.next = self.dic[key]
        self.dic[key].next = self.tail
        self.dic[key].prev = last_node
        self.tail.prev = self.dic[key]


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #print(key,value)
        if key in self.dic:
            self.dic[key].val = value
            self.update(key)
        else:
            if self.cur > self.capacity:
                delete_node = self.head.next
                delete_key = delete_node.key
                nxt_node = delete_node.next
                self.head.next = nxt_node
                nxt_node.prev = self.head
                
                del self.dic[delete_key]

                self.insert(key,value)

            else:
                
                self.cur += 1
                self.insert(key,value)
             
            
         
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)