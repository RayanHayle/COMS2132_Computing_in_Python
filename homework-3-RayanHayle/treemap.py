from collections.abc import MutableMapping 
from binary_search_tree import BinarySearchTree   # could use the version developed in class, but you may want to make 
                                                   # some changes, for example to keep track of the number of nodes in 
                                                   # the tree and to retrieve a list of elements (using an in-order traversal)

class TreeMap(MutableMapping):
    ''' map implemented using a binary search tree '''

    class _Item:
        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)
        
        def __lt__(self, other):
            return self._key < other._key
#---------------------
#YT Source: https://www.youtube.com/watch?v=JSNJig121-s 
    def __init__(self):
        ''' create an empty map '''
        self.tree = BinarySearchTree()


    def __setitem__(self, k, v):
        #TODO 1: insert(method) from BinarySearchTree()
        newNode = self._Item(k, v)
        self.tree.insert(newNode) 

    def __delitem__(self, k):
        raise NotImplementedError("Deletion not supported")

    def __len__(self):
        return len(self.tree)

    def __getitem__(self, k):
            
            #TODO 2: return value of key, and error catching 
        
            node = self.tree.find(k)  # find function from BinarySearchTree()
            if node is None: 
                raise KeyError(f"Key {k} is not found!")
            return node     

    def __iter__(self):
        #TODO 3
        # an easy way to do this is to get a list of all keys in the map using an 
        # in-order traversal, then return iter(keys)
        # __iter__ in BinarySearchTree()
        return iter(self.tree)


def main():
    tree_map = TreeMap()

    # Insert 
    tree_map['apple'] = 5
    tree_map['orange'] = 7
    tree_map['Rayan'] = 21

    # key
    print("Key:", tree_map['apple'])  
    print("Key:", tree_map['orange']) 
    
  
    print("Length:", len(tree_map))  

    
    for key in tree_map:
            print(f"Key: {key}, Value: {tree_map[key]}")


if __name__ == "__main__":
    main()

    '''
  Key: 5
  Key: 7
  Length: 3
  Key: Rayan, Value: 21
  Key: apple, Value: 5
  Key: orange, Value: 7'''