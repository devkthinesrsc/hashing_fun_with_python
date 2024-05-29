class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    # Takes a key and calculates its hash value using DJB hash function
        # Iterates over each character in the key, updates the `hash_value` using a simple formula, and finally takes modulo 'self.size' to ensure the hash value is within the range of hash table's size.
        # It attempts to evenly distribute the hash values across the hash table.
    def hash_function(self, key):
        hash_value = 5381
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return hash_value % self.size
    
    
    # insert method insets a key-value pair into the hash table
        # It calculates the hash value of the key using the hash_function method.
        # It then iterates over each pair in the bucket at the calculated index.
        # If the key is already present in the bucket, it updates the value and returns.
        # If the key is not present in the bucket, it appends the key-value pair to the bucket.
    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
    
    # lookup method searches for a key in the hash table and returns its value
        # It calculates the hash value of the key using the hash_function method.
        # It then iterates over each pair in the bucket at the calculated index.
        # If the key is found in the bucket, it returns the corresponding value.
        # If the key is not found in the bucket, it raises a KeyError.
    def lookup(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError("Key not found")
    
    # delete method removes a key-value pair from the hash table
        # It calculates the hash value of the key using the hash_function method.
        # It then iterates over each pair in the bucket at the calculated index.    
        # If the key is found in the bucket, it deletes the key-value pair and returns.
        # If the key is not found in the bucket, it raises a KeyError.
    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        raise KeyError("Key not found")
    
    # len method returns the total number of key-value pairs in the hash table
    def __len__(self):
        return sum(len(bucket) for bucket in self.table)
    
    # resize method resizes the hash table to a new size
        # It creates a new table of size 'new_size' and initializes it with empty buckets.
        # It then iterates over each bucket in the current table and rehashes the key-value pairs into the new table using the updated hash function.
        # Finally, it updates the size and table attributes of the hash table.
        # this operation is useful when the load factor of the hash table exceeds a certain threshold, and resizing helps in maintaining a low collision rate.
    def resize(self, new_size):
        new_table = [[] for _ in range(new_size)]
        for bucket in self.table:
            for key, value in bucket:
                index = self.hash_function(key, new_size)
                new_table[index].append([key, value])
        self.size = new_size
        self.table = new_table
    
    # items method returns an iterator over all key-value pairs in the hash table
        # It iterates over each bucket in the table and then iterates over each pair in the bucket, yielding the key-value pair.
    def items(self):
        for bucket in self.table:
            for pair in bucket:
                yield pair


# Example usage:
hash_table = HashTable()

# Inserting key-value pairs
hash_table.insert("apple", 5)
hash_table.insert("banana", 10)
hash_table.insert("orange", 15)

# Looking up a value
print(hash_table.lookup("banana"))  # Output: 10

# Deleting a key
hash_table.delete("banana")

# Length of the hash table
print(len(hash_table))  # Output: 2

# Iterating through items
for key, value in hash_table.items():
    print(key, value)




# function takes a file path as input and returns a hash table containing the word frequencies
# It reads the file line by line, splits each line into words, and updates the word frequencies in the hash table.
# It uses a simple hash table to store the word frequencies, where the keys are the words and the values are the corresponding frequencies.
# It strips leading and trailing whitespaces from each word and converts it to lowercase to ensure consistent counting.
# It returns the hash table containing the word frequencies.
# This function can be useful for analyzing text data and counting word frequencies in a document.
def count_word_frequencies(file_path):
    hash_table = HashTable()
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip().lower()
                if word:
                    if word in hash_table:
                        hash_table[word] += 1
                    else:
                        hash_table[word] = 1
    return hash_table

word_frequencies = count_word_frequencies("book.txt")

# Printing word frequencies
for word, frequency in word_frequencies.items():
    print(f"{word}: {frequency}")
