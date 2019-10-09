import My2_3Tree as T23
import MyAVLTree as TAVL
import MyBinaryTree as BST
import MyHeap as HP
import MyLinkedList as LST
import MyQueue as Q
import MyStack as S

InitDictionary = {  '0': None,
                    '1': S.MyStack(),
                    '2': Q.MyQueue(),
                    '3': LST.LinkList(),
                    '4': BST.BST(),
                    '5': TAVL.AVLTree(),
                    '6': HP.Heap(),
                    '7': T23.Tree23()
                 }


def InitDict(key):
    return InitDictionary[str(key)]


class ClassObject(object):
    obj = None
    name = ''

    def __init__(self, key):
        if key == 0:
            print "No object created.\n"
        else:
            self.obj = InitDict(str(key))
