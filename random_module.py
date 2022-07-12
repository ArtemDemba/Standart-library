import random

print(random.randint(1, 100))   # Returns random int value from 1 to 100

print(random.random())          # Returns random float value from 0 to 1

print(random.uniform(1, 5))     # Returns random float value from 1 to 5

print(random.randrange(1, 10, 2))   # Returns random int value from 1 to 10 with step 2

print(random.gauss(0, 2))       # Returns rand float value with Normal distribution
                                # (expected value = 0, s = 2)

lst = [1, 2, 3, 4, 5]
print(random.choice(lst))       # Returns random element from iterable object

random.shuffle(lst)             # To shuffle iterable object
print(lst)

lst_1 = random.sample(lst, 3)   # Returns a list with 3 random elements from lst
print(lst_1)

random.seed(1)      # If we want to retrieve the same random values we can write it
                    # (argument - any natural number - grain)
