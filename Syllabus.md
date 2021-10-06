## Methodoly

2. 学习数据数据结构topic
3. 按特定topic刷题(DFS, BFS, HashMap)  5 + 10 + 15
3. 总结题目背后算法知识





## Order

1. Array and String
2. Arrays
3. Queue and Stack
4. Hash Table
5. Binary Search
6. Recursion I
7. Recursion II
8. Linked List
9. Binary Tree
10. Binary Search Tree
11. Trie
12. N-ary tree
13. Decision Tree
14. Machine Learning



Recursion, linked list, Queue and Stack,  binary tree, bst, heap&grap algorithm, dfs, hash table, string, bit operations, dp, 



## Array and String

### Goal

1. Understand the differences between `array` and `dynamic array`;
2. Be familiar with `basic operations` in the array and dynamic array;
3. Understand `multidimensional arrays` and be able to use a `two-dimensional array`;
4. Understand the concept of `string` and the different features string has;
5. Be able to apply the `two-pointer technique` to practical problems.

### Problems

1.  [Find Pivot Index](https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/) ([1991- Find the Middle Index in Array](https://leetcode.com/problems/find-the-middle-index-in-array/) )
    - left = right( sum - left - current)
2.  [Largest Number At Least Twice of Others](https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/)
3.  [Plus One](https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/)
4.  *[Diagonal Traverse](https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/)
    - the sum of indices on all diagonals are equal
    - direction: %2
5.  [54 - Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
6.  [Pascal's Triangle](https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1170/)
7.  [Add Binary](https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1160/)
8.  [Implement strStr()](https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/)
9.  [Longest Common Prefix](https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/)
10.  [Reverse String](https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1183/)
11.  [Array Partition I](https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1154/)
12. [167-Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
    - two-pointer
13. [Remove Element](https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1151/)
14. [Max Consecutive Ones](https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1301/) (Sliding window problem)
15. [209 - Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) (Sliding window problem)
16.  [Pascal's Triangle II](https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1171/)
17.  [Reverse Words in a String](https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1164/)
18.  [Reverse Words in a String III](https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1165/)
19.  [Remove Duplicates from Sorted Array](https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1173/)
20.  [Move Zeroes](https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1174/)
### Conclusion

1. **Two-pointer Technique**
   - one starts from the first element and another starts from the last element
     - 10, 11, 12
   - one is still used for the iteration while the second one always points at the position for next addition
     - 13, 14, 15
   - [Slow-pointer and fast-pointer problem in Linked List](https://leetcode.com/explore/learn/card/linked-list/214/linked-list-two-pointer/)



## Queue and Stack

### Problems

1. [622 - Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)
2. [Moving Average from Data Stream](https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1368/)
   - deque 双向队列-双向链表
3. [286 - Walls and Gates](https://leetcode.com/problems/walls-and-gates/)
4. [200 - Number of Islands](https://leetcode.com/problems/number-of-islands/)
5. [752 - Open the Lock](https://leetcode.com/problems/open-the-lock/)
6. [Perfect Squares](https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/)
   - BFS-shortest path, set() for visited node avoid repeated computing
7. 