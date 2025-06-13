class setNumbers:
    set= []
    def __init__(self, set=None):
        self.set=set if set is not None else []
    
    def sumSet(self):
        return sum(self.set)
    
    def average(self):
        if not self.set:
            return 0
        else:
            return sum(self.set)/len(self.set)
        
    def maxValue(self):
        if not self.set:
            return None
        else:
            return max(self.set)
        
    def minValue(self):
        if not self.set:
            return None
        else:
            return min(self.set)


    


        
