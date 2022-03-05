#include <stdio.h>
#define MIN(x,y)      ( (x)<(y)?(x):(y) )

int main() {
    int ableDistance, repairNum;
    int *distance, *repairTime;
    int *T, *P;

    /* input */
    scanf("%d %d", &ableDistance, &repairNum);
    distance = (int*)malloc(sizeof(int) * repairNum);
    repairTime = (int*)malloc(sizeof(int) * repairNum);
    T = (int*)malloc(sizeof(int) * (repairNum+1));
    P = (int*)malloc(sizeof(int) * (repairNum+1));
    for(int i=0; i<repairNum; i++)
        scanf("%d", &distance[i]);
    for(int i=0; i<repairNum; i++)
        scanf("%d", &repairTime[i]);

    T[0] = 0; P[0] = -1;
    for(int k=1; k <= repairNum + 1; k++) {
        int sum = 0;
        int min = 999999;
        for(int j=k-1; j>=0; j--) {
            sum += distance[j];
            if (sum > ableDistance) break;
            
            if(min > T)
            T[k] = MIN(T[j] + repairTime[k], min);
        }
    }
}