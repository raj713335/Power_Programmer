
bag = {}

for i in range(int(input())):
    value = int(input())
    if value not in bag.keys():
        bag[value] = 1
    else:
        bag[value] += 1

items_removed = int(input())

different_items = len(bag)
print(bag)
for each in sorted(bag.values()):
    if each <= items_removed:
        print(each)
        items_removed -= each
        different_items -= 1


print(different_items)

"""
4
1
1
1
1
2
"""

# OUTPUT 1


"""
6
1
2
3
1
2
2
2
"""

# Initially, ids = [1,2,3,1,2,2]. 3 items can be deleted and it is optimal to choose items having IDs 1 and 3.
# The final bag contains 3 items, all with ID 2.
