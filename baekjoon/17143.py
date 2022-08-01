# 낚시왕 (https://www.acmicpc.net/problem/17143)
R,C,m=map(int,input().split())
shark=[list(map(int,input().split())) for _ in range(m)]
dx=[0,-1,1,0,0] #위,아래,오른쪽,왼쪽
dy=[0,0,0,1,-1]
answer=0

def catch(col):
    global answer
    rmList=[]
    for i in shark:
        if i[1] == col:
            rmList.append(i)
    if len(rmList) == 0: return
    sorted(rmList,key=lambda x: x[0])
    target = rmList[0][4]
    answer += target
    for i in range(len(shark)):
        if shark[i][4] == target:
            shark.pop(i)
            return

def move():
    for i, a in enumerate(shark): #위치 업데이트
        r,c,s,d,z=a[0],a[1],a[2],a[3],a[4]
        nx=r+s*dx[d]
        ny=c+s*dy[d]

        if d == 1:
            t = s - (r-1)
            dir,move=divmod(t,(R-1))
            if dir % 2 == 0:
                nx=1+move
                shark[i][3] = 2 if R-1 != 1 else 1
            else:
                nx=R-move
                shark[i][3] = 2 if R-1 == 1 else 1
        elif d == 2:
            t = s - (R-r)
            dir,move=divmod(t,(R-1))
            if dir % 2 == 0:
                nx=R-move
                shark[i][3] = 1 if R-1 != 1 else 2
            else:
                nx=1+move
                shark[i][3] = 1 if R-1 == 1 else 2
        elif d == 3:
            t = s - (C-c)
            dir,move=divmod(t,(C-1))
            if dir % 2 == 0:
                ny=C-move
                shark[i][3] = 4 if C-1 != 1 else 3
            else:
                ny=1+move
                shark[i][3] = 4 if C-1 == 1 else 3
        elif d == 4:
            t = s - (c-1)
            dir,move=divmod(t,(C-1))
            if dir % 2 == 0:
                ny=1+move
                shark[i][3] = 3 if C-1 != 1 else 4
            else:
                ny=C-move
                shark[i][3] = 3 if C-1 == 1 else 4
        shark[i][0],shark[i][1]=nx,ny

    remove_list=[]
    for target in shark: #중복 상어 제거
        targetR,targetC=target[0],target[1]
        temp_remove_list=[target[4]] #상어의 크기를 저장할 리스트
        for temp in shark:
            if temp[4]==target[4]: continue
            tempR,tempC=temp[0],temp[1]
            if targetR==tempR and targetC==tempC: #위치가 같다면 크기값 넣기
                temp_remove_list.append(temp[4])
        if len(temp_remove_list) > 1:
            sorted(temp_remove_list)
            remove_list.extend(temp_remove_list[:-1]) #정렬 후 가장 큰값 빼고 넣기
    for i in remove_list:
        for j in range(len(shark)):
            if shark[j][4] == i:
                shark.pop(j)
                break
    
for col in range(1,C+1): #열 개수만큼 반복
    catch(col)
    move()

print(answer)