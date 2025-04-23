#kbest.py 25 points
import heapq # recommended, but you can also use the heap implementation discussed in class

import random # for testing

class KBestCounter:

  def __init__(self,k):
    self.k = k
    self.heap = []
    pass

  def count(self, x): #TODO
    #Source 1:https://docs.python.org/3/library/heapq.html
    #source 2: https://www.geeksforgeeks.org/max-heap-in-python/

    '''you get a list of values 
      and a key value --> k
      you accept  add each item if list[index] < k and when its not you compare it to head value 
      if keep is less replace it''' 


    if len(self.heap) < self.k:
            heapq.heappush(self.heap, x)
    else:
        if x > self.heap[0]: 
            #pop of the smaller number in compariion 
            heapq.heappushpop(self.heap, x)


  def kbest(self):#TODO
    """return a list of the $k$-largest elements that were ever passed to the `count` method."""
    return sorted(self.heap, reverse=True) # largest element first


def test_k_best():

  counter = KBestCounter(5)

  for i in range(1,101):
    next_value = random.randint(1,1000)
    counter.count(next_value)
    if i % 10 == 0:
      print(f"Current k-largest: {counter.kbest()}")
      

if __name__ == "__main__":

  test_k_best()
  '''
  python kbest.py
  Current k-largest: [983, 906, 875, 852, 694]
  Current k-largest: [983, 968, 906, 875, 869]
  Current k-largest: [983, 968, 939, 906, 899]
  Current k-largest: [994, 983, 968, 939, 906]
  Current k-largest: [994, 983, 978, 978, 968]
  Current k-largest: [994, 983, 978, 978, 968]
  Current k-largest: [994, 983, 978, 978, 968]
  Current k-largest: [994, 983, 978, 978, 968]
  Current k-largest: [994, 983, 978, 978, 968]
  Current k-largest: [997, 994, 983, 978, 978]
  '''
    
