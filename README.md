# Optimized Hash Map Implementation with Chaining

### Overview

This repository contains an optimized HashMap implementation in Python. The implementation uses a dynamic array to store the hash table and employs chaining with singly linked lists for collision resolution. The goal is to achieve O(1) time complexity for average case performance across all operations.


### Implementation Details

The main implementation is provided in the file hash_map_sc.py. It includes a skeleton code that you need to complete by implementing the following methods:

- `put(key, value)`: Insert or update the value associated with the given key.
- `get(key)`: Retrieve the value associated with the given key.
- `remove(key)`: Remove the key and its associated value from the hash map.
- `contains_key(key)`: Check if the hash map contains the given key.
- `clear()`: Remove all key-value pairs from the hash map.
- `empty_buckets()`: Count and return the number of empty buckets in the hash map.
- `resize_table()`: Resize the hash table to accommodate more key-value pairs.
- `table_load()`: Calculate and return the current load factor of the hash map.
- `get_keys_and_values()`: Return a list of all keys and values in the hash map.
- `find_mode()`: Find and return the key with the maximum occurrences in the hash map.

1. Two pre-written classes are provided for you in the skeleton code - DynamicArray and LinkedList (in a6_include.py). The objects of these classes MUST be used in the HashMap class implementation. Use a DynamicArray object to store the hash table, and LinkedList objects to store chains of key/value pairs.
2. The provided Dynamic Array and Linked List classes may provide different functionality than those described in the lectures or implemented in prior homework assignments. Review the docstrings in the skeleton code to understand the available methods, their use, and input/output parameters.
3. The number of objects stored in the hash map will be between 0 and 1,000,000 inclusive.
4. Two pre-written hash functions are provided in the skeleton code. Make sure to test the code with both functions. 
5. RESTRICTIONS: ANY built-in Python data structures and/or their methods must NOT be used.
6. Directly accessing any variables of the DynamicArray or LinkedList classes or directly call their double underscore (“dunder”) methods are NOT allowed. All work must be done only by using class methods.
7. Variables in the SLNode class are not private. They are allowed to accessed and changed directly.
8. Any imports beyond the ones included in the source code provided must not be used.
