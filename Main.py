import MyQueue as Q
import MyStack as S
import ClassObject as OBJ
import numpy as np


# Dan Goldshtein - 308193622
# Sagi Bachar - 312485436


def validInteger(userInput):
    while True:
        try:
            int(userInput)
            return int(userInput)
        except ValueError:
            userInput = raw_input("Invalid input. Type number again: ")


def userInputList():
    print "Type numbers, for stop adding numbers type 'end':"
    lst = []
    while True:
        num_string = raw_input()
        if num_string.lower() == 'end':
            break
        else:
            try:
                int(num_string)
            except ValueError:
                print "Invalid input. Type again: "
                continue

            element = int(num_string)
            lst.append(element)
    return lst


def objectMenuCreate():
    print "Choose object to create: "
    print "#1 - Stack program"
    print "#2 - Queue program"
    print "#3 - Linked List program"
    print "#4 - Binary Tree program"
    print "#5 - Avl Tree program"
    print "#6 - Heap program"
    print "#7 - Tree 2-3 program"

    program_number = raw_input()
    program_number = validInteger(program_number)

    while np.logical_or(int(program_number) < 1, int(program_number) > 7):
        program_number = raw_input("Type choice 1-7:\n")
        program_number = validInteger(program_number)
    return program_number


def checkRange(num, start, end):
    num = validInteger(num)
    while np.logical_or(int(num) < start, int(num) > end):
        num = raw_input("Type choice:" + str(start) + '-' + str(end) + "\n")
        num = validInteger(num)
    return str(num)


def SelectObjFromList(objectList=None):
    print "Select object from list:"
    for i in range(0, len(objectList)):
        print str(i + 1) + '. ' + classDict[str(type(objectList[i].obj))]
    print
    item_index = raw_input()
    item_index = validInteger(item_index)
    item_index = checkRange(item_index, 1, len(objectList))

    return int(item_index) - 1


def MenuForObject(objectList, pos):
    key = None
    program_number = '-1'
    while program_number != '0':
        program_number = raw_input("\nWhich action do you want to do for the object: \n"
                                   "1. Add item\s to object\n"
                                   "2. Remove item from object\n"
                                   "3. If item exists in object\n"
                                   "4. Print Data Structure\n"
                                   "0. Back To Menu\n")

        program_number = checkRange(program_number, 0, 4)
        if program_number == '0':
            print "Back To Menu.\n"

        elif program_number == '4':
            objectList[pos].obj.__print__()

        elif program_number == '1' or program_number == '2' or program_number == '3':

            if program_number == '1':
                # add elem option
                key = raw_input("\nWrite number for add:\n")
                key = validInteger(key)
                objectList[pos].obj.__add__(key)
                print "The element " + str(key) + " added!"

            elif program_number == '2':
                # del elem option
                if type(objectList[pos].obj) == S.MyStack \
                        or type(objectList[pos].obj) == Q.MyQueue \
                        or str(type(objectList[pos].obj)) == "<type 'instance'>":
                    key = None
                else:
                    key = raw_input("\nWrite number for delete:\n")
                    key = validInteger(key)

                del_indicator = objectList[pos].obj.__delitem__(key)
                if del_indicator is False:
                    print "Element was not exist!"
                elif del_indicator is None:
                    print "Element was not exist!"
                else:
                    print "Element deleted!"

            else:
                # search elem option
                key = raw_input("\nWrite number for search:\n")
                key = validInteger(key)
                if objectList[pos].obj.__contains__(key):
                    print str(key) + " found!"
                else:
                    print str(key) + " not exist!"


classDict = {"<class 'MyStack.MyStack'>": "Stack",
             "<class 'MyQueue.MyQueue'>": "Queue",
             "<class 'MyLinkedList.LinkList'>": "Linked List",
             "<class 'MyBinaryTree.BST'>": "Binary Tree",
             "<class 'MyAVLTree.AVLTree'>": "AVL Tree",
             "<type 'instance'>": "Heap",
             "<class 'My2_3Tree.Tree23'>": "2-3 Tree"
             }


def showObjectsList(objectList):
    if len(objectList) != 0:
        print "---Current objects in Object-List by index---"
        for i in range(0, len(objectList)):
            objectClass = type(objectList[i].obj)
            objectFromDict = classDict[str(objectClass)]
            print str(i + 1) + '. ' + str(objectFromDict)
        print "---------------------------------------------\n"
    else:
        print "---Create Object for start the program---"


def projectDriver():
    print "***Welcome To Data Structures Algorithms program***\n"
    objectList = []
    program_number = '-1'

    while program_number != '0':

        showObjectsList(objectList)

        program_number = raw_input("Which action do you want to do: \n"
                                   "1.Create object\n"
                                   "2.Select object for more actions\n"
                                   "3.Delete object from list\n"
                                   "0.Exit\n")
        program_number = checkRange(program_number, 0, 3)

        if program_number == '0':
            print "End of program.\n"
            exit(0)

        elif program_number == '1':
            objtype = objectMenuCreate()
            objectList.append(OBJ.ClassObject(objtype))

        elif program_number == '2':
            if objectList == []:
                print "No data structures exists!"
            else:
                pos = SelectObjFromList(objectList)
                MenuForObject(objectList, pos)

        else:
            if objectList == []:
                print "No data structures exists!"
            else:
                pos = SelectObjFromList(objectList)
                tp = type(objectList[pos].obj)
                print classDict[str(tp)] + " has been deleted.\n"
                del objectList[pos]



projectDriver()
