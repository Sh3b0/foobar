def solution(x, y):
    k = x + y - 2
    return str(x * (x + 1) // 2 + (k - x + 1) * (x + k) // 2)
