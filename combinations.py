# Note:
#     以下实现为基本方法，使用递归的方法。缺点是这样会涉及很多重复计算。
#     优化方法为：可以采用动态规划，以(idx, target)为key, 将对应结果保存下来，则下次再需要这个结果时，
# 可以直接返回，而不是重新计算一遍。
def combinations(numbers, idx, target, result, current=[]):
    '''
    Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. Each number in C may only be used once in the combination.
    '''
    if target == 0:
        result.append(current)
        return

    if idx >= len(numbers) or numbers[idx] > target:
        return

    # 1. Use this element
    cur = current.copy()
    cur.append(numbers[idx])
    combinations(numbers, idx+1, target-numbers[idx], result, cur)

    # 2. Not use this element.
    # In this case, we should skip all the same elements to avoid duplicates
    for i in range(idx+1, len(numbers)):
        if numbers[i] != numbers[idx]:
            combinations(numbers, i, target, result, current)
            break

if __name__ == '__main__':
    numbers = [10, 1, 2, 7, 6, 1, 5]
    result = []
    combinations(sorted(numbers), 0, 8, result)
    print(result)

    numbers = [1, 1, 1, 1,1,1,1,1,1,1, 1]
    result = []
    combinations(numbers, 0, 8, result)
    print(result)