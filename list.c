#include<stdio.h>
#include<malloc.h>
struct node {
        int data;
        struct node *next;
};

typedef struct node node;

node *create(node *head);
int display(node * head);

int main(int argc, char *argv[]){
        int ch,n=0;

        node *head,*tail,*current;
        head=(node*)malloc(sizeof(node));
        tail= create(head);
        display(head);

        return 0;
}

node *create(node *curr){
        int data;
        node *next;
        printf("Enter the Data Value (Enter -1 to Finish Linked list): ");
        scanf("%d",&data);
        if(data !=-1)
        {
                printf("rrrrr");
                next=(node*)malloc(sizeof(node));
                next->data=data;
                curr->next=next; 
                create(next);
                printf("%d",next->data);
        }
        else
        {
                printf("NULL");
                curr->next=NULL;
                return curr;
        }


}

int display(node *curr){
        printf("ddd");
        node *node=curr->next;
        printf("sss");
        while (node->next!= NULL){
                printf("%d :: ",node->data);
                node = node->next;
                display(node);
        }
        return 0;
}
