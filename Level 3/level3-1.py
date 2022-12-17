def solution(a, b):
    a, b = int(a), int(b)
    c = 0
    while min(a, b) != 1:
        if max(a, b) % min(a, b) == 0:
            return "impossible"

        c += max(a, b) // min(a, b)
        a, b = max(a, b) % min(a, b), min(a, b)
    return str(c + max(a, b) - 1)

