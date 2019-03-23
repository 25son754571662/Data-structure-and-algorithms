class stack:
    def __init__(self):
        self.l=[]
    def is_empty(self):
        return len(self.l)==0
    def pop(self):
        if not self or not self.l or self.l==[]:return
        return self.l.pop(0)
    def push(self,node):
        self.l.insert(0,node)
    def clear(self):
        self.l=[]
        
class queue:
    def __init__(self):
        self.s1=stack()
        self.s2=stack()
    
    def push(self, node):
        self.s1.push(node)
        
    def pop(self):
        if self.s1.is_empty() and self.s2.is_empty():return None
        if self.s2.is_empty():
            while not self.s1.is_empty():
                v=self.s1.pop()
                self.s2.push(v)
            self.s1.clear()
        return self.s2.pop()