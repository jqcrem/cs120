#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    # Your code goes here
    if v == None:
        return 0
    else: 
        v.size = 1 + calculate_sizes(v.left) + calculate_sizes(v.right)
    return v.size

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)

def find_vertex_helper(r, n):

    if (r.left == None or r.left.size <= n/2) and (r.right == None or r.right.size <= n/2):
        return r
    else:
        if (r.left != None and (r.right == None or r.left.size > r.right.size)):
            return find_vertex_helper(r.left, n)
        else:
            return find_vertex_helper(r.right, n)

def find_vertex(r): 
    # Your code goes here
    if r == None:
        return None
    
    return find_vertex_helper(r, r.size)


