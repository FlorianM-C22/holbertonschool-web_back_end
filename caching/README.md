## Resources

**Read or watch**:

- [Cache replacement policies - FIFO](/rltoken/4Ub_zi_LxGAeIWZRvqXC8g "Cache replacement policies - FIFO")
- [Cache replacement policies - LIFO](/rltoken/rAbFN7cZl67p1ecos7i9DA "Cache replacement policies - LIFO")
- [Cache replacement policies - LRU](/rltoken/-wHrdtTxPWbMqMwp-rx4Ag "Cache replacement policies - LRU")
- [Cache replacement policies - MRU](/rltoken/HCX2zXK2-pP8xzadawVXNA "Cache replacement policies - MRU")
- [Cache replacement policies - LFU](/rltoken/FYockAUCVuM_F-xooethfw "Cache replacement policies - LFU")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/cHhMVpo-XBzdLtk8C42Rrg "explain to anyone"), **without the help of Google**:

### General

- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system
- What limits a caching system have

## Requirements

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.9)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks

### 1.

Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- This caching system doesn’t have limit
- `def put(self, key, item):`
  - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
  - If `key` or `item` is `None`, this method should not do anything.
- `def get(self, key):`
  - Must return the value in `self.cache_data` linked to `key`.
  - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
BasicCache = \_\_import\_\_('0-basic\_cache').BasicCache

my\_cache = BasicCache()
my\_cache.print\_cache()
my\_cache.put("A", "Hello")
my\_cache.put("B", "World")
my\_cache.put("C", "Holberton")
my\_cache.print\_cache()
print(my\_cache.get("A"))
print(my\_cache.get("B"))
print(my\_cache.get("C"))
print(my\_cache.get("D"))
my\_cache.print\_cache()
my\_cache.put("D", "School")
my\_cache.put("E", "Battery")
my\_cache.put("A", "Street")
my\_cache.print\_cache()
print(my\_cache.get("A"))

guillaume@ubuntu:~/$ ./0-main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
guillaume@ubuntu:~/$
```

### 2.

Create a class `FIFOCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
  - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
  - If `key` or `item` is `None`, this method should not do anything.
  - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
    - you must discard the first item put in cache (FIFO algorithm)
    - you must print `DISCARD:` with the `key` discarded and following by a new line
- `def get(self, key):`
  - Must return the value in `self.cache_data` linked to `key`.
  - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
FIFOCache = \_\_import\_\_('1-fifo\_cache').FIFOCache

my\_cache = FIFOCache()
my\_cache.put("A", "Hello")
my\_cache.put("B", "World")
my\_cache.put("C", "Holberton")
my\_cache.put("D", "School")
my\_cache.print\_cache()
my\_cache.put("E", "Battery")
my\_cache.print\_cache()
my\_cache.put("C", "Street")
my\_cache.print\_cache()
my\_cache.put("F", "Mission")
my\_cache.print\_cache()

guillaume@ubuntu:~/$ ./1-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
DISCARD: B
Current cache:
C: Street
D: School
E: Battery
F: Mission
guillaume@ubuntu:~/$
```

### 3.

Create a class `LIFOCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
  - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
  - If `key` or `item` is `None`, this method should not do anything.
  - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
    - you must discard the last item put in cache (LIFO algorithm)
    - you must print `DISCARD:` with the `key` discarded and following by a new line
- `def get(self, key):`
  - Must return the value in `self.cache_data` linked to `key`.
  - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
""" 2-main """
LIFOCache = \_\_import\_\_('2-lifo\_cache').LIFOCache

my\_cache = LIFOCache()
my\_cache.put("A", "Hello")
my\_cache.put("B", "World")
my\_cache.put("C", "Holberton")
my\_cache.put("D", "School")
my\_cache.print\_cache()
my\_cache.put("E", "Battery")
my\_cache.print\_cache()
my\_cache.put("C", "Street")
my\_cache.print\_cache()
my\_cache.put("F", "Mission")
my\_cache.print\_cache()
my\_cache.put("G", "San Francisco")
my\_cache.print\_cache()

