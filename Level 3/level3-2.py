import math
import sys


def np2g(x):
    ans = 1 if x == 0 else int(2 ** math.ceil(math.log(x, 2)))
    return ans, abs(x - ans)


def np2s(x):
    ans = 1 if x == 0 else int(2 ** math.floor(math.log(x, 2)))
    return ans, abs(x - ans)


mem = {}


def solution_util(n):
    # print(n)
    if n in mem:
        return mem.get(n)
    if n == 1 or n == 0:
        return 0

    g = np2g(n)
    s = np2s(n)

    if g[1] == 0:
        mem[g[0]] = int(math.log(g[0], 2))
        return mem[g[0]]

    if s[1] == 0:
        mem[s[0]] = int(math.log(s[0], 2))
        return mem[s[0]]

    mem[s[0]] = solution_util(s[0])
    mem[g[0]] = solution_util(g[0])

    if n % 2 == 1:
        mem[(n + 1) // 2] = solution_util((n + 1) // 2)
        mem[(n - 1) // 2] = solution_util((n - 1) // 2)
        p3 = min(mem[(n + 1) // 2], mem[(n - 1) // 2]) + 2
    else:
        mem[n // 2] = solution_util(n // 2)
        p3 = mem[n // 2] + 1

    return min(mem[s[0]] + s[1], mem[g[0]] + g[1], p3)


def solution(n):
    # Without this line, recursion depth limit of 1000 will be reached with big numbers.
    # unfortunately, this line was blacklisted by google
    # Solution: either tabulate this implementation, or use java.
    sys.setrecursionlimit(1500)
    return solution_util(int(n))


print(solution('15'))
# print(solution("8810822610936164971310313186837410979920845487103513753391774103243102068223177352981099669051998691571017216199257395100770106511811777970181031639433381503604515099981751017375420391010262899013210191009710751061310697915875296703511593837105386095035805664099443521005897473579112319491080101033829959826"))
