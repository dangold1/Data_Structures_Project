
class TreeNode(object):
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None


    def preorder(self):
        if self:
            print str(self.key) + ' '
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
                print str(self.key) + ' '
            if self.right:
                self.right.inorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print str(self.key) + ' '


    def dfs(self, class_ind, space='', RorL=''):
        if self is None:
            return ''
        else:
            if RorL == 'R':
                print space + 'R--' + str(self.key)
            elif RorL == 'L':
                print space + 'L--' + str(self.key)
            else:
                print space + str(self.key)

            if class_ind == 'AVL':
                if self.left.node != None:
                    self.left.node.dfs('AVL', space + '    ', 'L')

                if self.right.node != None:
                    self.right.node.dfs('AVL', space + '    ', 'R')

            elif class_ind == 'BIN':
                if self.left != None:
                    self.left.dfs('BIN', space + '    ', 'L')

                if self.right != None:
                    self.right.dfs('BIN', space + '    ', 'R')
            else:
                pass
