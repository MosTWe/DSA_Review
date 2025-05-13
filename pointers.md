Pointers, and how they apply differently to different data types


integers

id(var) calls the address of a variable

x = 11
y = x

id(x) == id(y) #true

you can change the address x refers to but you can't change the value at the address. They are immutable


dictionaries

dict1 = {"a":1}
dict2 = dict1

id(dict1)==dict(2) #true

dict2["a"] = 2
dict1 == {'a':'2'}
dict2 == {'a':'2'}

id(dict1)==dict(2) #true

dictionaries stay pointing to the same place but you can update values. They are mutable

If you define
dict3 = {'hello':'world'}
dict2 = dict3
dict1 = dict2
athen id(dict1)==id(dict2)==id(dict3)=={'hello':'world'}.

Nothing points to {'a':2}, so it is cleaned up by garbage collection.