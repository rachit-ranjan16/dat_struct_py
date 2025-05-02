# dat-struct-py

Basic Data Structures and Operations Implemented in Python

## Installation Instructions

- Python 3.5+ is currently supported
- Install from PyPI using
  - pip install dat-struct-py

## Supported Data Structures

- Singly Linked List
- Doubly Linked List
- Circularly Singly Linked List  
- Stack using Linked List
- Queue using Linked List
- Binary Search Tree
- Trie
- Heap (MinHeap and MaxHeap)

### Operations Supported for Linked Lists

- Create a linked list through input sequence or inserts
  - At the beginning
  - At the end
  - At any Position
- Delete a node carrying some value
- Size
- Print
- Quick check whether the list has even length
- Return nth element from the end
- Quick check whether a cycle exists
- Return cycle length(if one exists)
- Reverse in Place
- Swap Pairs - Works only for Even length linked list

### Operations Supported for Stacks

- Create a stack by pushing elements one by one or through an input sequence
- Check whether the stack is empty
- Check whether the stack is full
- Push an element
- Pop an element
- Peek the top element
- Check balanced symbols
- Filter out all adjacent elements from the input
- Print the elements of the Stack

### Operations Supported for Queues

- Create a queue by queuing elements one by one or through an input sequence
- Check whether the Queue is empty
- Enqueue an element
- Dequeue an element
- Print the elements of the Queue

### Operations Supported for Binary Search Trees

- Create a binary search tree by
  - Inserting values one by one
  - Passing in an input list
- Traversals
  - Preorder
  - Inorder
  - Postorder
  - Spiral
    - Clockwise
    - Anticlockwise
  - Boundary
- Projections/Views
  - LHS
  - RHS
- Nodes at K distance away from root
- Connect Nodes at the Same Level
  - Singly Linked List
  - Circularly Singly Linked List

### Operations Supported for Tries

- Create a trie by inserting strings
- Insert a string into the trie
- Look up a string to check if it exists in the trie
- Prefix-based string operations

### Operations Supported for Heaps

- Create a heap (MinHeap or MaxHeap)
  - From an array of elements
  - By inserting elements one by one
- Insert an element
- Extract the top element (min for MinHeap, max for MaxHeap)
- Get the top element without removing it
- Check if the heap is empty
- Get the size of the heap
- Heapify an array

## Developer Tools

- Full Fledged Vagrant Box in tools/DevelopDatStructPy
  - Prerequisites
    - [VirtualBox Installation](https://www.virtualbox.org/wiki/Downloads)
    - [Vagrant Installation](https://www.vagrantup.com/downloads.html)
- Navigate to tools/DevelopDatStructPy
- Modify bootstrap.sh to contain your git username and email (**MANDATORY STEP**)
- Open Terminal/Command prompt
- Execute `vagrant up` to bring up the VM
- Execute `vagrant ssh` to login to the VM
- Master Code will be present at `home/ubuntu/Development/Repos/`
- Execute `source /home/ubuntu/Development/developEnv/bin/activate` to activate Python Virtual Environment

## Project Structure

- `dat_struct_py/`: Core implementation directory containing Python modules for data structures
- `dat_struct_py/blocks/`: Contains the fundamental node structures used by data structures
- `dat_struct_py/tests/`: Contains unit tests for each data structure implementation