guillaume@ubuntu:~/$ ./2-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: D
Current cache:
A: Hello
B: World
C: Holberton
E: Battery
Current cache:
A: Hello
B: World
C: Street
E: Battery
DISCARD: C
Current cache:
A: Hello
B: World
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
B: World
E: Battery
G: San Francisco
guillaume@ubuntu:~/$
```

### 4.

Create a class `LRUCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
  - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
  - If `key` or `item` is `None`, this method should not do anything.
  - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
    - you must discard the least recently used item (LRU algorithm)
    - you must print `DISCARD:` with the `key` discarded and following by a new line
- `def get(self, key):`
  - Must return the value in `self.cache_data` linked to `key`.
  - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
""" 3-main """
LRUCache = \_\_import\_\_('3-lru\_cache').LRUCache

my\_cache = LRUCache()
my\_cache.put("A", "Hello")
my\_cache.put("B", "World")
my\_cache.put("C", "Holberton")
my\_cache.put("D", "School")
my\_cache.print\_cache()
print(my\_cache.get("B"))
my\_cache.put("E", "Battery")
my\_cache.print\_cache()
my\_cache.put("C", "Street")
my\_cache.print\_cache()
print(my\_cache.get("A"))
print(my\_cache.get("B"))
print(my\_cache.get("C"))
my\_cache.put("F", "Mission")
my\_cache.print\_cache()
my\_cache.put("G", "San Francisco")
my\_cache.print\_cache()
my\_cache.put("H", "H")
my\_cache.print\_cache()
my\_cache.put("I", "I")
my\_cache.print\_cache()
my\_cache.put("J", "J")
my\_cache.print\_cache()
my\_cache.put("K", "K")
my\_cache.print\_cache()

guillaume@ubuntu:~/$ ./3-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: B
Current cache:
C: Street
F: Mission
G: San Francisco
H: H
DISCARD: C
Current cache:
F: Mission
G: San Francisco
H: H
I: I
DISCARD: F
Current cache:
G: San Francisco
H: H
I: I
J: J
DISCARD: G
Current cache:
H: H
I: I
J: J
K: K
guillaume@ubuntu:~/$
```

### 5.

Create a class `MRUCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
  - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
  - If `key` or `item` is `None`, this method should not do anything.
  - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
    - you must discard the most recently used item (MRU algorithm)
    - you must print `DISCARD:` with the `key` discarded and following by a new line
- `def get(self, key):`
  - Must return the value in `self.cache_data` linked to `key`.
  - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
""" 4-main """
MRUCache = \_\_import\_\_('4-mru\_cache').MRUCache

my\_cache = MRUCache()
my\_cache.put("A", "Hello")
my\_cache.put("B", "World")
my\_cache.put("C", "Holberton")
my\_cache.put("D", "School")
my\_cache.print\_cache()
print(my\_cache.get("B"))
my\_cache.put("E", "Battery")
my\_cache.print\_cache()
my\_cache.put("C", "Street")
my\_cache.print\_cache()
print(my\_cache.get("A"))
print(my\_cache.get("B"))
print(my\_cache.get("C"))
my\_cache.put("F", "Mission")
my\_cache.print\_cache()
my\_cache.put("G", "San Francisco")
my\_cache.print\_cache()
my\_cache.put("H", "H")
my\_cache.print\_cache()
my\_cache.put("I", "I")
my\_cache.print\_cache()
my\_cache.put("J", "J")
my\_cache.print\_cache()
my\_cache.put("K", "K")
my\_cache.print\_cache()

guillaume@ubuntu:~/$ ./4-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: B
Current cache:
A: Hello
C: Holberton
D: School
E: Battery
Current cache:
A: Hello
C: Street
D: School
E: Battery
Hello
None
Street
DISCARD: C
Current cache:
A: Hello
D: School
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
D: School
E: Battery
G: San Francisco
DISCARD: G
Current cache:
A: Hello
D: School
E: Battery
H: H
DISCARD: H
Current cache:
A: Hello
D: School
E: Battery
I: I
DISCARD: I
Current cache:
A: Hello
D: School
E: Battery
J: J
DISCARD: J
Current cache:
A: Hello
D: School
E: Battery
K: K
guillaume@ubuntu:~/$
```
