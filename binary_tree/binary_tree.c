#include <stdio.h>
#include <stdlib.h>
struct node
{
	int data;
	struct node *left;
	struct node *right;
};
struct node *create();
void print_tree(struct node *root, int level);
void free_tree(struct node *root);
int tree_hight(struct node *root);
int max(int a, int b);

int main()
{
    struct node *root;
    root = NULL;
    printf("Enter data or -1 for no node: ");
    root = create();
   
    printf("The tree hight is: %d\n", tree_hight(root));

    printf("Printing the tree:\n");
    print_tree(root, 0);
    free_tree(root);
    return 0;
}
struct node *create()
{
    int data;
    struct node *newNode;
    newNode = (struct node *)malloc(sizeof(struct node));
    if (!newNode)
        return NULL;

    scanf("%d", &data);
    if (data <= -1)
    {
        free(newNode);
        return NULL;
    }
    newNode->data = data;
    printf("Enter left child node for %d or -1 for no node: ", data);
    newNode->left = create();
    printf("Enter right child node for %d or -1 for node: ", data);
    newNode->right = create();

    return newNode;
}
void print_tree(struct node *root, int level)
{
    if (!root)
        return;

    print_tree(root->left, level + 1);

    for (int i = 0; i < level; i++)
        printf("        ");

    printf("[%d]--< \n", root->data);

    print_tree(root->right, level + 1);
}
void free_tree(struct node *root)
{
    if (!root)
        return;

    free_tree(root->left);
    free_tree(root->right);

    free(root);
}
int tree_hight(struct node *root)
{
    if (!root)
        return -1;
        int left_height = tree_hight(root->left);
        int right_height = tree_hight(root->right); 
    return (max(left_height, right_height) + 1);
}
int max(int a, int b)
{
    if (a > b)
         return a;
    else
        return b;
}