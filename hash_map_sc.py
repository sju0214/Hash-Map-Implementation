# Name: Seongyeong Ju
# OSU Email: jus@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6
# Due Date: 12/07/2023
# Description: Hash Map Implementation using Seperate Chaining 


from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number and the find the closest prime number
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        Updates key/value pair in hash map

        If key exists, the new value overwrites old value
        If key does not exist, new key/value pair is added 
        """
        # resize if table load factor is greater than or equal to 1
        if self.table_load() >= 1:
            new_capacity = self.get_capacity() * 2
            self.resize_table(new_capacity)
        
        # find hash key 
        hash_key = self._hash_function(key) % self._capacity 
        bucket = self._buckets[hash_key]

        # iterate and check if key exists, if so, overwrite value
        for node in bucket:
            if node.key == key:
                node.value = value
                return
        # insert key/value pair and increase size 
        bucket.insert(key, value)
        self._size += 1
        
    def resize_table(self, new_capacity: int) -> None:
        """
        Resizes capacity of hash table by rehashing hash table links
        Existing key/value pairs remain in new hash map
        
        New_capacity must be 1 or more and is prime
        """
        # if new_capacity is less than 1, do nothing 
        if new_capacity < 1:
            return

        if not self._is_prime(new_capacity):
            new_capacity = self._next_prime(new_capacity)

        new_table = HashMap(new_capacity, self._hash_function)
        for index in range(self._capacity):
            bucket = self._buckets.get_at_index(index)
            for node in bucket:
                new_table.put(node.key, node.value)

        self._buckets = new_table._buckets
        self._size = new_table._size
        self._capacity = new_table._capacity

    def table_load(self) -> float:
        """
        Returns current table load factor which is 
        Total number of elements stored in the table / number of buckets
        """
        load_factor = float(self.get_size() / self.get_capacity())
        return load_factor 

    def empty_buckets(self) -> int:
        """
        Returns number of empty buckets in hash table
        """
        num_of_empty = 0
        for index in range(self._capacity):
            bucket = self._buckets.get_at_index(index)
            if bucket.length() == 0:
                num_of_empty += 1
        return num_of_empty 

    def get(self, key: str):
        """
        Returns value associated with given key
        Returns None if key is not in hash map
        """
        # find bucket with key 
        find_hash_key = self._hash_function(key) % self._capacity
        bucket = self._buckets[find_hash_key]

        for node in bucket:
            if node.key == key:
                return node.value
        return None

    def contains_key(self, key: str) -> bool:
        """
        Returns bool value of True if key is in hash map
        Returns False if otherwise or empty hash map
        """
        # find bucket with key 
        find_hash_key = self._hash_function(key) % self._capacity
        bucket = self._buckets.get_at_index(find_hash_key)

        for node in bucket:
            if node.key == key:
                return True
        return False

    def remove(self, key: str) -> None:
        """
        Removes given key and associated value 
        Does nothing if key does not exist
        """
        # find bucket with key 
        # find_hash_key ONLY to find bucket nothing else 
        find_hash_key = self._hash_function(key) % self._capacity
        bucket = self._buckets.get_at_index(find_hash_key)

        # if key is in hash map, remove key and value
        node = bucket.contains(key)
        if node:
            bucket.remove(key)
            self._size -= 1
            return None


    def get_keys_and_values(self) -> DynamicArray:
        """
        Returns dynamic array with each index containing a tuple of 
        key/value pair in hash map 
        """
        # initialize dynamic array
        results_array = DynamicArray()
        # iterate through the buckets 
        for i in range(self._capacity):
            # iterate through indexes/nodes in each bucket
            for node in self._buckets[i]:
                results_array.append((node.key, node.value))
        return results_array


    def clear(self) -> None:
        """
        Clears contents of hash map without changing existing capacity
        """
        for i in range(self._capacity):
            self._buckets[i] = LinkedList()
        self._size = 0


def find_mode(da: DynamicArray) -> tuple[DynamicArray, int]:
    """
    Returns a tuple of a dynamic array of the most occuring value(s) 
    and int of the highest frequency mode value(s)
    """
    # if you'd like to use a hash map,
    # use this instance of your Separate Chaining HashMap
    map = HashMap()

    mode_arr = DynamicArray()
    # populate hash map with values in da 
    # key is the word string, value is the frequency of that word 
    for index in range(da.length()):
        if map.contains_key(da[index]):
            frequency = map.get(da[index])
            frequency += 1
            map.put(da[index], frequency)
        else:
            map.put(da[index], 1)
    
    # find the max count 
    tuple_arr = map.get_keys_and_values()
    max_count = 0 
    for index in range(tuple_arr.length()):
        element = tuple_arr[index]
        frequency = element[1]
        if frequency > max_count:
            max_count = frequency 
        
    # find element with the max count 
    for index in range(tuple_arr.length()):
        element = tuple_arr[index]
        frequency = element[1]
        mode_word = element[0]
        if frequency == max_count: # double = for compare
            mode_arr.append(mode_word)
    
    # return tuple[mode_arr, max_count]
    return mode_arr, max_count

        

# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(41, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(101, hash_function_1)
    print(round(m.table_load(), 2))
    m.put('key1', 10)
    print(round(m.table_load(), 2))
    m.put('key2', 20)
    print(round(m.table_load(), 2))
    m.put('key1', 30)
    print(round(m.table_load(), 2))

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(101, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(31, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(151, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(53, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(53, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - get_keys_and_values example 1")
    print("------------------------")
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(2)
    print(m.get_keys_and_values())

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(101, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(53, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")

    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")

