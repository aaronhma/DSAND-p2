# Explanation

## Exercise 1: LRU Cache

To solve this exercise, I decided to use a hash map. The reason I used it was because of the `set()` function took 2 values, which was a major hint, but also because getting/retrieving/putting values is all O(1) time complexity.

- Time complexity: O(n)
- Space complexity: O(n)

## Exercise 2: File Recursion

The idea behing this exercise is recursion. We visit each folder, and in each folder, we keep the files that matches the wanted pattern, then continue deeper into the folder.

- Time complexity: O(d \* w) - d: depth, w: width
- Space complexity: O(f) - f: files found

## Exercise 3: Huffman Coding

I implemented this problem with the following procedures:

- calculate occurences of each character in the string
- the character with the highest occurance is encoded with the minimum code length
- next character, etc.

* Time complexity: O(n) - recursion
* Space complexity: O(k) - k: size of alphabet

## Exercise 4: Active Directory

Recursion was used to solve this problem, but with 2 base cases to avoid the RecursionDepthOverflow error in Python.

- Time complexity: O(g \* u) - g: groups, u: users
- Space complexity: O(1) - depends on output

## Exercise 5: Blockchain

The blockchain problem was fairly simple. This problem was solved by a _backwards_ linked list, with the help of the `hashlib` python library for using the sha256() function.

- add: O(1)
- searching: O(n)
- size: O(1)
- get_info: O(1)

- Space: O(n)

## Exercise 6: Union and Intersection

To solve this problem, I added a helper function in the definition of the Linked List called `wrapper`, that returns the linked list as a Python list, then converted it into a set, then used the set built-in union and intersection to solve this problem.

- Time complexity: O(1)
- Space complexity: O(s1 + s2) - s1: size of 1st linked list, s2: size of 2nd linked list
