
# Corrected version of compute_ratios to avoid division by zero and improve clarity
def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            denominator = values[j] - values[i]
            if denominator != 0:
                ratio = values[i] / denominator
                results.append((i, j, ratio))
            else:
                results.append((i, j, None))  # or handle as you see fit
    return results

nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))
