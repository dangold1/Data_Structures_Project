
class Pair(object):

    # use this class if associative tree (or map) is needed
    # over 2-3 tree

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        if type(other) is Pair:
            return self.key < other.key
        else:
            return self.key < other

    def __gt__(self, other):
        if type(other) is Pair:
            return self.key > other.key
        else:
            return self.key > other

    def __eq__(self, other):
        if type(other) is Pair:
            return self.key == other.key
        else:
            return self.key == other

    def __str__(self):
        return 'key: %s, value: %s' % (str(self.key), str(self.value))

    def key(self):
        return self.key

    def val(self):
        return self.value


class Node(object):

    def __init__(self, v=None, parent=None):
        self.values, self.valcnt = None, 0
        self.links, self.refcnt = None, 0
        self.parent = parent
        self.__insertValueToNode(v)

    def __str__(self):
        out = []
        if self.values is not None:
            for v in self.values:
                if v is not None:
                    out.append(' %s ' % str(v))
            return ''.join(out)
        else:
            return 'empty'

    def __iter__(self):
        if self.values is not None:
            for item in self.values:
                yield item

    def __add__(self, a):
        self.__insertValueToNode(a)

    def __delitem__(self, key):
        if self.values is None:
            return False
        self.__removeValue(key)

    def __contains__(self, item):
        if self.values is None:
            return False
        return self.contains(item)

    def __getlink(self, a):
        for idx in xrange(self.valcnt):
            if idx is 0:
                if a < self.values[idx]: return idx
            else:
                if self.values[idx - 1] < a < self.values[idx]:  return idx
            if idx == self.valcnt - 1: return idx + 1
        return -1

    def __addLink(self, link):
        if self.links is None: self.links = [None] * 4
        self.links[self.refcnt] = link
        self.refcnt += 1

    def __insertLink(self, idx, anotherNode):
        if self.links is None: self.links = [None] * 4
        if idx == 0:
            self.links[0], self.links[1], self.links[2], self.links[3] = anotherNode, self.links[0], self.links[1], \
                                                                         self.links[2]
        elif idx == 1:
            self.links[1], self.links[2], self.links[3] = anotherNode, self.links[1], self.links[2]
        elif idx == 2:
            self.links[2], self.links[3] = anotherNode, self.links[2]
        else:
            self.links[3] = anotherNode
        self.refcnt += 1

    def __removeLink(self, idx):
        if idx == 0:
            self.links[0], self.links[1], self.links[2], self.links[3] = self.links[1], self.links[2], self.links[
                3], None
        elif idx == 1:
            self.links[1], self.links[2], self.links[3] = self.links[2], self.links[3], None
        elif idx == 2:
            self.links[2], self.links[3] = self.links[3], None
        else:
            self.links[3] = None
        self.refcnt -= 1

    def __rearrangeLinks(self, a):
        """ Rearrange links when adding a new node """
        if self.valcnt != 0:
            if a < self.values[0] and not self.isLeafNode() and self.refcnt < 3:
                # shift all the links to the right when adding new in element
                self.__insertLink(0, None)
            elif self.valcnt == 2 and self.refcnt == 3 and self.values[self.valcnt - 1] > a > self.values[0]:
                # rearrange middle links when adding med element
                self.__insertLink(1, None)

    def __sort3(self, arr, l):
        """ Sort 2 or 3 arrays (very rubost and fast) """
        if l >= 2:
            if arr[0] > arr[1]: arr[0], arr[1] = arr[1], arr[0]
        if l == 3:
            if arr[1] > arr[2]: arr[1], arr[2] = arr[2], arr[1]
            if arr[0] > arr[1]: arr[0], arr[1] = arr[1], arr[0]

    def __insertValueToNode(self, a):
        """ Insert a value into node """
        if a is not None and self.valcnt < 3:
            if self.valcnt is 0: self.values = [None] * 3
            self.__rearrangeLinks(a)
            self.values[self.valcnt] = a
            self.valcnt += 1
            self.__sort3(self.values, self.valcnt)
        return self

    def __removeValue(self, val):
        """ Remove value from node """
        if self.contains(val):
            idx = self.values.index(val)
            if idx == 0:
                self.values[0], self.values[1], self.values[2] = self.values[1], self.values[2], None
            elif idx == 1:
                self.values[1], self.values[2] = self.values[2], None
            else:
                self.values[2] = None
            self.valcnt -= 1
        return self

    def removeLink(self, node):
        """ Remove link from self to another node """
        self.__removeLink(self.getLinkIdx(node))
        return self

    def isConsistent(self):
        """ Check whether the node is consistent, this means it doesn't contain 3 items or 4 links """
        return not (self.valcnt > 2 or self.refcnt > 3)

    def isLeafNode(self):
        """ Check whether this is a leaf node or not """
        return self.refcnt == 0

    def isEmptyNode(self):
        """ Returns true if node doesn't containt any  value """
        return self.valcnt == 0

    def getLink(self, linkIdx):
        """ Get link by its index, return None if there is no link with such an index """
        if linkIdx < self.refcnt:
            return self.links[linkIdx]

    def getLinkIdx(self, destNode):
        """ Get index of the link which points to the given node """
        return self.links.index(destNode)

    def addLink(self, anotherNode):
        """ Add link to another node """
        if anotherNode is not None:
            if self.links is None: self.links = [None] * 4
            idx = self.__getlink(anotherNode.values[0])
            if idx != -1:
                if idx < self.refcnt and self.links[idx] is None:
                    self.links[idx] = anotherNode
                else:
                    self.__insertLink(idx, anotherNode)
                anotherNode.parent = self
        return self

    def contains(self, a):
        """ Check if node contains a given value """
        if self.valcnt is not 0:
            if (self.values[0] > a or self.values[self.valcnt - 1] < a) or a not in self.values:
                return None
            return self.values[self.values.index(a)]

    def chooseChild(self, a):
        """ Choose where to go according to the value a """
        idx = self.__getlink(a)
        if 0 <= idx < self.refcnt:
            return self.links[idx]

    def getItem(self, a):
        if self.contains(a):
            return self.values[self.values.index(a)]
        return None

    def InsertTreeNodesToList(self, lst, space=0):
        if self.links == None:
            lst.append([space, self.values])
        elif self.links[0] == None:
            lst.append([space, self.values])
        else:
            self.links[0].InsertTreeNodesToList(lst, space + 1)
            lst.append([space, self.values])

            for i in range(1, len(self.links)):
                if type(self.links[i]) is Node:
                    self.links[i].InsertTreeNodesToList(lst, space + 1)


