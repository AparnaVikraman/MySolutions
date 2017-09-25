#include<stdio.h>
#include<malloc.h>
struct stack{
    int data[10];
    int top;
};
struct stack* createstack(){
    struct stack *s;
    s = (struct stack*)malloc(sizeof(struct stack));
    s->top=-1;
    return s;
}
void push(int data, struct stack *s){
    //printf("%d",s->top);
    s->top++;
    s->data[s->top]=data;
}
void delete(struct stack *s){
    if(s->top != -1){
        s->top--;
    }
    else{
        printf("Stack Empty");
    }
}
int maximum(struct stack *s){
    int max=s->data[s->top],i;
    for(i=s->top;i>=0;--i){
        if(max<s->data[i])
            max=s->data[i];
    }
    return max;
}
int main(){
int n,i,max,j;
int p[2];
char temp;
struct stack *s=createstack();
scanf("%d",&n);
for(i=0;i<n;i++){
    j=0;
    //while(scanf("%d%c", &p[j++], &temp) == 1 && temp != '\n');
    //printf("%d %d %d\n",p[0],p[1],i);
    do{
        scanf("%d", &p[j++]);
        scanf("%c", &temp);
        //printf("%d %c", p[j-1],temp);
    }while(temp != '\n');
    switch(p[0]){
        case 1:
        push(p[1],s);
        break;
        case 2:
        delete(s);
        break;
        case 3:
        max=maximum(s);
        printf("%d",max);
        break;
    }
}
}
