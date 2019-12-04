

class BinaryTree:
    """
    A simple binary tree implement for my lerning alghorithm
    reference:
    http://www.ic.daito.ac.jp/~mizutani/python/binary_tree.html#binary_tree_search
    with fixing typo
    """
    def __init__(self, root = None):
        self.value = root
        self.left = None
        self.right = None

    def insert_left(self, insert):
        if self.left == None:
            self.left = BinaryTree(insert)
        else:
            _t = BinaryTree(insert)
            _t.left = self.left
            self.left = _t

    def insert_right(self, insert):
        if self.right == None:
            self.right = BinaryTree(insert)
        else:
            _t = BinaryTree(insert)
            _t.right = self.right
            self.right = _t

    def add_left(self, add):
        if self.left == None:
            self.left = BinaryTree(add)
        else:
            self.left.add_left(add)

    def add_right(self, add):
        if self.right == None:
            self.right = BinaryTree(add)
        else:
            self.right.add_right(add)

    def get_right(self):
        return self.right
        
    def get_left(self):
        return self.left

    def put_root(self, obj):
        self.value = obj

    def get_root(self):
        return self.value

    #This method is imcomplete
    # def print_content(self):
    #     print(self.get_root())
    #     if self.left != None:
    #         self.left.print_content()
    #     if self.right != None:
    #         self.right.print_content()
        # if self.

    def  post_order_search(self):
        if self != None:
            if self.left:
                self.left.post_order_search()
            if self.right:
                self.right.post_order_search()
            print(self.get_root(), end="")




def post_order_search(btree):
    if btree != None:
        post_order_search(btree.get_left())
        post_order_search(btree.get_right())
        print(btree.get_root(), end="") 
        



r = BinaryTree()
r.put_root(3)
r.insert_left(4)
r.insert_right(6)
r.insert_right(7)
r.insert_left(5)
post_order_search(r)
r.post_order_search()


r = BinaryTree()
r.put_root(3)
r.add_left(4)
r.add_right(6)
r.add_right(7)
r.add_left(5)
post_order_search(r)
r.post_order_search()



