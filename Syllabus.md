## Methodoly

2. 学习数据数据结构topic
3. 按特定topic刷题(DFS, BFS, HashMap)  5 + 10 + 15
3. 总结题目背后算法知识
4. 整理模板代码块



## Statistics

| Topic                | Easy | Medium | Hard | Unknown | Sum  |
| -------------------- | ---- | ------ | :--- | ------- | ---- |
| **Array and String** | 20   | 6      | 0    | 7       | 33   |
| **Queue and Stack**  | 7    | 11     | 0    | 1       | 19   |
| **Hash Table**       | 15   | 6      | 0    | 3       | 24   |
| **Total**            | 42   | 23     | 0    | 11      | 76   |

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

1.  [Find Pivot Index](https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/) ([1991- Find the Middle Index in Array](https://leetcode.com/problems/find-the-middle-index-in-array/) ) - Easy
    - left = right( sum - left - current)
2.  [Largest Number At Least Twice of Others](https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/) - Unknown
3.  [Plus One](https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/) - Easy
4.  *[Diagonal Traverse](https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/) - Medium
    - the sum of indices on all diagonals are equal
    - direction: %2
5.  [54 - Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) - Medium
6.  [Pascal's Triangle](https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1170/) - Easy
7.  [Add Binary](https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1160/) - Easy
8.  [Implement strStr()](https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/) - Unknown
9.  [Longest Common Prefix](https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/) - Easy
10.  [Reverse String](https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1183/) - Easy
11.  [Array Partition I](https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1154/) - Unknown
12. [167-Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) - Easy
    - two-pointer
13. [Remove Element](https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1151/) - Easy
14. [Max Consecutive Ones](https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1301/) (Sliding window problem) - Easy
15. [209 - Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) (Sliding window problem) - Medium
16.  [Rotate Array](https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1182/) - Medium
17.  [Pascal's Triangle II](https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1171/) - Easy
18.  [Reverse Words in a String](https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1164/) - Medium
19.  [Reverse Words in a String III](https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1165/) - Easy
20.  [Remove Duplicates from Sorted Array](https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1173/) - Easy
21.  [Move Zeroes](https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1174/) - Easy

**Arrays 101**

1. [Find Numbers with Even Number of Digits](https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/) - Unknown
2. [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) - Easy
3. [Duplicate Zeros](https://leetcode.com/problems/duplicate-zeros/) - Easy
4. [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) - Easy
5. [Check If N and Its Double Exist](https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/) - Unknown
6. [Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/) - Easy
7. [Replace Elements with Greatest Element on Right Side](https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/) - Unknown
8. [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) - Easy
9. [Height Checker](https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/) - Unknown
10. [Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/) - Medium
11. [Third Maximum Number](https://leetcode.com/problems/third-maximum-number/) - Easy
12. [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) - Easy

### Conclusion

1. **Two-pointer Technique**
   - one starts from the first element and another starts from the last element
     - 10, 11, 12
   - one is still used for the iteration while the second one always points at the position for next addition
     - 13, 14, 15
   - [Slow-pointer and fast-pointer problem in Linked List](https://leetcode.com/explore/learn/card/linked-list/214/linked-list-two-pointer/)



## Queue and Stack

### Problems

1. [622 - Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) - Medium
2. [Moving Average from Data Stream](https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1368/) - Easy
   - deque 双向队列-双向链表
3. [286 - Walls and Gates](https://leetcode.com/problems/walls-and-gates/) - Medium
4. [200 - Number of Islands](https://leetcode.com/problems/number-of-islands/) - Medium
5. [752 - Open the Lock](https://leetcode.com/problems/open-the-lock/) - Medium
6. *[Perfect Squares](https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/) \- Medium
   - BFS-shortest path, set() for visited node avoid repeated computing
7. [Min Stack](https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1360/) - Easy
8. [Valid Parentheses](https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1361/) - Easy
9. [Daily Temperatures](https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1363/) - Unknown
10. [Evaluate Reverse Polish Notation](https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1394/) \- Medium
11. [Clone Graph](https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1392/) \- Medium
12. *[494 - Target Sum](https://leetcode.com/problems/target-sum/) \- Medium
13. [Binary Tree Inorder Traversal](https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1383/) - Easy
14. [Implement Queue using Stacks](https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1386/) - Easy
15. [Implement Stack using Queues](https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1387/) - Easy
16. [Decode String](https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1379/) \- Medium
17. [Flood Fill](https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1393/) - Easy
18. [01 Matrix](https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1388/) \- Medium
19. [Keys and Rooms](https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1391/) \- Medium



### Conclusion

1. Queue & Stack
2. Circular Queue: a fixed-size array
3. Queue and BFS
   - BFS Template I: shortest path
     - out while loop and inner for loop (length of stack)
   - BFS Template II: never visited a node twice
     - visited
4. Stack and DFS
   - DFS Template I: recursion
   - DFS Template II: explicit stack
     - visited 



## Hash Table

### Introduction

Hash table is a data structure using **hash funcitons** in order to support quick **insertion** and **search**.

- hash set: set - no repeated values
- hash map: map - (key, value) pair

### Problems

1. [Design HashSet](https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1139/) - Easy
2. [Design HashMap](https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1140/) - Easy
3. [Contains Duplicate](https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1112/) - Easy
4. [Single Number](https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1176/) - Easy
5. [Intersection of Two Arrays](https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1105/) - Easy
6. [Happy Number](https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1131/) - Easy
7. [Two Sum](https://leetcode.com/problems/two-sum/) - Easy
8. [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) - Easy
9. [Minimum Index Sum of Two Lists](https://leetcode.com/problems/minimum-index-sum-of-two-lists/) - Easy
10. [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) - Easy
11. [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) - Easy
12. [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) - Easy
13. [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) - Easy
14. [Group Anagrams](https://leetcode.com/problems/group-anagrams/) - Medium
15. *[Group Shifted Strings](https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1125/) - Unknown
16. [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) - Medium
17. [Find Duplicate Subtrees](https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1127/) - Unknown
18. [Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/) - Easy
19. [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) - Medium
20. [Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/) - Easy
21. [4Sum II](https://leetcode.com/problems/4sum-ii/) - Medium
22. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) - Medium
23. [Unique Word Abbreviation](https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1137/) - Unknown
24. [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) - Medium

### Conclusion

How to design the key?

1. When the order of each element in the string/array doesn't matter, you can use the **sorted string/array** as the key.
2. If you only care about the offset of each value, usually the offset from the first value, you can use the **offset** as the key.
3. In a tree, you might want to directly use the **TreeNode** as key sometimes. But in most cases, **the serialization of the subtree** might be a better idea.
4. In a matrix, you might want to use the **row index** or the **column index** as key.
5. In a Sudouku, you can combine the row index and the column index to identify which **block** the element belongs to.
6. Sometimes, in a matrix, you might want to aggregate the values in the same **diagonal line**.

## Binary Search

### problems

1. [Binary Search](https://leetcode.com/problems/binary-search/) - Easy
2. [Sqrt(x)](https://leetcode.com/problems/sqrtx/) - Easy
3. [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/) - Easy
4. *[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) - Medium
5. [First Bad Version](https://leetcode.com/problems/first-bad-version/) - Easy
6. [Find Peak Element](https://leetcode.com/problems/find-peak-element/) - Medium
7. [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) - Medium
8. [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) - Medium
9. [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) - Medium
10. [Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/) - Easy
11. [Search in a Sorted Array of Unknown Size](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/) - Medium
12. [Pow(x, n)](https://leetcode.com/problems/powx-n/) - Medium
13. [Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/) - Easy
14. [Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/) - Easy
15. *[Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) - Hard
16. *[Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) - Medium



## Recursion

### Problems

1. [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) - Medium
2. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) - Easy
3. [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) - Easy
4. [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) - Easy
5. [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) - Easy
6. [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) - Easy
7. [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) - Easy
8. [K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/) - Medium
9. [Sort an Array](https://leetcode.com/problems/sort-an-array/) - Medium
10. [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) - Medium
11. [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/solution/) - Medium
12. *[N-Queens II](https://leetcode.com/problems/n-queens-ii/) - Hard
13. [Combinations](https://leetcode.com/problems/combinations/) - Medium
14. [Same Tree](https://leetcode.com/problems/same-tree/) - Easy
15. [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) - Medium
16. [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) - Medium
17. [Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/) - Medium
18. *[Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) - Hard
19. *[Permutations](https://leetcode.com/problems/permutations/) - Medium
20. [Letter Combinations of a Phone Number](https://leetcode.com/explore/learn/card/recursion-ii/507/beyond-recursion/2905/) - Medium



## Linked List

### Problems

1. [Design Linked List](https://leetcode.com/problems/design-linked-list/) - Medium
2. [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) - Easy
3. [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) - Medium
4. [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) - Easy
5. [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) - Medium
6. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) - Easy
7. [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) - Easy
8. [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) - Medium
9. [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) - Easy
10. [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) - Medium
11. [Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) - Medium
12. [Insert into a Cyclic Sorted List](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/solution/) - Medium
13. [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) - Medium
14. [Rotate List](https://leetcode.com/problems/rotate-list/solution/) - Medium

