#include<stdio.h>
#include<malloc.h>
int* rotate(int *a, int n){
    int temp = a[0];
    //for(int i=0;i<n-1;i++){
    //    a[i] = a[i+1];
    //}
    //a[n-1] = temp;
    a = &a[1];
    a[n-1]=temp;
    return a;
}
int main(){
    int n; 
    int k; 
    scanf("%d %d",&n,&k);
    int *a = malloc(sizeof(int) * n);
    for(int a_i = 0; a_i < n; a_i++){
       scanf("%d",&a[a_i]);
    }
    for(int a_i=0; a_i < k;a_i++){
        a = rotate(a, n);
    }
    for(int a_i=0; a_i < n; a_i++){
        printf("%d ",a[a_i]);
    }
    return 0;
}

