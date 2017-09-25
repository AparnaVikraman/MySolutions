#include<stdio.h>
#include<malloc.h>
struct Node{
    int data;
    struct Node *prev;
    struct Node *next;
};
typedef struct Node node;
node* createNode(){
    printf("\ncreate");
    node *newnode = (node *)malloc(sizeof(node));
    newnode->prev = NULL;
    newnode->next = NULL;
    printf("\ncreated");
    return newnode;
}
node* SortedInsert(node *head, int data){
   node *newnode = createNode(), *temp;
   newnode->data = data;
   printf("\nentered data into newnode");
   if(head == NULL){
       //printf("%dss",newnode->data);
       head = newnode;
   }else{
       if(head->data > data){
           printf("\nhead->data:%d >data:%d",head->data, data);
           newnode->next=head;
           head->prev=newnode;
           head=newnode;
           return head;
       }
       temp = head->next;
       while(temp != NULL && temp->data < data){
          temp=temp->next;
       }
       if(temp->data > data){
           temp->prev->next = newnode;
           newnode->prev=temp->prev;
           temp->prev=newnode;
           newnode->next=temp;
       }else{
           temp->next=newnode;
           newnode->prev=temp;
       }
       }
   printf("%d", head->data);
   return head;
}
void print(node *head){
    node *temp = head;
    while(temp!=NULL){
        printf("%d", temp->data);
        temp=temp->next;
    }
}
int main(){
    int num, n,a,j;
    node *head = NULL;
    scanf("%d",&num);
    for(int i=0;i<num;i++){
        scanf(" %d",&n);
        for( j=0;j<n;j++)
        {
            scanf("%d",&a);
            printf("%d",a);
            head = SortedInsert(head, a);
            printf("\nend");
        }
        printf("\nprinting head");
        print(head);
    }
}
