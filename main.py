from Abstract import sack
from Abstract import item

import random
import algorithm
random.seed()
# import algorithm

def main():
    s1 = sack.Sack()
    
    i1 = item.Item('Test1', 5, 10)
    i2 = item.Item('Test2', 2, 1)
    i3 = item.Item('Test3', 10, 30)
    i4 = item.Item('Test4', 8, 12)
    i5 = item.Item('Test5', 3, 3)

    items = []
    items.extend((i1, i2, i3, i4, i5))

    a1 = algorithm.Algorithm(s1, items)

    a1.performAlgorithm()

if __name__ == "__main__":
    main()