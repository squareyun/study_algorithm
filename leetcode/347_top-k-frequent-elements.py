def max_heapify(A, i):
    l = i*2 + 1
    r = i*2 + 2
    if l < len(A) and A[l][0] > A[i][0]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r][0] > A[largest][0]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

# max-heap을 만드는 함수
def build_max_heap(A):
    for i in range(len(A) // 2 - 1, -1, -1):
        max_heapify(A, i)

# heap에 가장 루트 노드를 제거하고 반환하는 함수
def extract_max_heap(A):
    if len(A) == 0:
        return None
    A[0], A[-1] = A[-1], A[0] # 루트 노드와 리프 노드 교환
    ret = A.pop() # 원소 제거
    max_heapify(A, 0)
    return ret

import math

# heap에 원소를 넣는 함수
def insert_max_heap(A, x):
    A.append(x)
    
    i = len(A) - 1
    while i > 0:
        parent = calculate_parent(i)

        if A[i][0] > A[parent][0]:
            A[i], A[parent] = A[parent], A[i]
            i = parent
        else: break

# 부모노드의 idx를 계산하는 함수
def calculate_parent(i):
    if i % 2 == 0:
        parent = int(i / 2) - 1
    else:
        parent = math.floor(i / 2)
    return parent

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in nums:
            try:
                h[i] += 1
            except:
                h[i] = 1

        q = []
        for key, value in h.items():
            insert_max_heap(q, [value, key])

        ret = []
        for i in range(k):
            ret.append(extract_max_heap(q)[1])
        return ret

