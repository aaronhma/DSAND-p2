# Explanation

## Exercise 1: LRU Cache

To solve this exercise, I decided to use a hash map. The reason I used it was because of the `set()` function took 2 values, which was a major hint, but also because getting/retrieving/putting values is all O(1) time complexity.

## Exercise 2: File Recursion

The idea behing this exercise is recursion. We visit each folder, and in each folder, we keep the files that matches the wanted pattern, then continue deeper into the folder.

## Exercise 3: Huffman Coding

I implemented this problem with the following procedures:

- calculate occurences of each character in the string
- the character with the highest occurance is encoded with the minimum code length
- next character, etc.

* Time complexity: O(n) - recursion

## Exercise 4: Active Directory

Recursion was used to solve this problem, but with 2 base cases to avoid the RecursionDepthOverflow error in Python.

## Exercise 5: Blockchain

The blockchain problem was fairly simple. This problem was solved by a _backwards_ linked list, with the help of the `hashlib` python library for using the sha256() function.

## Exercise 6: Union and Intersection

To solve this problem, I added a helper function in the definition of the Linked List called `wrapper`, that returns the linked list as a Python list, then converted it into a set, then used the set built-in union and intersection to solve this problem.
