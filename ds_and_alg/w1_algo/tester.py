import timeit
from collections import Counter
import random
import string

uncode_str = ''.join(random.choices(string.ascii_letters, k=100000))

def manual_count():
    counter_dict = {}
    for n in uncode_str:
        counter_dict[n] = counter_dict.get(n, 0) + 1
    return list(counter_dict.items())

def counter_version():
    counter_dict = Counter(uncode_str)
    return list(counter_dict.items())

print("Manual:", timeit.timeit(manual_count, number=10))
print("Counter:", timeit.timeit(counter_version, number=10))
# Manual: 0.0353
# Counter: 0.0248