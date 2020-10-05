class AVLTree():
    def __init__(self):
        self.root = None
    
    #public method
    def insert(self, val):
        self.root = self._insert(self.root, val)
    
    #private method
    def _insert(self, root, val):
        if root is None:
            return TreeNode(val)
        if val <root.val:
            root.l = self._insert(root.l, val)
        else:
            root.r = self._insert(root.r, val)

        ##Calculate the height
        root.height = max(self.height(root.l), self.height(root.r)) +1
        self._balance(root)
        ##Balance the height, height (L) >height(R)  >1 left heavy <-1 right heavy
        return root

        ##4 rotations: left, right, left-right, right-left
    def _balance(self, root)
        balance_fac = self.height(root.l) - self.height(root.r)
        if (balance_fac > 1):
            print("LEFT HEAVY")
        else:
            print("RIGHT HEAVY")
        return
    def _isLeftHeavy(self, node):
        balance_fac = self.height(root.l) - self.height(root.r)
        if (balance_fac > 1):
            return True
        else:
            return False 
        return root
    def _isRightHeavy(self, node):
        balance_fac = self.height(root.l) - self.height(root.r)
        if (balance_fac < -1):
            return True
        else:
            return False
        return root
    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

class TreeNode():
    def __init__(self, val ,l=None,r=None, height = None):
        self.val = val
        self.l = l
        self.r = r
        self.height = None
    def __str__(self):
        return self.val


if __name__ == "__main__":
