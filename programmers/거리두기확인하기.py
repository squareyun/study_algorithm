import itertools
def solution(places):
    answer = []
    
    for place in places:
        index = []
        exitFlag = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    index.append((i, j))
        for a in itertools.combinations(index, 2):
            if exitFlag: break
            
            if abs(a[0][0]-a[1][0]) + abs(a[0][1]-a[1][1]) > 2:
                continue
            check = []
            if a[0][0] == a[1][0]:
                for i in range(min(a[0][1],a[1][1]), max(a[0][1],a[1][1])):
                    check.append((a[0][0], i))
            elif a[0][1] == a[1][1]:
                for i in range(min(a[0][0],a[1][0]), max(a[0][0],a[1][0])):
                    check.append((i, a[0][1]))
            else:
                if a[0][1] > a[1][1]:
                    check.append((min(a[0][0],a[1][0]),min(a[0][1],a[1][1])))
                    check.append((max(a[0][0],a[1][0]),max(a[0][1],a[1][1])))
                elif a[0][1] < a[1][1]:
                    check.append((max(a[0][0],a[1][0]),min(a[0][1],a[1][1])))
                    check.append((min(a[0][0],a[1][0]),max(a[0][1],a[1][1])))

            print(a, check)
            for c in check:
                if place[c[0]][c[1]] == 'O':
                    answer.append(0)
                    exitFlag = True
                    break
        if not exitFlag:
            answer.append(1)
    
    return answer