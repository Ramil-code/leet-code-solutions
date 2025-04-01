class MyHashMap:
# Map initialization
    def __init__(self):
        self.size=100
        self.map=[None]*self.size
    
# Create hash    
    def get_hash(self,key):
        return hash(key)%self.size

#Add key & value to the map

    def put(self, key: int, value: int) -> None:
        new_hash=self.get_hash(key)
        key_value=[key,value]

        if self.map[new_hash] is None:
            self.map[new_hash]=[key_value]
        else:
            for pair in self.map[new_hash]:
                if pair[0]==key:
                    pair[1]=value
                    return
            self.map[new_hash].append(key_value)

    def get(self, key: int) -> int:
        key_hash=self.get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0]==key:
                    return pair[1]
        return -1
    
    def remove(self, key: int) -> None:
        key_hash=self.get_hash(key)
        if self.get_hash[key_hash] is not None:
            for i in range (0, len(self.get_hash[key_hash])):
                if self.get_hash[key_hash][i][0]==key:
                    self.get_hash[key_hash].pop(i)
            