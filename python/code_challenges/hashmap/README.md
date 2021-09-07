# Hash Table:
Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.


## Auther :
Anas Abu Ghalieha


## Challenge

add

Arguments: key, value
Returns: nothing
This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

get

Arguments: key
Returns: Value associated with that key in the table

contains
Arguments: key
Returns: Boolean, indicating if the key exists in the table already.
hash
Arguments: key
Returns: Index in the collection for that key


## Approach & Efficiency

Big O Notation

Time: O(1)

Space: O(N)


# API


+ Create a hashtable with the following methods:
1- add which takes in both the key and value. Hash the key, and add the key and value pair to the table, handling collisions as needed.
2- get that takes in the key and returns the value from the table.
+ contains that takes in the key and returns a boolean, indicating if the key exists in the table already.
hash that takes in an arbitrary key and returns an index in the collection.
+ Find that takes Key and Search in the hashtable and returns the value.
+ contains check if the there is a value for the key in the Hashtable
+ Add 