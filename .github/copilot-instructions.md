# Copilot Instructions for dat_struct_py Repository

This document provides context about the `dat_struct_py` repository to help Copilot understand the project structure and purpose.

## Project Overview

`dat_struct_py` is a Python library containing implementations of common data structures. The goal is to provide clear, well-documented, and tested implementations.

## Core Implementation (`dat_struct_py/`)

This directory contains the main Python modules for the data structures:

*   **`linkedlist.py`**: Implements `sLinkedList` (Singly), `dLinkedList` (Doubly), and `cLinkedList` (Circular Singly). Includes operations for insertion, deletion, traversal, size, cycle detection, reversing, etc.
*   **`queue.py`**: Implements `lQueue` (Linked List based Queue) with standard operations (enqueue, dequeue, isEmpty, size).
*   **`stack.py`**: Implements `lStack` (Linked List based Stack) with standard operations (push, pop, peek, isEmpty, isFull) and extras like balanced parentheses checking.
*   **`tree.py`**: Implements `BinarySearchTree` with insertion, various traversals (preorder, inorder, postorder, spiral, boundary), views (LHS/RHS), k-distance nodes, and sibling connection.
*   **`trie.py`**: Implements a `Trie` for prefix-based string operations (insert, lookup).
*   **`heap.py`**: Implements a base `Heap` class along with derived `MinHeap` and `MaxHeap` classes. Supports operations like insertion, extraction, getting the top element, checking size/emptiness, and heapification.
*   **`blocks/node.py`**: Defines the fundamental node classes (`sNode`, `dNode`, `bNode`) used by the data structures above.

## Tests (`dat_struct_py/tests/`)

Contains unit tests for each data structure to ensure correctness. Test files generally correspond to the implementation files (e.g., `test_linked_lists.py` tests `linkedlist.py`).

## Other Key Files

*   **`setup.py`, `MANIFEST.in`**: Standard Python packaging files.
*   **`Makefile`**: Contains commands for development tasks (e.g., running tests).
*   **`tools/DevelopDatStructPy/`**: Contains Vagrant setup for a consistent development environment.

## Key Considerations for Copilot

*   The library is implemented in Python.
*   Focus on the classes and methods defined within the `dat_struct_py/` directory for core logic.
*   Refer to `dat_struct_py/tests/` for usage examples and expected behavior.
*   Node structures are defined in `dat_struct_py/blocks/node.py`.
