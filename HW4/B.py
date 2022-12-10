class ReverseIter:
     def __init__(self, listt):
         self.info = listt
         self.index = len(self.info)
     def __iter__(self):
         return self
     def __next__(self):
         if self.index == 0:
             raise StopIteration
         self.index = self.index - 1
         return self.info[self.index]

##it = ReverseIter([10, 54, 12, 0])
##print(next(it))
##print(next(it))
