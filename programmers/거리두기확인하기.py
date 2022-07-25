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
            
            distance = abs(a[0][0]-a[1][0]) + abs(a[0][1]-a[1][1])
            if distance > 2:
                continue
            if distance == 1:
                answer.append(0)
                exitFlag = True
                break
            check = []
            if a[0][0] == a[1][0] or a[0][1] == a[1][1]:
                check.append(((a[0][0]+a[1][0])//2, (a[0][1]+a[1][1])//2))
            else:
                if a[0][1] > a[1][1]:
                    check.append((min(a[0][0],a[1][0]),min(a[0][1],a[1][1])))
                    check.append((max(a[0][0],a[1][0]),max(a[0][1],a[1][1])))
                elif a[0][1] < a[1][1]:
                    check.append((max(a[0][0],a[1][0]),min(a[0][1],a[1][1])))
                    check.append((min(a[0][0],a[1][0]),max(a[0][1],a[1][1])))

            for c in check:
                if place[c[0]][c[1]] == 'O':
                    answer.append(0)
                    exitFlag = True
                    break
        if not exitFlag:
            answer.append(1)
    
    return answer