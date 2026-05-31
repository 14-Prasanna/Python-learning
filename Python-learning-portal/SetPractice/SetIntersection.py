# 3. Set Intersection Count
def set_intersection_count(sets):
    if not sets:
        return 0
    return len(sets[0].intersection(*sets[1:]))

all_sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
print(set_intersection_count(all_sets))