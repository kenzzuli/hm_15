from collections import Iterable

print(isinstance([], Iterable))  # True
print(isinstance({}, Iterable))  # True
print(isinstance(tuple(), Iterable))  # True
print(isinstance("abc", Iterable))  # True
print(isinstance(100, Iterable))  # False
