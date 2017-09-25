#include<stdio.h>
#include<malloc.h>
struct list{
int data;
struct list *next;
};
struct stack{
   struct list *top;
   int capacity;
};
struct stack* initializeStack(int capacity){
    struct stack *s = (struct stack*)malloc(sizeof(struct stack));
    s->top = NULL;
    s->capacity = capacity;
    return s;
}
int countElements(struct list *node){
    int count = 0;
    while(node != NULL){
        //printf("sss%d\n", node->data);
        node = node->next;
        count++;
    }
    printf("count: %d", count);
    return count;
}
int isStackEmpty(struct list *head){
    if (head == NULL)
        return 1;
    else return 0;
}
int isStackOverflow(struct stack *s){
    int count = countElements(s->top);
    if(count > s->capacity)
        return 1;
    else return 0;
}
struct list* createNode()
{
    struct list *node = (struct list *)malloc(sizeof(struct list));
    node->data = -1;
    node->next = NULL;
}
struct list* push(struct stack *s, int data)
{
    struct list *newnode;
    if (!isStackOverflow(s)){
        newnode = createNode();
        newnode->data = data;
        if (s->top != NULL){
            newnode->next = s->top;
        }
        s->top = newnode;
    }else printf("Stack is full");
    return s->top;
}
struct list* pop(struct list *head){
    struct list *temp=head;
    if (isStackEmpty(head)){
        printf("Stack is Empty");
    }
    printf("Popped: %d\n", head->data);
    head = head->next;
    free(temp);
    return head;
}
void main()
{
    struct list *head = NULL;
    int a[] = {1,2,3,4,5,6,7};
    int i;
    struct stack *s = initializeStack(5);
    for(i=0;i<7;i++)
    {
        s->top = push(s, a[i]);
    }
    s->top = pop(s->top);
    s->top = pop(s->top);
}
