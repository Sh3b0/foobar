from fractions import Fraction
import numpy as np


def qr_decomposition(m):
    terminal = set()
    for i in range(len(m)):
        if sum(m[i]) == 0:
            terminal.add(i)
    R, Q = [], []
    for i in range(len(m)):
        if i in terminal:
            continue
        total = float(sum(m[i]))
        r, q = [], []
        for j in range(len(m[i])):
            if j in terminal:
                r.append(m[i][j] / total)
            else:
                q.append(m[i][j] / total)
        R.append(r)
        Q.append(q)
    return Q, R


def format_ans(dec):
    ans = []
    dens = []
    for num in dec:
        frac = Fraction(num).limit_denominator()
        ans.append(frac.numerator)
        dens.append(frac.denominator)
    lcd = 1
    for i in dens:
        lcd = np.lcm(lcd, i)
    for i in range(len(ans)):
        ans[i] *= int(lcd / dens[i])
    ans.append(lcd)
    return ans


# Ref. https://en.wikipedia.org/wiki/Absorbing_Markov_chain
def solution(m):
    if len(m) < 2:
        return [1, 1]
    Q, R = qr_decomposition(m)
    F = np.linalg.inv(np.subtract(np.identity(len(Q)), Q))
    FR = np.dot(F, R)
    return format_ans(FR[0])


print(solution(
    [
        [0, 1, 0, 0, 0, 1],  # s0, the initial state, goes to s1 and s5 with equal probability
        [4, 0, 0, 3, 2, 0],  # s1 can become s0, s3, or s4, but with different probabilities
        [0, 0, 0, 0, 0, 0],  # s2 is terminal, and unreachable (never observed in practice)
        [0, 0, 0, 0, 0, 0],  # s3 is terminal
        [0, 0, 0, 0, 0, 0],  # s4 is terminal
        [0, 0, 0, 0, 0, 0],  # s5 is terminal
    ]
))
