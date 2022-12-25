class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mins = [] 
        self.data = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.data)==0: 
            self.mins.append(x)
        else: 
            if x<self.mins[-1]:
                self.mins.append(x)
            else:
                self.mins.append(self.mins[-1])
        self.data.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        self.mins.pop(-1) 
        return self.data.pop(-1)
        
        

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]
