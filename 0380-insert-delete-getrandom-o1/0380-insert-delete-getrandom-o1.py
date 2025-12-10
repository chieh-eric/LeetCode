import random
class RandomizedSet(object):

    def __init__(self):
        self.store = []
        self.pos = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False
        self.pos[val] = len(self.store)
        self.store.append(val)
   


    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False
        lastValue = self.store[-1]
        popIndex = self.pos[val]
        self.store[popIndex], self.store[-1] = self.store[-1], self.store[popIndex]
        self.pos[lastValue] = popIndex
        self.store.pop()
        del self.pos[val]

        return True
      
    def getRandom(self):
        """
        :rtype: int
        """
        target = random.randint(0, len(self.store) - 1)
        return self.store[target]
        #print(target)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()