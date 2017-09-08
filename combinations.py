def combinations(numbers, idx, target, result, current=[]):
    # print(numbers, idx, target, current)
    if target == 0:
        result.append(current)
        return

    if idx >= len(numbers) or numbers[idx] > target:
        return

    # 1. Use this element
    cur = current.copy()
    cur.append(numbers[idx])
    combinations(numbers, idx+1, target-numbers[idx], result, cur)

    # 2. Not use this element. In this cae, we should skip all the same elements 
    # to avoid duplicates
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