#include <stdio.h>
#include <stdlib.h>
struct node
{
	int data;
	struct node *left;
	struct node *right;
};

struct node *create();
void print_post(struct node *root);
void free_tree(struct node *root);
void print_pre(struct node *root);
void print_in(struct node *root);

int main()
{
	struct node *root;
	root = NULL;

	root = create();
	printf("Printing the tree in In-order traversal:\n");
	print_in(root);

	printf("Printing the tree in Pre-order traversal:\n");
	print_pre(root);

	printf("Printing the tree in Post-order traversal:\n");
	print_post(root);

	free_tree(root);

	return 0;
}
struct node *create()
{
	int x;
	struct node *newNode;
	newNode = (struct node *)malloc(sizeof(struct node));
	if (!newNode)
		return NULL;

	printf("Enter data or enter -1 for no node: ");
	scanf("%d", &x);
	if (x == -1)
	{
		free(newNode);
		return NULL;
	}
	newNode->data = x;
	printf("Enter left child for %d: ", x);
	newNode->left = create();
	printf("Enter right child for %d: ", x);
	newNode->right = create();

	return newNode;
}
void print_post(struct node *root)
{
	if (root == NULL)
		return;

	print_post(root->left);
	print_post(root->right);

	printf("%d\n", root->data); // Print the data of the current node
}
void free_tree(struct node *root)
{
	if (root == NULL)
		return;

	free_tree(root->left);
	free_tree(root->right);

	free(root);
}
void print_pre(struct node *root)
{
	if (root == NULL)
		return;

	printf("%d\n", root->data);

	print_pre(root->left);
	print_pre(root->right);
}
void print_in(struct node *root)
{
	if (root == NULL)
		return;

	print_in(root->left);

	printf("%d\n", root->data);

	print_in(root->right);
}
