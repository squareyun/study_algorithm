import itertools
def solution(expression):
    answer = []
    
    operator = ["*", "+", "-"]
    for op in itertools.permutations(operator, 3):
        a = op[0]
        b = op[1]
        t_list = []
        for i in expression.split(a):
            t = []
            for j in i.split(b):
                t.append(f"({j})")
            t_list.append(f"({b.join(t)})")
        answer.append(abs(eval(a.join(t_list))))

    return max(answer)

print(solution("100-200*300-500+20"))

# 100-200 300-500+20
# 100-200 300-500 20
# (100-200) (300-500) (20)
# (100-200) (300-500)+(20)
# (100-200) ((300-500)+(20))
# (100-200)*((300-500)+(20))