class BinaryTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.val:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)


    def traversePreOrder(self, root):
        #Root, L, R
        ##base condition 
        if root is None:
            return
        print(root.v)
        self.traversePreOrder(root.l)
        self.traversePreOrder(root.r)

    def traverseInOrder(self, root):
        #L,Root, R
        ##base condition
        if root is None:
            return
        self.traverseInOrder(root.l)
        print(root.v)
        self.traverseInOrder(root.r)

    def traversePostOrder(self, root):
        ## Rl root
        ##base condition
        if root is None:
            return
        self.traversePostOrder(root.l)
        self.traversePostOrder(root.r)
        print(root.v)



    #def find(self, val):


class Node():
    def __init__(self, val):
        self.val  = val
        self.l = None
        self.r = None

    

if __name__ == "__main__":
    tree = BinaryTree()
    tree.add(7)
    tree.add(4)
    tree.add(9)
    tree.add(1)
    tree.add(6)
    tree.add(8)
    tree.add(10)
    print("Done")