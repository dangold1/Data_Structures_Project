import MyLinkedList_Node as N


class LinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    # Adding Functions

    def __add__(self, value):
        self.__add(value)

    def __delitem__(self, key):
        if self.__contains__(key):
            self.__deleteValueFromList(key)
            return True
        else:
            return False

    def __contains__(self, value):
        return self.__Contains(value)

    def __add(self, value, HeadOrTail='T'):
        node = N.ListNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if HeadOrTail == 'T':
                self.addTail(node)
            elif HeadOrTail == 'H':
                self.addHead(node)
            else:
                pass

    def addTail(self, node):
        self.tail.Next = node
        node.Prev = self.tail
        self.tail = self.tail.Next

    def addHead(self, node):
        self.head.Prev = node
        node.Next = self.head
        self.head = self.head.Prev

    # Deleting Functions

    def deleteHeadOrTail(self, HeadOrTail=''):
        if HeadOrTail == '':
            self.emptyList()
        else:
            if HeadOrTail == 'H':
                self.deleteHead()
            elif HeadOrTail == 'T':
                self.deleteTail()
            else:
                pass

    def emptyList(self):
        while self.head.Next != None:
            self.deleteHeadOrTail('H')
        self.deleteHeadOrTail('H')

    def isEmpty(self):
        return self.head is None

    def deleteHead(self):
        if self.head == None:
            pass
        elif self.head.Next == None:
            tmp = self.head
            self.head = None
            del tmp
        else:
            tmp = self.head
            self.head = self.head.Next
            self.head.Prev = None
            del tmp

    def deleteTail(self):
        if self.head == None:
            pass
        elif self.head.Next == None:
            tmp = self.head
            self.head = None
            del tmp
        else:
            tmp = self.tail
            self.tail = self.tail.Prev
            self.tail.Next = None
            del tmp

    def deleteNodeFromList(self, node):
        if node == self.head:
            self.deleteHead()
        elif node == self.tail:
            self.deleteTail()
        else:
            node.Prev.Next = node.Next
            node.Next.Prev = node.Prev
            del node

    def __deleteValueFromList(self, value):
        tmp = self.head
        while tmp != None:
            if tmp.value == value:
                newpos = tmp.Next
                self.deleteNodeFromList(tmp)
                tmp = newpos
            else:
                tmp = tmp.Next
        return value

    def __Contains(self, value):
        tmp = self.head
        while (tmp != None):
            if tmp.value == value:
                return True

            tmp = tmp.Next
        if tmp == None:
            return False

    # Printing Functions
    def __print__(self):
        output = ''
        if self.head != None:
            tmp = self.head
            while tmp.Next != None:
                output += str(tmp.value)
                output += ' <-> '
                tmp = tmp.Next
            output += str(tmp.value)
        else:
            output += '--Empty List--'
        print output

    def Count(self, value=''):
        count = 0
        tmp = self.head

        while (tmp != None):
            if value == '':
                count += 1
            else:
                if tmp.value == value:
                    count += 1
            tmp = tmp.Next
        if value == '':
            print "the list contains " + str(count) + " values"
        else:
            print "the value " + str(value) + " appears in the list " + str(count) + " time/s"
