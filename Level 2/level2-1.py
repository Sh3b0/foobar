def solution(xs):
    neg = 0
    zer = 0
    for elem in xs:
        if elem < 0:
            neg += 1
        elif elem == 0:
            zer += 1

    if len(xs) == 1:  # special case 1
        return str(xs[0])

    if zer == len(xs):  # special case 2
        return "0"

    if neg == 1 and zer == len(xs) - 1:  # special case 3
        return "0"

    res = 1
    if neg % 2 == 0:  # even (including 0) negatives -> multiply all (except zeros)
        for i in xs:
            if i != 0:
                res *= i
    elif neg % 2 != 0:  # odd negatives -> multiply all (except max negative and zeros)
        mx = 0
        for i in xs:
            if i < 0 and mx == 0:  # initialize mx
                mx = i
            if i != 0:
                res *= i
                if i < 0:
                    mx = max(mx, i)
        res //= mx

    return str(res)


# tests
# print(solution([2**32, 2**32, 2**32, 2**32]))
# print(solution([2, 0, 2, 2, 0]))
# print(solution([1, 2, 0, 3]))
# print(solution([-1, -2, 0, 3]))
# print(solution([-1, 2, 0, 3]))
# print(solution([-1, -2, 0, -3]))
# print(solution([0, -1, 0, 0]))
# print(solution([-1, -1, 0, -1]))
# print(solution([0, 0, 0, 0]))
# print(solution([1, 2, 3, 4]))
# print(solution([-1]))
# print(solution([-2**444]))
