def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i, len(values)):
            denominator = values[j] - values[i]
            if denominator != 0:
                ratio = values[i] / denominator
                results.append((i, j, ratio))
            else:
                # Optionally, skip or handle division by zero
                results.append((i, j, None))
    return results

nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))
