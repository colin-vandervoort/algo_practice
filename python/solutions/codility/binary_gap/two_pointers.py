# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    # Implement your solution here
    max_gap = 0
    binary_rep = bin(N)[2:]
    binary_rep_len = len(binary_rep)
    left = 0
    while left < binary_rep_len:
        if binary_rep[left] == "1":
            right = left + 2
            while right < binary_rep_len:
                if binary_rep[right] == "1":
                    max_gap = max(max_gap, right - left - 1)
                    left = right - 2
                    break
                right += 1
        left += 1

    return max_gap
