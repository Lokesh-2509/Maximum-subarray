def max_subarray_sum(A, B, C):
    max_sum = 0
    current_sum = 0
    left = 0
    for right in range(A):
        current_sum += C[right]
        while current_sum > B:
            current_sum -= C[left]
            left += 1
        max_sum = max(max_sum, current_sum)
    return max_sum
A1 = 5
B1 = 12
C1 = [2, 1, 3, 4, 5]
print(max_subarray_sum(A1, B1, C1))
A2 = 3
B2 = 1
C2 = [2, 2, 2]
print(max_subarray_sum(A2, B2, C2))
