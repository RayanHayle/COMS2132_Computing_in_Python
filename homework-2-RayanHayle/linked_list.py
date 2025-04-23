class List:
  """
  abstract data type for a list.
  """

  def get(self, k):  
    ''' retrieve element at index k
    '''
    pass

  def insert(self, k,x): 
    ''' insert element x at index k 
    '''
    pass

  def remove(self, k): 
    ''' remove element at index k
    '''
    pass

  def append(self, x): 
    ''' add x at the end of the list
    '''
    pass

  def __len__(self): 
    ''' return the length of the list
    '''
    pass


class DoubleNode:
  
  def __init__(self, element, prev, next):
    self.element = element
    self.prev = prev
    self.next = next
    

class DoubleLinkedList(List): 

  def __init__(self): 
    self._head = DoubleNode(None, None, None)
    self._tail = DoubleNode(None, self._head, None) 
    self._head.next = self._tail
    self.len = 0


  def _get_node(self, k):
    '''internal method to retrieve the node at index k
    '''
   
    if k == -1: 
      return self._head    

    if k <= self.len // 2:   # k in first half
      current = self._head.next
      for i in range(k):
        current = current.next
    else:                   # k in second half    
      current = self._tail.prev
      for i in range(self.len - k -1):
        current = current.prev
      
    return current


  def get(self, k):  
    ''' retrieve element at index k
    '''
    return self._get_node(k).element
   

  def insert(self, k,x): 
    '''insert element x at index k 
    '''
    if k > self.len: 
      raise IndexError("invalid list index") 

    pred = self._get_node(k-1)
    node = DoubleNode(x, None, None) 
    node.next = pred.next 
    pred.next = node
    node.next.prev = node
    node.prev = pred 
    self.len += 1


  def remove(self, k):  
    '''#remove element at index k
    '''
    if k >= self.len:
      raise IndexError("invalid list index")

    node = self._get_node(k)
    pred = node.prev
    succ = node.next

    pred.next = succ
    succ.prev = pred
    node.next = None
    node.prev = None
    self.len -= 1

  def append(self,x): 
    '''add x at the end of the list, aka push
    '''
    self.insert(self.len, x)

  def __repr__(self): 
    if self.len == 0:
      return "[ ]"

    current = self._head.next
    result = "["
    while current.next != self._tail: #for i in range(self.len):
      result = result + str(current.element) + " "
      current = current.next
    result = result + str(current.element) + "]"
    return result 

  def ___str___(self): 
    return repr(self)
  

  def __len__(self): 
    '''return the length of the list
    '''
    return self.len 

  #TODO1
  def find(self, x):  #o(n)
    ''' returns the index of the first occurence of an element equal to x.
    '''
    current = self._head.next  # self._head is  -->  [none,none,none] so skip to the next node
    index = 0

    if current is None:
      return IndexError('out of bound')

    while current != self._tail:  # Stop at the tail, which is also a dummy node pointing to none
          if current.element == x:
              return index
          current = current.next
          index += 1

    return -1
          
  #TODO2
  def flip_pairs(self):  # O(n)
    '''Flips each adjacent pair in the linked list. 
       Note: if the list has an odd number of elements, the last element 
       remains in its original place.'''
    if self.len < 2:
      return 
    current = self._head.next  # Start from the first real node

    # Traverse the list in pairs
    while current is not None and current.next is not self._tail:
        node1 = current
        node2 = current.next

        # swap next and prev: node1.next = node3 , node3.prev = node1
        node1.next = node2.next  
        if node2.next is not None:
            node2.next.prev = node1#  
        
        node2.prev = node1.prev# nodde2 prev --> None  because node1.prev=None
        if node1.prev is not None:
            node1.prev.next = node2 #  item <--- node1.prev
        else:
          self._head.next = node2 

        node2.next = node1
        node1.prev = node2

        current = node1.next  
    print(self)  
     
if __name__ == "__main__":


  li = DoubleLinkedList()
  li.append(5) #0
  li.append(6) #1
  li.append(15)#2
  li.append(20) #3
  li.append(21)#odd

  print('5 at index ', li.find(5))
  print('6 at index ', li.find(6))
  print('15 at index ', li.find(15))
  print('20 at index ',li.find(20))
  print('21 at index ',li.find(21))

  li.flip_pairs()
