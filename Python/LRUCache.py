class LRUCache:
    
    def __init__(self, capacity: int):
        self.a=[]
        self.d={}
        self.cap=capacity  

    def get(self, key: int) -> int:
        if(key in self.a):
            self.a.remove(key)
            self.a.insert(0,key)
            #print("get",self.a)
            return self.d[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.d:
            if key in self.a:
                self.a.remove(key)
        
        if (len(self.a)==self.cap):
                self.a.pop()
        
        self.a.insert(0,key)
        
        self.d[key]=value
        #print("put",self.a)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
