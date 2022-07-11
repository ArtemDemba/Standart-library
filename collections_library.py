import collections


first_dict = {1: 1, 2: 2, 3: 3}
second_dict = {4: 4, 5: 5}

chain = collections.ChainMap(first_dict, second_dict)
second_dict[2] = 14
#print(2 in chain)

counter = collections.Counter([1, 2, 1, 2, 3, 6, 4, 7, 3])

#print(counter.most_common(4))
#print(counter)

default = collections.defaultdict(int)
primary_dict = {1: 1, 2: 2}
default[3] += 1
print(default)

