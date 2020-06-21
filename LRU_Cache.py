# LRU CACHE
class LRU_Cache(object):
    """
    Defines a LRU Cache object.
    """

    def __init__(self, capacity=5):
        # Initialize class variables
        self.data = {}
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        try:
            return self.data[key]
        except KeyError:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.capacity == len(self.data.keys()):
            total_keys = list(self.data.keys())
            first_key = total_keys[0]
            del self.data[first_key]
        else:
            if key in self.data:
                print("The key already exists in the LRU Cache!")
            else:
                self.data[key] = value
# LRU CACHE


# TESTS
# Udacity Tests
print("[RUNNING] Running Udacity tests...\n")
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

assert(our_cache.get(1) == 1)
assert(our_cache.get(2) == 2)
assert(our_cache.get(9) == -1)

our_cache.set(5, 5)
our_cache.set(6, 6)

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(3))

assert(our_cache.get(3) == 3)

print("\n[PASS] Finished running Udacity tests!")

# Student Tests
print("[RUNNING] Running student tests!\n")
cache = LRU_Cache(4)
cache.set(1, 2)
print(cache.get(1))
cache.set(3, 4)
cache.set(833, 34)
cache.set(34, 3)
cache.set(45, 3)
print(cache.get(5))  # returns -1
print(cache.get(3))  # retunrns 4
print(cache.get(833))  # returns 34
print(cache.get(34))  # returns 3
print(cache.get(45))  # returns 3
print(cache.get(1))  # returns -1
print("\n[PASS] Finished running student tests!")
# TESTS
