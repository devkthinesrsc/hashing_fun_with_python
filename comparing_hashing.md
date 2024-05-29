# Comparing Hash Functions:

1. To compare hash functions, you can measure their collision rates and distribution of hash values for various input data sets.
2. You can also compare their performance in terms of runtime and memory usage.
3. Common hash functions to compare with DJB include FNV, MurmurHash, and JenkinsHash.

# Comparing Collision Resolution Methods:

1. To compare collision resolution methods like chaining and probing, you can measure their performance under different load factors and table sizes.
2. You can compare their average lookup, insertion, and deletion times.
3. Additionally, you can analyze their behavior in terms of memory usage and clustering effects.

## example of comparing different hash functions using Python's timeit module:

```
import timeit

# Define different hash functions
def djb_hash(key):
    hash_value = 5381
    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
    return hash_value

def fnv_hash(key):
    # Implementation of FNV hash function
    pass  # Placeholder for FNV hash function

# Define a function to compare hash functions
def compare_hash_functions(data, hash_functions):
    for hash_function in hash_functions:
        start_time = timeit.default_timer()
        for key in data:
            hash_function(key)
        end_time = timeit.default_timer()
        print(f"Hash function {hash_function.__name__} took {end_time - start_time} seconds")

# Create sample data
data = ["apple", "banana", "orange"] * 100000

# Compare hash functions
hash_functions = [djb_hash, fnv_hash]
compare_hash_functions(data, hash_functions)
```