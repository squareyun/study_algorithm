import math
import sys

sys.setrecursionlimit(10 ** 8) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

def makeSegTree(idx, start, end):
    if start == end: # 리프 노드
        seg[idx] = (arr[start], arr[start]) # 최소값, 최대값은 동일
        return seg[idx]
    
    mid = (start + end) // 2 # 몫 구하기

    left = makeSegTree(idx * 2, start, mid)
    right = makeSegTree(idx * 2 + 1, mid + 1, end)

    # 왼쪽과 오른쪽 중 각각 min, max 계산
    seg[idx] = (min(left[0], right[0]), max(left[1], right[1]))

    return seg[idx]

def find(idx, start, end):
    # 찾으려는 범위가 전혀 겹치지 않을 때
    if range2 < start or range1 > end:
        return (10**9+1, 0) # 최대 min 값, 최소 max 값 반환
    
    # 찾으려는 범위가 트리 범위에 속할 때
    if range1 <= start and end <= range2:
        return seg[idx]
    
    mid = (start + end) // 2
    left =  find(idx * 2, start, mid)
    right = find(idx * 2 + 1, mid + 1, end)
    return (min(left[0], right[0]), max(left[1], right[1]))

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)] # 이런 방식으로 입력받을 수 있다니

h = math.ceil(math.log2(n)) + 1 # 노드 개수에 따른 트리의 높이 계산 공식
nodeNum = 1 << h ## 2^h 계산
seg = [0 for _ in range(nodeNum)]
makeSegTree(1, 0, len(arr) - 1)

for _ in range(m):
    range1, range2 = map(int, input().split())
    range1, range2 = range1 - 1, range2 - 1 # index이므로 -1 해주기
    answer = find(1, 0, len(arr) - 1)
    print(answer[0], answer[1])