import copy


class MyQueue(object):

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def __len__(self):
        return len(self.queue)

    def front(self):
        if not self.isEmpty():
            return self.queue[len(self.queue) - 1]
        print "queue is empty"
        return None

    def back(self):
        if not self.isEmpty():
            return self.queue[0]
        print "queue is empty"
        return None

    def __add__(self, value):
        self.queue = [value] + self.queue

    def __delitem__(self, key=None):
            return self.pop_front()

    def __contains__(self, key):
        tmp = copy.deepcopy(self)
        while not tmp.isEmpty():
            if tmp.pop_front() == key:
                del tmp
                return True
        del tmp
        return False

    def pop_front(self):
        if self.__len__() == 0:
            return False
        return self.queue.pop()

    def __print__(self):
        print ' <- ' + str(self.queue[::-1])
