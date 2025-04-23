class File:
    def __init__(self, name, size): 
        self.name = name
        self.size = size

    def __repr__(self): 
        return f"{self.name} ({self.size})"


class Directory: 
    def __init__(self, name): 
        self.name = name
        self.children = []
        self.total_size = 0  # Initialize total size for each directory

    def __repr__(self): 
        return self.name

    def add_child(self, child_node):  # Ensure this method exists
        self.children.append(child_node)


class InvalidPath(Exception): 
    def __init__(self, path):
        super().__init__(f"The path '{path}' is invalid or does not exist.")


class FileTree: 

    def __init__(self): 
        self.root = Directory("")
       
    def _find_directory(self, path, node=None):
        if not node: 
            node = self.root

        if path == []: 
            return node
        else: 
            for n in node.children: 
                if n.name == path[0]:
                    return self._find_directory(path[1:], n)

            raise InvalidPath("/" + "/".join(path))  # Raise exception with invalid path
  
    def add_directory(self, path):
        parts = path.split("/")[1:]  # Skip the leading '/'
        if len(parts) == 0:  # If the path is just "/"
            raise InvalidPath(path)

        new_dir_name = parts[-1]
        path_list = parts[:-1]
        new_dir = Directory(new_dir_name)  
        self._find_directory(path_list).add_child(new_dir)
  
    def add_file(self, path, size): 
        parts = path.split("/")[1:]  # Skip the leading '/'
        if len(parts) == 0:  # If the path is just "/"
            raise InvalidPath(path)

        new_file_name = parts[-1]
        path_list = parts[:-1]
        new_file = File(new_file_name, size) 
        self._find_directory(path_list).add_child(new_file)

    def print_tree(self, node=None, indent=0):
        if not node: 
            node = self.root
            print(" " * indent + "+- /")
        else: 
            print(" " * indent + "|")
            print(" " * indent + "+- " + str(node))
        if isinstance(node, Directory): 
            for c in node.children:
                self.print_tree(c, indent + 2)

    def total_size_recursive(self, node=None):
        '''
        Compute the sum of all file sizes in the tree.
        '''
        if not node:
            node = self.root
        
        total = 0
        for child in node.children:
            if isinstance(child, File):
                total += child.size
            else:  # It's a Directory
                total += self.total_size_recursive(child)  # Recursive call
        
        node.total_size = total  # Update the total size for the directory
        return total

    def better_add_file(self, path, size): 
        '''
        Insert the file and update the total size for each subtree. 
        '''
        parts = path.split("/")[1:]  # Skip the leading '/'
        if len(parts) == 0:  # If the path is just "/"
            raise InvalidPath(path)

        new_file_name = parts[-1]
        path_list = parts[:-1]
        new_file = File(new_file_name, size) 
        directory = self._find_directory(path_list)
        directory.add_child(new_file)

        # Update the total size for the directory and its parents
        while directory:
            directory.total_size += size
            directory = None  

if __name__ == "__main__":
    tree = FileTree()
    tree.add_file("/hello.txt", 100)
    tree.add_directory("/subdir")
    tree.add_file("/subdir/nested.txt", 200)
    tree.add_directory("/subdir/another_subdir")
    tree.add_file("/subdir/another_subdir/world.txt", 50)
    tree.add_file("/subdir/nested.txt", 150)
    tree.print_tree()
    '''
        +- /
      |
      +- hello.txt (100)
      |
      +- subdir
        |
        +- nested.txt (200)
        |
        +- another_subdir
          |
          +- world.txt (50)
        |
        +- nested.txt (150)
  '''