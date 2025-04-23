Answer to written portion goes into this file.
### 2.1) - List (5 pts)
- To implement a `reverse()` Methods I would first establish a doubly-linked list with 0(1) time complexity 
- I would have self.head pointing to the first node and self.tail to the last node
- I would have self.prev and self.next to swap them in postion for each node 
- Finally swap self.head and self.tail to complete the reversal process
- The time complexity at O(1) because only self.head and self.tail is modified 
```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None  
        self.tail = None  
    
    def Reverse(self):
      #the end goal is:
      self.head = self.tail
      self.tail = self.head
```

### 2.2) - Stacks and Queues (10 pts)
  #### a)
    - Dequeue from queue to stack 
    - first in first out: q = ['M', 'E', 'L', 'O', 'N', 'S'] and append to s stack 
    1. Dequeue(q) ' → s = ['M']
    2. Dequeue(q)  → s = ['M', 'E']
    3. Dequeue(q)  → s = ['M', 'E', 'L']
    4. Dequeue(q)  → s = ['M', 'E', 'L', 'O']
    5. Dequeue(q)  → s = ['M', 'E', 'L', 'O', 'N']
    6. Dequeue(q)  → s = ['M', 'E', 'L', 'O', 'N', 'S']
    7. li = s.pop() and li.append()  
    8. li = ['S', 'N', 'O', 'L', 'E', 'M']
    9. print(li[::-1] ) reverse li 
    10. This is how it looks in code 
        ```Python 
          q = ['M', 'E', 'L', 'O', 'N', 'S']
          s = []
          li = []

          # Dequeue and push to stack
          s.append(q.pop(0))  # s = ['M']
          s.append(q.pop(0))  # s = ['M', 'E']
          s.append(q.pop(0))  # s = ['M', 'E', 'L']
          s.append(q.pop(0))  # s = ['M', 'E', 'L', 'O']
          s.append(q.pop(0))  # s = ['M', 'E', 'L', 'O', 'N']
          s.append(q.pop(0))  # s = ['M', 'E', 'L', 'O', 'N', 'S']

          # Pop from stack and append to li
          li.append(s.pop())  # li = ['S']
          li.append(s.pop())  # li = ['S', 'N']
          li.append(s.pop())  # li = ['S', 'N', 'O']
          li.append(s.pop())  # li = ['S', 'N', 'O', 'L']
          li.append(s.pop())  # li = ['S', 'N', 'O', 'L', 'E']
          li.append(s.pop())  # li = ['S', 'N', 'O', 'L', 'E', 'M']

          # Reverse the list to get the desired order
          li = li[::-1]  # li = ['L', 'E', 'M', 'O', 'N', 'S']`
        ```


  #### b)
  - You cannot rearrange ['D','E','S','P','A','I','R'] into ['P','R','A','I','S','E','D'] using **stack LAFO** 
  - Stack can only pop from the top and push to the top meaning it cannot be reordered
  - Pop from the top will return each letter backwords not rearranged
  - D can be poped off and then pop off everything else off, and then push it however that would not change the sequence of the letters
    - it will only reverse it to ['R','I','A','P','S','E','D']


  #### 2.3) - Tree Traversals (10 pts)
  - Preorder Traversal: Root → Left → Right
  - Postorder Traversal: Left → Right → Root

  - Preorder = 1, 2 , 3 ---> Root = 1, left  =2, child of left = 3
  - Postorder = 3, 2, 1 ---> Root = 1, right = 2 child of right = 3
  - strcture is different  

  ### 2.4) - Binary Search Trees (15 pts)
  ##### a)
  - 4,2,1,6,3,5
  1. root: 4
  2. 2 < 4,  2 goes left  of 4
  3. 1 <2  will go to rigth of 2
  4. 6 > 4, 6 goes to right of 4
  5. 3 <4 but 3>2 so 3 will go the left of 2
  6. 5 > 4, but 5 <6, so 5 will go to left of 6
  ```Python 
       4 - root
      / \
     2   6
    / \  /
   1   3 5
  ````

##### b)
- **Best case** is a balanced tree and insert at root wich will give O(1) because you won't need to traverse throgh half the tree
- **Worst case** is a non-balanced being it becomes a list each new number will be right of prevous smaller number. this is worst case because search becomes o(n) 
```Python 
     1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
````

##### c)
- Source1: https://www.geeksforgeeks.org/tree-sort/
- Source2: https://www.geeksforgeeks.org/complexity-different-operations-binary-tree-binary-search-tree-avl-tree/

-- **Best case running time for insert**: `O(log N)`
- **Worst case running time for insert**: `O(N)`
- **Best case running time for sorting using BST**: `O(N log N)`
- **Worst case running time for sorting using BST**: `O(N^2)`