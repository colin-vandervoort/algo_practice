# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    # Implement your solution here
    max_gap = 0
    binary_rep = bin(N)[2:]
    for left_idx, left_elem in enumerate(binary_rep):
        if left_elem == "1":
            right_idx = left_idx + 1
            while right_idx < len(binary_rep):
                if binary_rep[right_idx] == "1":
                    max_gap = max(max_gap, right_idx - left_idx - 1)
                    break
                right_idx += 1

    return max_gap
