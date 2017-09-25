#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
struct stack{
    int *data;
    int top;
    int capacity;
};
struct stack* createstack(int c){
    struct stack *s;
    s = (struct stack*)malloc(sizeof(struct stack));
    s->data=(int *)malloc(sizeof(int)*c);
    s->top=-1;
    s->capacity=c;
    return s;
}
struct stack* enqueue(int data,struct stack *s1, struct stack *s2){
    s2->top=-1;
    while(s1->top != -1)
        {
        s2->data[++s2->top]=s1->data[s1->top--];
    }
    s1->data[++s1->top]=data;
    while(s2->top != -1)
        {
        s1->data[++s1->top]=s2->data[s2->top--];
    }
    return s1;
}
void dequeue(struct stack *s1){
    if(s1->top != -1){
        s1->top--;
    }
}
int front(struct stack *s){
    if(s->top!=-1){
        return s->data[s->top];
    }
    return 0;
}
int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    struct stack *s1,*s2;
    int q,i,j,f,p[2];
    char temp;
    s1=createstack(q);
    s2=createstack(q);
    scanf("%d",&q);
    for(i=0;i<q;i++){
        j=0;
        do{
            scanf("%d", &p[j++]);
            scanf("%c", &temp);
        }while(temp != '\n');
        switch(p[0]){
        case 1:
        s1 = enqueue(p[1],s1,s2);
        break;
        case 2:
        dequeue(s1);
        //printf("%d\n",f);
        break;
        case 3:
        f=front(s1);
        printf("%d\n",f);
        break;
        }}
    return 0;
}

