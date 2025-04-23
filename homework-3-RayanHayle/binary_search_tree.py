import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

#  def find_below_me(self, x): 
#  
#    if x < self.data: 
#      return self.left.find_below_me(x)
#    elif x > self.data: 
#      return self.right.find_below_me(x)
#    else: 
#      return self 

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0  # change 1

    def _get_node(self, node, x):
      """
    Find the node with value x in the subtree rooted in node, if it exists. 
    Otherwise, return None
    """
    # change 2: add ._key to data 
      if node is None:
          return None
      
      if x < node.data._key:
          return self._get_node(node.left, x)
      elif x > node.data._key:
          return self._get_node(node.right, x)
      else:
          return node

   
    def find(self, x): # find is a "driver" method that calls the recursive method _get_node on the root 
      found = self._get_node(self.root, x)
      if found: 
        return found.data._value    #change 2: add ._value to data

      else: 
        raise Exception(f"{x} not in the tree")


    def _insert_helper(self, node, x):
        
        if node is None:
            return Node(x) #change 3: creat new node here instead of Node(x, none, none)
        
        if x < node.data:
            node.left = self._insert_helper(node.left, x)
        elif x > node.data:
            node.right = self._insert_helper(node.right, x)

        else:
          raise Exception(f"{x} was already in the tree")

        return node


    def insert(self, x):
    #if self.root == None: # tree was empty
      #  self.root = Node(x, None, None) # single root node, no children 
      #  return 
        self.root = self._insert_helper(self.root, x)

        self.size += 1 # change 4: for len tracking 


    def __len__(self):
        return self.size
    
    #TODO CHANGE 5: 

    '''keep track of the number of nodes in 
    the tree and to retrieve a list of elements (using an in-order traversal)'''

    def __iter__(self):
      # Source: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
      # not identical, gave idea to use a stack 
        keys = []  
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            keys.append(current.data._key)  
            current = current.right
        
        return iter(keys)  
           
if __name__ == "__main__":

  x = "train"


  word_tree = BinarySearchTree()
  word_list = []
  with open('wordle.txt','r') as f:
    for line in f: 
      word = line.strip()
      word_list.append(word)

  random.shuffle(word_list)
  for word in word_list: 
    word_tree.insert(word)

  print(word_tree.find("train")) 
  print(word_tree.find("lyric"))

