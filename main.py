from Abstract import sack
from Abstract import item
import random

random.seed()
# import algorithm

def main():
    s1 = sack.Sack()
    print(s1.max_capacity)
    items = []
    i1 = item.Item('Test', 5, 10)
    items = {'1': i1}

    print(random.random())

if __name__ == "__main__":
    main()