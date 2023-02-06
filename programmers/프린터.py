#TITLE: 프린터
#LEVEL: 2
#TAG: queue
#DATE: 20230206

from collections import deque

def solution(priorities, location):
    answer = 0
    
    q1 = deque(priorities)
    q2 = deque([x for x in range(len(priorities))])
    
    while len(q1) >= 0:
        priority = q1.popleft()
        loc = q2.popleft()
        
        if q1 and max(q1) > priority:
            q1.append(priority)
            q2.append(loc)
        else:
            answer += 1
            if loc == location:
                break

    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))