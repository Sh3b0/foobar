def solution(s):
    n = len(s)
    for k in range(1, n+1):
        if n % k == 0:  # string can be divided into k equal parts
            begin = 0
            end = k
            res = []
            ans = n // k
            # print(res)
            while end <= n:
                res.append(s[begin:end])
                begin += k
                end += k
            
            if ''.join(res) == ans * res[0]:
                return ans


print(solution("abccbaabccba"))  # 2
