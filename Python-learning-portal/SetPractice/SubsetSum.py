from itertools import combinations
def subset_sum_to_target(input_set, target_sum):
    elements = list(input_set)
    result = []
    for r in range(1, len(elements) + 1):
        for combo in combinations(elements, r):
            if sum(combo) == target_sum:
                result.append(set(combo))
    return result
num_set = {1, 2, 3, 4, 5}
print(subset_sum_to_target(num_set, 8))