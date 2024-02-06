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
from SkipList import SkipList
import random
import time
import string

def functionalityTests():
    print("Test 1")
    #creating list
    v = SkipList()
    #printing list
    v.print()
    #inserting to list
    v.insert(10)
    v.print()
    v.insert(2)
    v.print()
    v.insert(5)
    v.insert(6)
    v.insert(7)
    v.insert(3)
    v.insert(11, "test")
    v.insert(12)
    v.insert(1)
    v.insert(3)
    v.print()
    #searching for an item in list
    node = v.search(6)
    assert node != None
    node = v.search(20)
    assert node == None
    node = v.search(11)
    assert node.value == "test"
    #deleting from list
    v.delete(11)
    v.delete(7)
    v.delete(1)
    v.print()
    node = v.search(11)
    assert node == None
    v.insert(11)
    node = v.search(11)
    assert node.key == 11
    assert node.value == None
    v.insert(-4)
    v.insert(29)
    v.insert(4)
    v.print()


def largeTests():
    print("Test 2")
    v2 = SkipList()
    for i in range(10000):
        v2.insert(random.randrange(-10000000,10000000))
    v2.print()
    #log2(10000) is 13.2 
    #The odds of getting less than 10 total levels is ~0.0000571177
    print("10000 elements has " + str(v2.levels+1) + " levels.")
    assert v2.levels >= 9 
    #The odds of getting 20 or more levels is very low with my implementation
    assert v2.levels < 20
    v2.insert(30)
    for i in range(1000000):
        v2.insert(random.randrange(-10000000,10000000))
    #The odds of getting less than 17 total levels is ~2.0270897e-7 (higher change with my implementation but still not likely)
    print("1000000 elements has " + str(v2.levels+1) + " levels.")
    assert v2.levels >= 16
    #The odds of getting 30 or more levels is very low with my implementation
    assert v2.levels < 30
    node = v2.search(30)
    assert node.key == 30


def stringTests():
    #Test that sorting by strings also works
    print("Test 3")
    v3 = SkipList()
    for i in range(50):
        s = ""
        for i in range(5):
            s += random.choice(string.ascii_lowercase)
        v3.insert(s)
    v3.print()


def timetesthelper(v, n = 5000, m = 5000, o = 5000):
    b1 = time.process_time() 
    for i in range(n):
        v.insert(random.randrange(0,n))
    insertTime = time.process_time() - b1
    print("Time for Insert " + str(v.advanceLevelProb) + " advanceLevelProb: " + str(insertTime) + " seconds") 
    b2 = time.process_time()
    for i in range(m):
        v.search(random.randrange(0,n))  
    searchTime = time.process_time() - b2
    print("Time for Search " + str(v.advanceLevelProb) + " advanceLevelProb: " + str(searchTime) + " seconds")   
    b3 = time.process_time()
    for i in range(o):
        v.delete(random.randrange(0,n)) 
    deleteTime = time.process_time() - b3
    print("Time for Delete " + str(v.advanceLevelProb) + " advanceLevelProb: " + str(deleteTime) + " seconds")     
    totalTime = time.process_time() - b1
    print("Total time for " + str(v.advanceLevelProb) + " advanceLevelProb: " + str(totalTime) + " seconds")  

def timeTests():
    #In smaller cases and equal ammounts of insert, search and delete, having a lower advanceLevelProb is faster than the default 0.5
    print("Test 4")
    print("Test with thousands of operations")
    v4 = SkipList(0.5) 
    timetesthelper(v4) #0.328125 seconds
    v4 = SkipList(0.25)
    timetesthelper(v4) #0.296875 seconds
    v4 = SkipList(0.10)
    timetesthelper(v4) #0.3125 seconds
    v4 = SkipList(0)
    timetesthelper(v4) #8.109375 seconds
    
    print("Test with hundreds of thousands of operations")
    #In larger cases having closer to a 0.5 advanceLevelProb is optimal
    v4 = SkipList(0.5)
    timetesthelper(v4, 100000, 500000, 10000)  #17.734375 seconds
    v4 = SkipList(0.45)
    timetesthelper(v4, 100000, 500000, 10000) #16.671875 seconds
    v4 = SkipList(0.40)
    timetesthelper(v4, 100000, 500000, 10000) #16.8125 seconds
 

def dictComparison():
    print("Test 5")
    # For inserting and searching dictionaries are faster (O(logN) vs O(1))
    l = []
    for i in range(100000):
        l.append(i)
    random.shuffle(l)
    l = l[0:50000]
    b1 = time.process_time()
    v5 = SkipList(0.45)
    for ele in l:
        v5.insert(ele, "test")
    for ele in l:
        node = v5.search(ele)
    t1 = time.process_time() - b1 #Total time for Skip List is 2.5625 seconds
    print("Total time for Skip List inserting and searching: " + str(t1) + " seconds") 
    b2 = time.process_time()
    d = dict()
    for ele in l:
        d[ele] = "test"
    for ele in l: 
        node = d[ele]
    t2 = time.process_time() - b2 #Total Time for Dictionary is 0.03125 seconds
    print("Total time for Dictionary inserting and searching: " + str(t2) + " seconds")
    
    # For iterating over a range skip lists are faster (O(logN + M) vs O(N)) M-number of elements in range
    start = 5000
    end = 6000
    
    b3 = time.process_time()
    skipResult = []
    r = None 
    s = start
    while r == None:
        r = v5.search(s)
        s += 1
    while r.key < end:
        skipResult.append((r.key, r.value))
        r = r.next[0]
    print(str(len(skipResult)) + " elements in range")
    t3 = time.process_time() - b3 #Total time for Skip List is 0.00 seconds
    print("Total time for Skip List iterating over range: " + str(t3) + " seconds") 
    
    b4 = time.process_time()
    dictResult = dict(filter(lambda ele: ele[0] >= start and ele[0] < end, d.items()))
    print(str(len(dictResult)) + " elements in range")
    t4 = time.process_time() - b4 #Total time for dictionary is 0.109375 seconds
    print("Total time for dictionary iterating over range: " + str(t4) + " seconds") 
    
    
    
    
    
#FunctionalityTests
#Test1 - All basic functionality
functionalityTests()
#Test2 - Inserting lots of elements
largeTests() #slow
#Test3 - using strings as keys
stringTests()
#Test4 - timed comparision
timeTests() #slow 
#Test5 - comparison with Dict
dictComparison()