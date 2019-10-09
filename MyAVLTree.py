
import TreeNode as N


class AVLTree(object):
    def __init__(self, key=None):
        self.node = None
        self.height = -1
        self.balance = 0

        if key != None:
            self.__add__(key)

    def is_leaf(self):
        return (self.height == 0)

    def __add__(self, key):
        self.__insert(key)

    def __insert(self, key):
        tree = self.node
        newnode = N.TreeNode(key)

        if tree == None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()

        elif key < tree.key:
            self.node.left.__insert(key)

        elif key > tree.key:
            self.node.right.__insert(key)

        self.__rebalance()

    def __rebalance(self):
        '''
        __rebalance a particular (sub)tree
        '''
        # key inserted. Let's check if we're balanced
        self.__update_heights(False)
        self.____update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.__lrotate()  # we're in case II
                    self.__update_heights()
                    self.____update_balances()
                self.__rrotate()
                self.__update_heights()
                self.____update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.__rrotate()  # we're in case III
                    self.__update_heights()
                    self.____update_balances()
                self.__lrotate()
                self.__update_heights()
                self.____update_balances()

    def __rrotate(self):
        # Rotate left pivoting on self
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def __lrotate(self):
        # Rotate left pivoting on self
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def __update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.__update_heights()
                if self.node.right != None:
                    self.node.right.__update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def ____update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.____update_balances()
                if self.node.right != None:
                    self.node.right.____update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def __delitem__(self, key):
        if self.__contains__(key):
            self.__delete(key)
            return True
        return False

    def __delete(self, key):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node != None:
            if self.node.key == key:
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None  # leaves can be killed at will
                # if only one subtree, take that
                elif self.node.left.node == None:
                    self.node = self.node.right.node
                elif self.node.right.node == None:
                    self.node = self.node.left.node

                # worst-case: both children present. Find logical successor
                else:
                    replacement = self.__logical_successor(self.node)
                    if replacement != None:  # sanity check
                        self.node.key = replacement.key

                        # replaced. Now delete the key from right child
                        self.node.left.__delete(replacement.key)

                self.__rebalance()
                return
            elif key < self.node.key:
                self.node.left.__delete(key)
            elif key > self.node.key:
                self.node.right.__delete(key)

            self.__rebalance()
        else:
            return

    def __logical_predecessor(self, node):
        '''
        Find the biggest keyd node in LEFT child
        '''
        node = node.left.node
        if node != None:
            while node.right != None:
                if node.right.node == None:
                    return node
                else:
                    node = node.right.node
        return node

    def __logical_successor(self, node):
        '''
        Find the smallese keyd node in RIGHT child
        '''
        node = node.left.node
        if node != None:  # just a sanity check

            while node.right != None:
                if node.right.node == None:
                    return node
                else:
                    node = node.right.node
        return node

    def __check_balanced(self):
        if self == None or self.node == None:
            return True

        # We always need to make sure we are balanced
        self.__update_heights()
        self.____update_balances()
        return ((abs(self.balance) < 2) and self.node.left.__check_balanced() and self.node.right.__check_balanced())

    def inorder_traverse(self):
        if self.node == None:
            return []

        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    def __contains__(self, item):
        return self.__findNodeValue(self,item)

    def __findNodeValue(self, currentNode, key):
        if currentNode.node is None:
            return False
        elif key == currentNode.node.key:
            return True
        elif key < currentNode.node.key:
            return self.__findNodeValue(currentNode.node.left, key)
        else:
            return self.__findNodeValue(currentNode.node.right, key)


    def __print__(self):
        print "AVL Tree:"
        if self.node == None:
            print "--Empty Tree--"
        else:
            self.node.dfs('AVL')
