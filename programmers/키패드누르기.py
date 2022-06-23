answer = ''
left = '*'
right = '#'

def solution(numbers, hand):
    mustL = [1, 4, 7]
    mustR = [3, 6, 9]

    weight = [['1', '2', '3'],['4', '5', '6'],['7', '8', '9'],['*', '0', '#']]

    for i in numbers:
        i = str(i)

        if int(i) in mustL:
            useL(i)
            continue
            
        if int(i) in mustR:
            useR(i)
            continue
        
        distL = distance(left, i, weight)
        distR = distance(right, i, weight)
        
        if distL > distR:
            useR(i)
        elif distR > distL:
            useL(i)
        else:
            if hand == 'left':
                useL(i)
            else: useR(i)
        
    return answer

def useL(i):
    global answer
    global left

    answer += 'L'
    left = i

def useR(i):
    global answer
    global right

    answer += 'R'
    right = i

# Manhattan Distance
def distance(a, b, weight):
    ax = ay = bx = by = 0
    
    for i, x in enumerate(weight):
        if a in x:
            ax = i
            ay = x.index(a)
            break
    
    for i, x in enumerate(weight):
        if b in x:
            bx = i
            by = x.index(b)
            break
    return abs(ax - bx) + abs(ay - by)