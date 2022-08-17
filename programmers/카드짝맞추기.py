# TITLE: 카드 짝 맞추기 (https://school.programmers.co.kr/learn/courses/30/lessons/72415)
# TAG: kakao, bruteforce, bfs
# DATE: 20220817
# AUTHOR: squareyun
# REFERENCE: https://www.youtube.com/watch?v=Q4bTSdi1psw&ab_channel=ezsw

from collections import deque

Board = []
cards = {}
Allremoved = 1 #카드가 삭제되었는지를 비트 연산자를 통해 확인
MinCnt = 987654321 #최소 조작 횟수
D = ((-1,0),(1,0),(0,-1),(0,1)) #상하좌우

def check(x,y):
    return x<0 or x>3 or y<0 or y>3

def bfs(removed, src, dst):
    visited = [[False for _ in range(4)] for _ in range(4)]
    q = deque([])
    q.append(src)
    while q:
        cur = q.popleft()
        if cur[0] == dst[0] and cur[1] == dst[1]:
            return cur[2]
        
        for i in range(4):
            nr = cur[0] + D[i][0]
            nc = cur[1] + D[i][1]
            if check(nr,nc):
                continue
            if not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr,nc,cur[2]+1))
            
            #ctrl + 방향키는 이미 한칸 움직인 상태에서 최대 2번 이동 가능
            for _ in range(2):
                if (removed & 1 << Board[nr][nc]) == 0: #카드를 만날 경우
                    break
                if check(nr+D[i][0], nc+D[i][1]):
                    break
                nr += D[i][0]
                nc += D[i][1]
            
            if not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr,nc,cur[2]+1))

    return 987654321

def permutate(cnt, removed, src): #조작 횟수, 삭제된 카드, 현재 커서 위치
    global MinCnt

    if cnt >= MinCnt: #가지치기 (큰 값은 확인할 이유가 없음)
        return

    #종료 조건
    if removed == Allremoved:
        MinCnt = min(MinCnt, cnt)
        return
    
    for num, card in cards.items():
        if removed & 1 << num: #이미 삭제된 카드라면 스킵
            continue
            
        one = bfs(removed, src, card[0]) + bfs(removed, card[0], card[1]) + 2
        two = bfs(removed, src, card[1]) + bfs(removed, card[1], card[0]) + 2

        permutate(cnt+one, removed | 1 << num, card[1])
        permutate(cnt+two, removed | 1 << num, card[0])

def solution(board, r, c):
    global Board, cards, Allremoved
    Board = board

    for i in range(4):
        for j in range(4):
            num = Board[i][j]
            if num:
                Allremoved |= 1 << num
                if num in cards:
                    cards[num].append((i,j,0))
                else:
                    cards[num] = [(i,j,0)]
    
    permutate(0, 1, (r, c, 0))
    
    return MinCnt

print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]],0,1))