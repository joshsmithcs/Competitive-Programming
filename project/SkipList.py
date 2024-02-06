"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  
  https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/skiplists.pdf
  https://towardsdatascience.com/data-structures-2-skip-lists-d36b58191d69
  https://www.baeldung.com/cs/skip-lists
  https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/LinkedList.py
  https://www.hni.uni-paderborn.de/fileadmin/Fachgruppen/Algorithmen/Lehre/Vorlesungsarchiv/SS2006/Skiplists.pdf

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
from random import random
 
class Node:
    #Each element in the SkipList is stored as a Node. Size of the node corelates to its level in the SkipList
    def __init__(self, key, value, level):
        self.key = key
        self.value = value
        self.next =  [None] * (level+1)
class SkipList:
    #Initializes the SkipList
    #prob is an optional parameter that dicates the probability a node moves up levels should be left at 0.5 in most cases
    def __init__(self, advanceLevelProb = 0.5):
        self.head = Node(None, None, -1)
        self.levels = -1
        self.advanceLevelProb = advanceLevelProb
    #Inserts a key into the skiplist
    #key is what the elements are sorted by
    #value is an optional parameter that gets stored with the key in a Node
    def insert(self, key, value = None):
        level = self.__randomLevel()
        if level > self.levels:
            self.levels += 1
            self.head.next.append(None)
        x = self.head
        beforeNew = []
        afterNew = [] 
        #Finds the spot in each level for the Node to go. 
        #If the key already exists replace it and exit
        for i in range(self.levels, -1, -1):
            z = x.next[i]
            while (z != None and key > z.key):
                x = z
                z = z.next[i]
            if z != None and key == z.key:
                z.value = value
                return
            elif level >= i:
                beforeNew.append(x)
                afterNew.append(z)
        #Adds the new Node to each level that it belongs to
        itr=0
        f = Node(key, value, level)
        for lvl in range(level, -1, -1):
            beforeNew[itr].next[lvl] = f
            f.next[lvl] = afterNew[itr]
            itr+=1
    #Deletes the key from the SkipList        
    def delete(self, key):
        x = self.head
        for i in range(self.levels, -1, -1):
            z = x.next[i]
            while (z != None and (key > z.key or z.key == None)):
                x = z
                z = z.next[i]
            if z != None and key == z.key:
                x.next[i] = z.next[i]
    #Finds the key in the Skiplist
    #Returns the node if it exists, and None if it does not
    def search(self, key):
        x = self.head
        for i in range(self.levels, -1, -1):
            z = x.next[i]
            while (z != None and (key > z.key or z.key == None)):
                x = z
                z = z.next[i]
            if z != None and key == z.key:
                return z
        return None
        
    #Prints the SkipList by each level
    #printValues is an optional parameter that if True prints the Node values as well
    def print(self, printValues=False):
        print("SkipList with " + str(self.levels+1) + " levels.")
        if printValues:
            for i in range(self.levels, -1, -1):
                v = self.head.next[i]
                l = []
                c = 0
                while v != None:
                    l.append(str(v.key) + ":" + str(v.value))
                    v = v.next[i]
                    c += 1
                print("level:"+str(i),"length:"+str(c), l)
        else:
            for i in range(self.levels, -1, -1):
                v = self.head.next[i]
                l = []
                c = 0
                while v != None:
                    l.append(v.key)
                    v = v.next[i]
                    c += 1
                print("level:"+str(i),"length:"+str(c), l) 
    #randomLevel is used internally to determine the level of a new Node
    def __randomLevel(self):
        level = 0
        while( self.advanceLevelProb > random() and level <= self.levels):
            level += 1
        return level
    