import TreeNode as Tnode


class BST(object):
    def __init__(self):
        self.root = None

    def __setRoot(self, key):
        self.root = Tnode.TreeNode(key)

    def __add__(self, key):
        if self.root is None:
            self.__setRoot(key)
        else:
            self.__insertNode(self.root, key)

    def __insertNode(self, currentNode, key):
        if key <= currentNode.key:
            if currentNode.left:
                self.__insertNode(currentNode.left, key)
            else:
                currentNode.left = Tnode.TreeNode(key)

        elif key > currentNode.key:
            if currentNode.right:
                self.__insertNode(currentNode.right, key)
            else:
                currentNode.right = Tnode.TreeNode(key)

    def __contains__(self, key):
        return self.__findNodeValue(self.root, key)

    def __findNodeValue(self, currentNode, key):
        if currentNode is None:
            return False
        elif key == currentNode.key:
            return True
        elif key < currentNode.key:
            return self.__findNodeValue(currentNode.left, key)
        else:
            return self.__findNodeValue(currentNode.right, key)

    def __setSuccessor(self, node):
        original = node
        prev = node
        curr = node.left
        while curr != None and curr.right != None:
            prev = curr
            curr = curr.right

        if curr == None:
            print "no successor"
        else:
            node.key = curr.key
            if original.left == curr:
                prev.left = None
            else:
                prev.right = None
            del curr

    def __delitem__(self, key):
        if self.__contains__(key):
            self.__deleteNode(self.root, key)
            return True
        return False


    def __deleteNode(self,node, key,prev=None,direction=None,):
        if node is None:
            return None
        elif node.key == key:
            if node.left is None and node.right is None:
                if node == self.root:
                    self.root = None
                elif node != self.root and direction == 'R':
                    prev.right = None
                elif node != self.root and direction == 'L':
                    prev.left = None
                return None
            elif node.left is None:
                if direction == 'R' and prev != None:
                    prev.right = node.right
                else:
                    prev.left = node.right
                return node.right
            elif node.right is None:
                if direction == 'R':
                    prev.right = node.left
                else:
                    prev.left = node.left
                return node.left
                # return node.left
            else:
                self.__setSuccessor(node)
        elif key < node.key:
            self.__deleteNode(node.left, key, node,'L')

        else:
            # key > node.key
            self.__deleteNode(node.right, key,node, 'R')
        return node

    def __print__(self):
        print "Binary Tree:"
        if self.root == None:
            print "--Empty Tree--"
        else:
            self.root.dfs('BIN')
