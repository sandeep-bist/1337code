class Iterator:
    def __init__(self, nums):
       """
       Initializes an iterator object to the beginning of a list.
       :type nums: List[int]
       """
       pass

    def hasNext(self):
       """
       Returns true if the iteration has more elements.
       :rtype: bool
       """
       pass

    def next(self):
       """
       Returns the next element in the iteration.
       :rtype: int
       """
       pass


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.tmp = None
        self.no_such_element = False
        self.advance_iter()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.tmp
        

    def next(self):
        """
        :rtype: int
        """
        if self.no_such_element:
            return
        res = self.tmp
        self.advance_iter()
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return not self.no_such_element
    
    
    def advance_iter(self):
        """
        """
        if self.iter.hasNext():
            self.tmp = self.iter.next()
        else:
            self.no_such_element = True
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].