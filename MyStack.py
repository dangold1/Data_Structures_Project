import copy


class MyStack(object):

    def __init__(self):
        self.stk = []

    def __add__(self, value):
        self.stk.append(value)

    def __delitem__(self, key=None):
        if self.isEmpty():
            return False
        return self.__pop()

    def __contains__(self, key):
        tmp = copy.deepcopy(self)
        while not tmp.isEmpty():
            if tmp.__pop() == key:
                del tmp
                return True
        del tmp
        return False

    def __pop(self):
        return self.stk.pop()

    def isEmpty(self):
        return self.stk == []

    def top(self):
        if not self.isEmpty():
            return self.stk[len(self.stk) - 1]
        else:
            print "Stack is empty"
            return None

    def __len__(self):
        return len(self.stk)

    def __print__(self):
        if self.__len__() == 0:
            print "---Empty Stack---"
        else:
            max = 0
            topline = "-----"

            for i in range(0, len(self.stk)):
                length = len(str(self.stk[i]))
                if max < length:
                    max = len(str(self.stk[i]))

            for i in range(len(self.stk) - 1, -1, -1):
                space = ""
                addspace = max - len(str(self.stk[i]))
                space += " " * addspace
                print"| " + space + str(self.stk[i]) + " |"

            for i in range(1, max):
                topline += "-"
            print topline
