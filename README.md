# DS-II-Final-Project
Ropes data structure is a type of data structure used for efficiently manipulating large strings of text or data. It was first introduced in 1987 by Hans-Juergen Boehm and Russell Atkinson. 

A rope is essentially a binary tree that represents a large string of text, where each node in the tree represents a smaller substring or segment of the overall string.

Ropes are particularly useful when working with very long strings or text documents, as they allow for efficient insertion, deletion, and concatenation operations without the need for costly memory reallocation. In this way, ropes provide a useful alternative to more traditional string data structures such as arrays or linked lists.

In this introduction, we will explore the basic principles and properties of ropes data structure, and provide examples of how they can be used in practice.


In this project we have implemented the following functions:

init(rope): Initializes a new Rope object with a string s

merge(left, right): Concatenates two Rope instances left and right into a new Rope instance.

Search(indexing): returns the character at ith position, we search recursively beginning at the root node.

Split(self, i): Splits the Rope at the specified index i.

Insert(rope, x): takes a Rope instance rope, a string s, and an index i, and inserts the string s into the Rope at the specified index i.

Delete(rope): This delete function takes a Rope instance rope, a start index start, and an end index end, and removes the characters from the Rope between the start and end indices. 

Replace: replaces a given string with text in the rope
