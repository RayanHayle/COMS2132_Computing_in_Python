# COMS 2132 Intermediate Computing in Python 
## Homework 3, Spring 2025
### Due: Friday April 18, 11:59pm 

**Submission:** All submissions must be through GitHub Classroom. Make sure to commit often and remember to push your final version to your remote repository on Github. We will grade the latest version you commit before the due date. 

Homework 2 has a programming part, and a written part. For the written part, please add all answers to the file written.md, either in plain text or using [Markdown formatting](https://www.markdownguide.org/basic-syntax/), which displays nicely in Github. 


### Part 1: Programming (70 pts)


#### 1.1) Tree Map (20 pts)
Recall that Python provides an abstract base class [`collections.abc.MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping) that specifies the abstract data type for a mutable map.
In the [lecture about maps and hash tables](https://github.com/coms2132-sp25/2132-sp25-material/blob/main/lectures/lecture08/08-maps-hash-tables.ipynb), we discussed how to implement a `MutableMapping` using a hash table. 

As an alternative, we could use a binary search tree to implement this functionality. A BST also represents a set of keys (i.e. no duplicates). It allows us to *insert* and *find* keys in expected $O(\log n)$ time (N.B: performance could be improved using self-balancing trees to guarantee the $O(\log n)$ time, even in the worst case. Common self-balancing tree data structures include [Red-Black Trees](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree) and [AVL Trees](https://en.wikipedia.org/wiki/AVL_tree). This was not discussed in class, so for this exercise we will use a non-balancing BST).  

**TODO:** In the file `treemap.py`, implement the class `TreeMap`. Method placeholders have been provided. As a starting point for the BST, you can use the code discussed in class [https://github.com/coms2132-sp25/2132-sp25-material/blob/main/lectures/lecture07/binary_search_tree.py](https://github.com/coms2132-sp25/2132-sp25-material/blob/main/lectures/lecture07/binary_search_tree.py). You should instantiate a binary search tree in the `__init__` method of the `TreeMap` as a data field. 


#### 1.2) k-best Counter (25 pts)
Assume you are given a sequence of values (for example, measurements obtained from a sensor or from a web API, see problem 1.3). Only one value is provided at a time. We do not know how many elements there are in the sequence. In fact, there could be infinitely many. This is also called a *stream* of values. The goal is to be able to retrieve the k-largest elements seen so far at any time.

**TODO:** In the file `kbest.py`, complete the class KBestCounter that keeps track of the $k$-largest elements seen so far in a stream of data using a priority queue / heap. The class should have two methods:

* `def count(self, x)` - process the next element in the set of data. 
* `def kbest(self)` - return a list of the $k$-largest elements that were ever passed to the `count` method. The result does not have to be in a particular order. 

Important: `KBestCounter` objects should only store the $k$-largest items. Other items should not be stored. 

You can use the heap class discussed in class, or you can use the [heapq module](https://docs.python.org/3/library/heapq.html).

The function `test_k_best` generates 100 random numbers and presents each to the KBestCounter. After each 10 numbers, it calls the `kbest` method and prints the 5 largest numbers seen so far. 

#### 1.3) Earthquake Monitor (25 pts) 
(part b of this problem uses the k-best counter class from problem 1.2)

The US Geological Servey (USGS) provides a real-time data feed of seismic events through their [API](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php).

The data is available in various formats, but here we will use their [JSON (JavaScript Object Notation)](https://en.wikipedia.org/wiki/JSON) API. The API returns the full list of earthquake events over the last hour, and the data is updated every minute. 

Take a look at the file `earthquakes.py`. 
The class `Earthquake` represents a single earthquake event, including the time, magnitude (as a float), place (as a plain-text string), longitude, latitude, and depth. Time is represented as the number of seconds since epoch (Jan 1 1970, 00:00:00).

The function `fetch_earthquake_data` accesses the USGS feed and returns a list of `Earthquake` instances. 
The main program currently fetches the raw earthquake data every 60 seconds, and then prints *all* earthquaes returned in the data stream. 

```bash 
$ python earthquakes.py
2025-03-28 11:06:19.780000 -- 0.97 10 km SSE of Pinnacles, CA
2025-03-28 11:03:17.670000 -- 0.93 8 km NNW of The Geysers, CA
2025-03-28 10:54:47.360000 -- 0.71 7 km WNW of Cobb, CA
2025-03-28 10:38:07.220000 -- 2.12 13 km SSE of Volcano, Hawaii
2025-03-28 10:34:20.770000 -- 1.49 9 km NW of The Geysers, CA

2025-03-28 11:29:15.670000 -- 1.06 3 km NE of The Geysers, CA
2025-03-28 11:06:19.780000 -- 0.97 10 km SSE of Pinnacles, CA
2025-03-28 11:03:17.670000 -- 0.93 8 km NNW of The Geysers, CA
2025-03-28 10:54:47.360000 -- 0.71 7 km WNW of Cobb, CA
2025-03-28 10:38:07.220000 -- 2.12 13 km SSE of Volcano, Hawaii
2025-03-28 10:34:20.770000 -- 1.49 9 km NW of The Geysers, CA
```

**TODO**

* a) write the method `print_new_quakes`, which should repeatedly fetch the API data every 60 seconds, but only print _new_ earthquakes in each iteration (if any). The output should be something like this: 

```$ python earthquakes.py
2025-03-28 11:06:19.780000 -- 0.97 10 km SSE of Pinnacles, CA
2025-03-28 11:03:17.670000 -- 0.93 8 km NNW of The Geysers, CA
2025-03-28 10:54:47.360000 -- 0.71 7 km WNW of Cobb, CA
2025-03-28 10:38:07.220000 -- 2.12 13 km SSE of Volcano, Hawaii
2025-03-28 10:34:20.770000 -- 1.49 9 km NW of The Geysers, CA

2025-03-28 11:29:15.670000 -- 1.06 3 km NE of The Geysers, CA
```

You will need to keep track of the earthquakes seen so far in a python `set`. Sets (in Python and other languages) are hashtables that store only keys. Add an appropriate `__hash__(self)` method and `__eq__(self)` method to the `Earthquake` class to ensure that duplicates are detected correctly. 

* b) write the method `print_k_largest(k)`, which should repeatedly fetch the API data every 60 seconds and then print the $k$-largest earthquakes seen in the data stream so far. You can use the k-best counter from problem 1.2 (using `from kbest import KBestCounter`).
You will still need to use a `set` for duplicate detection. 
In order to use the k-best counter, you will need to make your `Earthquake` class comparable by magnitude by implementing appropriate ``_gt__`, ``__lt__``, and ``__eq__`` methods.

### Part 2: Written (30 pts)

#### 2.1) - Hash Tables (15 pts) 

Insert the following keys one-by-one into an initially empty hash table of size 7. Use the hash code function $f(x) = x$ and the compression function $g(x) = x mod 7$.

10, 1, 18, 15, 26, 11, 19

Show the result for
 
* (a) a separate chaining hash table (you do not have to worry about the load factor -- no need to rehash).
* (b) an open addressing hash table using linear probing. 

#### 2.2) - Heaps (15 pts)

(a) Insert the values 8, 12, 14, 11, 9, 16, 10, 7, 6 into an initially empty binary min-heap. Show the heap after each insertion as an array or as a tree. You do not need to show each individual percolation step.

(b) Perform three `delete_min` operations on the final heap from part (a). Show the heap after each `delete_min` as a tree or array.


