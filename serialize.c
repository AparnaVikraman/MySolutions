#include<stdio.h>
#include<malloc.h>
#define MARKER -1
struct Node
{
    int key;
    struct Node* left, *right;
};

struct Node* newNode(int key)
{
    struct Node *temp=(struct Node*)malloc(sizeof(struct Node));
    temp->key = key;
    temp->left = temp->right = NULL;
    return (temp);
}

void serialize(struct Node *root, FILE *fp){
    if(root == NULL){
        fprintf(fp, "-1 ");
        return;
    }
    fprintf(fp, "%d ", root->key);
    serialize(root->left, fp);
    serialize(root->right, fp);
}
struct Node* deserialize(struct Node *root, FILE *fp){
    int val;
    if( !fscanf(fp, "%d", &val) || val == MARKER)
        //printf("%d", val);
        return NULL;
    root = newNode(val);
    root->left = deserialize(root->left, fp);
    root->right = deserialize(root->right, fp);
    return root;
}
void inorder(struct Node *root)
{
    if (root)
    {
        inorder(root->left);
        printf("%d ", root->key);
        inorder(root->right);
    }
}
int main()
{
    FILE *fp = fopen("tree.txt","w");
    // Let us construct a tree shown in the above figure
    struct Node *root1 = NULL;
    struct Node *root        = newNode(20);
    root->left               = newNode(8);
    root->right              = newNode(22);
    root->left->left         = newNode(4);
    root->left->right        = newNode(12);
    root->left->right->left  = newNode(10);
    root->left->right->right = newNode(14);
    if(fp == NULL){
        printf("Error");
        return 0;
    }
    serialize(root, fp);
    fclose(fp);

    fp = fopen("tree.txt","r");
    root1 = deserialize(root1, fp);
    inorder(root1);
}
