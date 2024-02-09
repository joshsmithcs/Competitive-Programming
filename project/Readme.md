README  
SkipList by Joshua Smith 1528312  
Skip Lists are a data structure similar to Linked Lists, except they contain multiple levels of decreasing size to
make searching faster. In practice, Skip Lists function similarly to balanced binary trees and can be used to
represent the same abstract data types such as dictionaries and ordered lists.
My implementation of Skip List doesn’t allow for duplicates so it can be used as a backend for dictionaries and
sorted sets however other implementations of Skip List could allow duplicates. I chose not to have a maximum
height for my skip list implementation and to cap each node to a level only one greater than any existing nodes
to keep space and time complexity down for smaller data sets (since there can’t be many levels with only one
element before deletion) however this does lead to the number of levels being slightly lower than logN on
average which could marginally increase the time complexity.
Since this is a randomized data structure the running time bound doesn’t depend on the input, but rather on
how well the data is partitioned into the levels. In the best case, the randomized skip list performs as a perfect
skip list which has an O(1) runtime for search (if the element is the head of the highest level) and O(logN) for
insert and delete as traversal will work almost identical to a balanced binary search tree, except if an element
is in a higher level it has to be inserted/deleted at all levels below. In the worst-case all elements are on the
same level which would result in the same time complexity as a linked list which is O(n) for search insert and
delete (as you have to search for the element/spot for the element before inserting or deleting). This is
extremely unlikely when dealing with large data sets. In the average case, there is O(logN) number of levels
and each level has on average 2 steps so insert, delete and search are all O(logN) operations.
Resources I used:  
https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/skiplists.pdf  
https://towardsdatascience.com/data-structures-2-skip-lists-d36b58191d69  
https://www.baeldung.com/cs/skip-lists  
https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/LinkedList.py  
https://www.hni.uni-paderborn.de/fileadmin/Fachgruppen/Algorithmen/Lehre/Vorlesungsarchiv/SS2006/Skiplists.pdf  
Files included:  
SkipList.py - The implementation of Randomized Skip List  
SkipListTest.py - All tests for SkipList.py  
To run the tests run SkipListTest.py
SkipListTest will output a lot of text that describes what is being tested.  
Test 1 has general functionality testing on a small dataset.  
Test 2 shows Skip Lists working on a large data set and tests correctness.  
Test 3 shows that keys can also be strings.  
Test 4 has time tests at different advance level probabilities and dataset sizes.  
Test 5 has time tests compared to dictionaries for different functionality  