class Tree23(object):

    def __init__(self):
        self.root = Node()
        self.lastSearchDepth = 0

    def __iter__(self):
        stack = [self.root]
        while len(stack):
            node = stack.pop()
            yield node
            for j in xrange(node.refcnt - 1, -1, -1):
                stack.append(node.getLink(j))

    def __str__(self):
        """ String representation of a tree (parentheses form) """
        out, stack = [], [self.root]
        while stack:
            node = stack.pop()
            if node == ')':
                out.append(')')
                continue
            out.append('%s(' % str(node))
            stack.append(')')
            for j in xrange(node.refcnt - 1, -1, -1):
                stack.append(node.getLink(j))
        return ''.join(out)

    def __contains__(self, item):
        if self.root.values is None:
            return False
        else:
            return self.contains(item)

    def __add__(self, key):
        self.__insertValue(key)

    def __delitem__(self, key):
        if self.contains(key):
            self.__removeValueFromTree(key)
            return True
        else:
            return False

    def __nextSucc(self, node):
        self.lastSearchDepth += 1
        if not node.isLeafNode():
            return self.__nextSucc(node.links[0])
        return node

    def __find(self, curNode, a):
        if curNode is not None:
            if curNode.contains(a):
                return curNode
            nextNode = curNode.chooseChild(a)
            if nextNode is None:
                return curNode
            self.lastSearchDepth += 1
            return self.__find(nextNode, a)

    def __getLeftSibling(self, node):
        """ Returns left sibling of a node """
        if (node and node.parent) is not None:
            return node.parent.getLink(node.parent.getLinkIdx(node) - 1)

    def __getRightSibling(self, node):
        """ Returns right sibling of a node """
        if (node and node.parent) is not None:
            return node.parent.getLink(node.parent.getLinkIdx(node) + 1)

    def __getSiblings(self, node):
        """ Returns node's siblings """
        # check whether one of our siblings has two items
        lS, rS, lCnt, rCnt = None, None, 0, 0
        if self.__getRightSibling(node) is not None:
            rS = self.__getRightSibling(node)
            rCnt = rS.valcnt
        if self.__getLeftSibling(node) is not None:
            lS = self.__getLeftSibling(node)
            lCnt = lS.valcnt
        return lS, lCnt, rS, rCnt

    def __swapValues(self, node1, a1, node2, a2):
        """ Swap any two values in nodes """
        if node1 is not node2:
            idx1, idx2 = node1.values.index(a1), node2.values.index(a2)
            node1.values[idx1], node2.values[idx2] = node2.values[idx2], node1.values[idx1]

    def __fixNodeRemove(self, node, parent=-1):

        """ Fix deletion """

        global next_node, sib, parent_val, sib_val, child
        if node.isEmptyNode():

            if node is not self.root:

                if parent == -1:
                    parent = node.parent

                if node.isEmptyNode() or not node.isConsistent():

                    lS, lCnt, rS, rCnt = self.__getSiblings(node)
                    rSS, lSS = self.__getRightSibling(rS), self.__getLeftSibling(lS)

                    redistribute = True

                    if (rS or lS) is not None:
                        if rCnt == 2 or (rCnt == 1 and rSS != None and rSS.valcnt == 2):
                            sib = rS
                        elif lCnt == 2 or (lCnt == 1 and lSS != None and lSS.valcnt == 2):
                            sib = lS
                        elif lCnt == 1:
                            sib, redistribute = lS, False
                        elif rCnt == 1:
                            sib, redistribute = rS, False

                    if redistribute:
                        # case 1: redistribute
                        # left and right case
                        if parent.valcnt == 1:
                            if node == parent.getLink(0):
                                parent_val, sib_val = parent.values[0], sib.values[0]
                                child = sib.chooseChild(sib_val - 1)
                            elif node == parent.getLink(1):
                                parent_val, sib_val = parent.values[parent.valcnt - 1], sib.values[sib.valcnt - 1]
                                child = sib.chooseChild(sib_val + 1)
                        else:
                            if sib == parent.getLink(1):
                                # left
                                if node == parent.getLink(0):
                                    parent_val, sib_val = parent.values[0], sib.values[0]
                                    child = sib.chooseChild(sib_val - 1)
                                # right
                                elif node == parent.getLink(2):
                                    parent_val, sib_val = parent.values[parent.valcnt - 1], sib.values[sib.valcnt - 1]
                                    child = sib.chooseChild(sib_val + 1)
                            # middle
                            elif sib == parent.getLink(2):
                                parent_val, sib_val = parent.values[parent.valcnt - 1], sib.values[0]
                                child = sib.chooseChild(sib_val - 1)
                            elif sib == parent.getLink(0):
                                parent_val, sib_val = parent.values[0], sib.values[sib.valcnt - 1]
                                child = sib.chooseChild(sib_val + 1)

                        node.__add__(parent_val)
                        parent.__delitem__(parent_val)
                        parent.__add__(sib_val)
                        sib.__delitem__(sib_val)

                        if not node.isLeafNode():
                            # if this is not a leaf node, redistribute the links also
                            node.addLink(child)
                            sib.removeLink(child)

                        next_node = sib

                    else:
                        # case 2: merge
                        if parent.valcnt == 1:
                            parent_val = parent.values[0]
                        else:
                            if sib == parent.getLink(0):
                                parent_val = parent.values[0]
                            elif sib == parent.getLink(1):
                                if sib == rS:
                                    parent_val = parent.values[0]
                                if sib == lS:
                                    parent_val = parent.values[parent.valcnt - 1]

                        child = node.getLink(0)

                        sib.__add__(parent_val)
                        parent.__delitem__(parent_val)
                        parent.removeLink(node)

                        if not node.isLeafNode():
                            sib.addLink(child)

                        next_node = parent

                self.__fixNodeRemove(next_node, next_node.parent)

            else:
                # root node
                self.root = self.root.getLink(0)

    def __fixNodeInsert(self, node):
        if not node.isConsistent():
            # conflict detected, try to resolve it
            if node.isLeafNode() and node is not self.root:
                # case for leaf node
                node.parent.__add__(node.values[1])
                node.parent.removeLink(node)
                # split the node
                node.parent.addLink(Node(node.values[0], node.parent))
                node.parent.addLink(Node(node.values[node.valcnt - 1], node.parent))
                self.__fixNodeInsert(node.parent)
            else:
                # case for internal node or root node
                if node is not self.root:
                    node.parent.__add__(node.values[1])
                    node.parent.removeLink(node)
                    parent = node.parent
                else:
                    self.root = Node(node.values[1])
                    parent = self.root

                # split the node
                leftNode, rightNode = Node(node.values[0], parent), Node(node.values[node.valcnt - 1], parent)
                parent.addLink(leftNode).addLink(rightNode)
                leftNode.addLink(node.getLink(0)).addLink(node.getLink(1))
                rightNode.addLink(node.getLink(2)).addLink(node.getLink(3))

                if node is not self.root:
                    self.__fixNodeInsert(parent)

    def contains(self, a):
        """ See if we have a given value in our tree """
        node = self.__findNode(a)
        return True if node.contains(a) else False

    def __findNode(self, a):
        """ Find the node which contains the given value """
        self.lastSearchDepth = 0
        return self.__find(self.root, a)

    def __findInorderSucc(self, node, a):
        """ Returns inorder successor of any node """
        self.lastSearchDepth = 0
        if node.isLeafNode():
            return node
        new_node = node.chooseChild(a + 1)
        return self.__nextSucc(new_node)

    def __insertValue(self, a):
        """ Inserts a new value to tree and keeps it balanced """
        if self.root is None:
            self.root = Node(a)
        elif a is not None:
            node = self.__findNode(a)
            res = node.contains(a)
            if res:  return res
            # try to insert a new value into existing node
            node.__add__(a)

            self.__fixNodeInsert(node)
        return self

    def insertList(self, xs):
        """ Insert a list of values into a tree """
        if xs is not None and type(xs) is list:
            for item in xs: self.__insertValue(item)

    def __removeValueFromTree(self, a):
        """ Removes a value from the tree and keeps it balanced """
        node = self.__findNode(a)
        if not node or not node.contains(a):
            return None
        # swap the value we want to delete with its inorder successor (always leaf)
        succ = self.__findInorderSucc(node, a)
        self.__swapValues(node, a, succ, succ.values[0])
        # delete leaf node value
        succ.__delitem__(a)
        # fix tree if needed
        self.__fixNodeRemove(succ)
        return self

    def __print__(self):
        if self.root is None or self.root.values is None:
            print "Empty Tree"
            return False
        lst = []
        depth = 0
        maxspace = 1

        self.root.InsertTreeNodesToList(lst)

        # remove None values
        for i in range(0, len(lst)):
            lst[i][1] = [x for x in lst[i][1] if x is not None]

        # calculate max spacing:
        for i in lst:
            maxspace = max(maxspace, len(str(i[1])))

        # print with spacing
        for i in range(0, len(lst)):
            if lst[i][0] == 0:
                print lst[i][1]
            else:
                print ' ' * (maxspace + 1) * (lst[i][0] - 1) + '|' + '-' * maxspace + str(lst[i][1])
