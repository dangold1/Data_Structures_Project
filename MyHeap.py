import numpy as np


class Heap:
    def __init__(self):
        self.heapList = []

    def __len__(self):
        return len(self.heapList)

    def isEmpty(self):
        return len(self) == 0

    def __add__(self, item):
        self.heapList.append(item)
        self.heapifyUp(len(self) - 1)

    def __delitem__(self, key=None):
        return self.extractMax()

    def extractMax(self):
        if len(self) == 0:
            return None
        self.__swap(0, len(self) - 1)
        res = self.heapList.pop()
        self.heapifyDown(0)
        return res

    def __contains__(self, key):
        for item in self.heapList:
            if item == key:
                return True
        return False

    def _left(self, j):
        return 2 * j + 1

    def _hasLeft(self, j):
        return self._left(j) < len(self)

    def _right(self, j):
        return 2 * j + 2

    def _hasRight(self, j):
        return self._right(j) < len(self)

    def _parent(self, j):
        return (j - 1) / 2

    def __swap(self, i, j):
        self.heapList[i], self.heapList[j] = self.heapList[j], self.heapList[i]

    def heapifyUp(self, j):
        while j > 0 and self.heapList[j] > self.heapList[self._parent(j)]:
            self.__swap(j, self._parent(j))
            j = self._parent(j)

    def heapifyDown(self, j):
        while j < len(self):
            if self._hasLeft(j):
                smallChild = self._left(j)
                if self._hasRight(j) and self.heapList[smallChild] < self.heapList[self._right(j)]:
                    smallChild = self._right(j)
                if self.heapList[j] < self.heapList[smallChild]:
                    self.__swap(j, smallChild)
                    j = smallChild
                else:
                    break
            else:
                break

    def __print__(self):
        if len(self) == 0:
            print "Empty heap"
        else:
            lst = self.heapList
            lst = [str(i) for i in lst]
            maxlen = max(len(x) for x in lst)
            pos = len(lst) - 1
            depth = Getdepth(lst)
            pos = 0
            res_mat = []
            res_mat_text = []

            # insert values from list into listoflists
            for i in range(0, depth + 1):
                lstrows = []
                for j in range(2 ** i - 1, 2 ** (i + 1) - 1):
                    if pos < len(lst):
                        lstrows.append(lst[pos])
                        pos += 1
                res_mat.append(lstrows)

            # print each row - depend on its depth
            for i in range(depth, -1, -1):
                RowStr = ''

                for j in range(0, len(res_mat[i])):

                    # print the bottom row normally
                    if i == depth:
                        RowStr += str(res_mat[i][j]) + ' ' * maxlen

                    # print the bottom+1 row in dependent of the last row
                    # (last row may be not full, needed a specific case to handle)
                    elif i == depth - 1:
                        if len(res_mat[i + 1]) > j * 2 + 1:
                            RowStr += InsertVal_Between2PrevVal(RowStr, depth, i, j, res_mat, res_mat_text)
                        else:
                            RowStr += ' ' * 2 * maxlen + '  ' + str(res_mat[i][j])

                    # print the other rows depending on the previous row
                    else:
                        RowStr += InsertVal_Between2PrevVal(RowStr, depth, i, j, res_mat, res_mat_text)
                res_mat_text.append(RowStr)

            for i in range(depth, -1, -1):
                print res_mat_text[i]


def InsertVal_Between2PrevVal(RowStr, depth, i, j, res_mat, res_mat_text):
    findFirst_Prevrow = res_mat_text[depth - i - 1].find(str(res_mat[i + 1][j * 2]))
    findSecond_Prevrow = res_mat_text[depth - i - 1].find(str(res_mat[i + 1][j * 2 + 1]),findFirst_Prevrow + len(res_mat[i + 1][j * 2]) )
    middle = findFirst_Prevrow + (findSecond_Prevrow - findFirst_Prevrow) / 2
    return ' ' * (middle - len(RowStr)) + str(res_mat[i][j])


def Getdepth(lst):
    return int(np.log2(len(lst)))
