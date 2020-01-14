class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value)\
            + ', ' + str(self.weight) + '>'
        return result

def value(item):
    return item.getValue()
#inverse 逆
def weight_inverse(item):
    return 1.0 / item.getWeight
#density 密度
def density(item):
    return item.getValue() / item.getWeight()

def greedy(items, maxWeight, keyFunction):
    """
    """





    
