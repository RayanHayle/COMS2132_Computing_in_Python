
## 2.1) Hash Tables (15 pts)

**2.1 A**
 - List: [ 10, 1, 18, 15, 26, 11, 19]
 1.  Mod each number by 7 to give it an index box


| Index | Value      |
|-------|------------|
| 0     | -          |
| 1     | 1, 15      | 
| 2     |            |
| 3     | 10         |
| 4     | 18, 11     |
| 5     | 26, 19     |
| 6     |            |

**2.1 B**

2. Drop last item into index below 

| Index | Value  |
|-------|---------|
| 0     | 19    |
| 1     | 1     |
| 2     |15     |
| 3     | 10    |
| 4     | 18   |
| 5     | 26     |
| 6     | 11     |


---

## 2.2) - Heaps (15 pts)


**2.2 A**

- [8, 12, 14, 11, 9, 16, 10, 7, 6 ] into heap one at a time
- percolate means the child has to be always smaller than parent - min heap
- min heap: root smallest, parent less than child, and child go left or right no based on size

- 8: [Root: 8]
- 12: [Root: 8, Left: 12]
- 14: [Root: 8, Left: 12, Right: 14]
- 11: [Root: 8, Left: 12, Right: 14, Left of 12: 11]
- 9: [Root: 8, Left: 12, Right: 14, Left of 12: 11, Right of 12: 9]
- 16: [Root: 8, Left: 12, Right: 14, Left of 12: 11, Right of 12: 9, Left of 14: 16]
- 10: [Root: 8, Left: 12, Right: 14, Left of 12: 11, Right of 12: 9, Left of 14: 16, Right of 14: 10]
- 7: [Root: 7, Left: 8, Right: 14, Left of 8: 12, Right of 8: 9, Left of 14: 16, Right of - 14: 10]
- 6: [Root: 6, Left: 7, Right: 14, Left of 7: 8, Right of 7: 9, Left of 14: 16, Right of 14: 10, Left of 10: 11]

```
        6
       / \
      7   14
     / \  / \
    8  9 16 
   / \
  10  11
  ```
**2.2 B**
- Perform three delete_min operations

 **--Remove 1--**
1. remove Root : 6
2. Root is last element: 11 --> swap with smallest child: 7

```
        7
       / \
      11   14
     / \  / \
    8  9 16 
   / \
  10 
 ```

 **--Remove 2--**
1. remove Root: 7
2. Root is last element: 19 --> swap with smallest child: 8
```
        8
       / \
      10   14
     / \  / \
    11  9  
 ``` 
 
   **--Remove 3--**
1. remove Root: 8
2. Root is last element: 9
 ```

        9
       / \
      10   14
     / \  / \
    11   
  
 ```