##gives us the ability to calculate our own hashes from string data types
import hashlib

print(hashlib.md5(b"hello").hexdigest())

##Hashlib is the library that we are calling the md5 function from hashlib.md5(). We are passing the string "hello" to this function (hashlib.md5(b"hello")).
##The 'b' before the "hello" string is encoding the unicode-object "hello" to a binary format before hashing it (a condition required by this hashing function).
##The hexdigest method is returning the encoded data in hexadecimal format, which allows us to see the output hash.
