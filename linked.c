#include<stdio.h>
#include<unistd.h>
#include<string.h>
#include<stdlib.h>
#include <stddef.h>
struct node {
	int data;
	struct node *next;
};

typedef struct node node;

node *create(node *head);
int display(node *head);

int main(int argc, char *argv[]){
	int ch,n=0;

	node *head,*tail,*current;
	head=(node*)malloc(sizeof(node));
	create(head);
	display(head);

	return 0;
}
	
node *create(node *curr){
	int data;
	node *tmp;
	printf("Enter the Data Value (Enter -1 to Finish Linked list): ");
	scanf("%d",&data);
	if(data !=-1)
	{
                curr->next=(node*)malloc(sizeof(node));
                curr->next->data=data;
                curr->next->next=NULL;
                //curr->next=tmp;
		//curr->data=data;
		//tmp=(node*)malloc(sizeof(node));
                //curr->next=tmp;
                //printf("%dsss",curr->data);
		create(curr->next);
                return;
                //printf("%d",curr->data);
                //return curr;
                
	}
	/*else
	{
                //printf("sss");
		curr->next=NULL;
		return curr;
	}*/
return 0;

}

int display(node *curr){
	node *tmp=curr;
        //printf("%p :: ",curr->next);
        if(tmp->next!=NULL){
        	printf("%d  ", tmp->data);
                tmp = tmp->next;
                display(tmp);
} 
}

int insert(int index,node *head){
	return 0;
}

