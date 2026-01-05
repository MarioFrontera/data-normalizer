class DataSet:
    def __init__(self, values):
        self.values = values

    def mean(self):
        return sum(self.values) / len(self.values) if self.values else None
    
    def minimum(self):
        return min(self.values) if self.values else None
    
    def maximum(self):
        return max(self.values) if self.values else None
    
    