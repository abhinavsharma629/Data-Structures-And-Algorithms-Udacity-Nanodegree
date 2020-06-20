class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.max_cap=capacity
        self.cache_dict={}
        self.LRU_CacheMaintainance={}


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if(key in self.cache_dict):
        	'''updating cache memory for Least Recently Used Cache
        	As adding entry to dict is based on order'''

        	del self.LRU_CacheMaintainance[key]
        	self.LRU_CacheMaintainance[key]=1

        	return self.cache_dict[key]
        else:
        	return -1

    def removeLRU(self):
    	key=None
    	for i,j in self.LRU_CacheMaintainance.items():
    		key=i
    		break
    	del self.LRU_CacheMaintainance[key]
    	del self.cache_dict[key]

    def set(self, key, value):
        if(self.max_cap<=0):
            return -1
        if(key in self.cache_dict):
        	self.cache_dict[key]=value
        	del self.LRU_CacheMaintainance[key]
        	self.LRU_CacheMaintainance[key]=1

        else:
        	if(len(self.cache_dict)==self.max_cap):
        		self.removeLRU()
        	self.LRU_CacheMaintainance[key]=1
        	self.cache_dict[key]=value



our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry






our_cache = LRU_Cache(1)

print(our_cache.get(1))       # returns -1
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns -1
print(our_cache.get(2))       # returns -1
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
print(our_cache.get(4))      # returns 4

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(6))      # returns 6



our_cache = LRU_Cache(0)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns -1
print(our_cache.get(2))       # returns -1
print(our_cache.get(3))       # returns -1
print(our_cache.get(4))       # returns -1
