class Node:

    def __init__ (self, key):
        self.data = key
        self.left_child = None
        self.right_child = None

class BST:

    def __init__ (self):
        self.root= None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
        else:
            self._insert(self.root, key)

    def _insert (self, curr, key):
        if key.data < curr.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self._insert(curr.left_child,key)
        else:
            if curr.right_child == None:
                curr.right_child = key
            else:
                self._insert(curr.right_child, key)

    def in_order_traversial(self):
        self._in_order_trasversial(self.root)


    def _in_order_trasversial(self, curr):
        if curr:
            self._in_order_trasversial(curr.left_child)
            print(curr.data)
            self._in_order_trasversial(curr.right_child)

    def find_val(self, key):
        self._find_val(self.root, key)

    def _find_val(self, curr, key):
        if curr:
            if key == curr.data:
                print("FOUND")
            elif key < curr.data:
                self._find_val(curr.left_child, key)
            elif key > curr.data:
                self._find_val(curr.right_child, key)
        else:
            print("not found")

    def min_right_subtree(self, curr):
        if curr.left_child == None:
            return curr
        else:
            self.min_right_subtree(curr.left_child)

    def delete_val(self, key):
        self._delete_val(self.root, None, None, key)

    def _delete_val(self, curr, prev, is_left, key):
        if curr:
            if curr.data == key:
                if curr.right_child and curr.left_child:
                    min_child = self.min_right_subtree(curr.right_child)
                    curr.data = min_child.data
                    self._delete_val(curr.right_child, curr, False, min_child.data)

                elif curr.left_child == None and curr.right_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = None
                        else:
                            prev.right_child = None
                    else:
                        self.root = None
                elif curr.left_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.right_child
                        else:
                            prev.right_child = curr.right_child
                    else:
                        self.root = curr.right_child
                else:
                    if prev:
                        if is_left:
                            prev.left_child = curr.left_child
                        else:
                            prev.right_child = curr.left_child
                    else:
                        self.root = curr.left_child

            elif curr.data < key:
                is_left = False
                self._delete_val(curr.right_child, curr, is_left, key)
            elif curr.data > key:
                is_left = True
                self._delete_val(curr.left_child, curr, is_left, key)
        else:
            print("not found so cant delete")


tree = BST()
tree.insert("F")
tree.insert("C")
tree.in_order_traversial()
tree.delete_val("F")
tree.in_order_traversial()
