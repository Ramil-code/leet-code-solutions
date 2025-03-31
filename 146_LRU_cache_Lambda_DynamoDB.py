from collections import OrderedDict

class LRUCache(object):
    def __init__(self,capacity:int):
        self.cache=OrderedDict()
        self.capacity =capacity
    
    def get (self,key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    def put(self,key, value):
        if key in self.cache:
            self.cache[key]=key
            
    