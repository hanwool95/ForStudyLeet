# Design a HashMap without using any built-in hash table libraries.
#
# Implement the MyHashMap class:
#
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

class MyHashMap:

    def __init__(self):
        self.hashMap = {}

    def put(self, key: int, value: int) -> None:
        self.hashMap[key] = value

    def get(self, key: int) -> int:
        if key in self.hashMap.keys():
            return self.hashMap.get(key)
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.hashMap.keys():
            self.hashMap.pop(key)

# Runtime: 218 ms, faster than 94.63% of Python3 online submissions for Design HashMap.
# Memory Usage: 17.1 MB, less than 96.99% of Python3 online submissions for Design HashMap.

