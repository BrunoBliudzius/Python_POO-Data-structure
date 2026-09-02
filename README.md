# Python OOP & Data Structures

Implementation of fundamental data structures in Python using **Object-Oriented Programming (OOP)**.

This repository is part of my journey to deepen my knowledge of Python and Computer Science fundamentals. The main goal was to understand how common data structures work internally by implementing them from scratch instead of relying directly on Python's built-in implementations.

## About the Project

This project was developed as a practical exercise in **Object-Oriented Programming, Data Structures, Algorithms, and problem-solving**.

Each data structure has its own implementation using classes, objects, methods, object references, recursion, iteration, and Python special methods such as `__len__`, `__contains__`, `__iter__`, `__str__`, and `__bool__`.

The main concepts practiced throughout the project include:

* Object-oriented design
* Encapsulation
* Object references
* Recursion
* Iteration
* Searching and insertion
* Node-based data structures
* Linear and non-linear data structures
* Hash tables
* Trees
* Graphs
* Breadth-First Search (BFS)
* Heap operations and heapify
* Python special methods
* Composition between data structures

## Implemented Data Structures

| Data Structure     | Implementation   | Main Concepts                               |
| ------------------ | ---------------- | ------------------------------------------- |
| Linked List        | `linked_list.py` | Nodes, references, insertion and removal    |
| Stack              | `stack.py`       | LIFO, `push`, `pop`, `peek`                 |
| Queue              | `queue.py`       | FIFO, `enqueue`, `dequeue`, `peek`          |
| Set                | `set.py`         | Union, intersection and difference          |
| Hash Table         | `hash_table.py`  | Hashing, collision handling and resizing    |
| Max Heap           | `max_heap.py`    | Max heap, heapify, insertion and extraction |
| Binary Search Tree | `tree.py`        | BST, searching, insertion and traversal     |
| Graph              | `graph.py`       | Adjacency list and BFS                      |

## Implementation Highlights

### Linked List

The linked list uses `Node` objects to represent individual elements and maintains references to the `head` and `tail`, as well as the current size of the structure.

Python special methods are also used to provide natural interactions with the data structure:

```python
len(linked_list)
```

and:

```python
value in linked_list
```

The implementation also provides `__iter__`, allowing the structure to be traversed directly using a `for` loop.

### Stack

Implementation of a **LIFO (Last In, First Out)** data structure.

The stack provides operations such as:

* `push`
* `pop`
* `peek`
* `clear`

### Queue

Implementation of a **FIFO (First In, First Out)** data structure.

The queue provides operations such as:

* `enqueue`
* `dequeue`
* `peek`
* Access to the last element

### Set

A custom set implementation supporting operations such as:

* Add
* Remove
* Union
* Intersection
* Difference

Python operator overloading is also used to make set operations more intuitive:

```python
set_a | set_b
set_a & set_b
set_a - set_b
```

### Hash Table

The hash table uses Python's `hash()` function and handles collisions through **chaining**, using linked lists to store multiple elements within the same bucket.

The implementation also includes a **resize mechanism** based on the load factor, allowing the table to increase its capacity when necessary.

### Max Heap

Implementation of a **Max Heap** using a list as the underlying storage structure.

The implementation includes:

* `insert`
* `extract`
* `peek`
* `clear`
* `_heapify_up`
* `_heapify_down`

The heap property is restored after insertions and extractions through heapify operations.

### Binary Search Tree

The Binary Search Tree uses nodes containing references to left and right child nodes.

The implementation includes:

* Insertion
* Searching
* In-order traversal
* Element counting
* Iteration

The in-order traversal allows the elements to be retrieved in ascending order while maintaining the BST property.

### Graph

The graph uses an **adjacency list** to represent connections between vertices.

The implementation supports:

* Directed graphs
* Undirected graphs
* Vertex insertion
* Edge insertion
* Breadth-First Search (BFS)

The BFS implementation uses the custom `Queue` and `Set` structures developed in this project, demonstrating how different data structures can work together to implement an algorithm.

## Object-Oriented Programming Concepts

This project was designed to practice OOP through real implementations rather than isolated examples.

The main concepts include:

* Classes and objects
* Constructors
* Instance attributes
* Public and internal methods
* Object composition
* Encapsulation
* Special methods / dunder methods
* Iterators
* Generators
* Recursion

One example of composition can be found in the `Graph` implementation, which uses the custom `Queue` and `Set` structures when performing BFS.

## Technologies

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

**Language:** Python

**Concepts:** Object-Oriented Programming, Data Structures, Algorithms, Recursion, Iteration

**Version Control:** Git / GitHub

## Getting Started

Clone the repository:

```bash
git clone https://github.com/BrunoBliudzius/Python_POO-Data-structure.git
```

Navigate to the project directory:

```bash
cd Python_POO-Data-structure
```

Each implementation can be executed individually:

```bash
python linked_list.py
python stack.py
python queue.py
python set.py
python hash_table.py
python max_heap.py
python tree.py
python graph.py
```

No external dependencies are required to run the implementations.

## Learning Goals

The main purpose of this project was to go beyond simply using data structures and understand how they work internally.

The learning process can be summarized as:

**How data is stored → How operations are performed → What those operations cost → How different structures can be combined to solve problems.**

Understanding these fundamentals provides a strong foundation for further studies in algorithms, software engineering, backend development, and system design.

## Future Improvements

Possible improvements and extensions to the project include:

* [ ] Add Big O complexity analysis
* [ ] Add automated tests using `pytest`
* [ ] Improve type hints using `typing`
* [ ] Add dedicated documentation for each data structure
* [ ] Implement additional searching and sorting algorithms
* [ ] Implement Depth-First Search (DFS)
* [ ] Implement balanced trees
* [ ] Add edge-case testing
* [ ] Improve project organization into modules and packages

## License

This project is available under the MIT License.

---

**A study project focused on Python, Object-Oriented Programming, Data Structures, Algorithms, and Computer Science fundamentals.**
