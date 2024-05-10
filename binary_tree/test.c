#include <stdio.h>
#include <stdlib.h>

// Define a structure for the binary tree node
typedef struct Node {
    int data;
    struct Node* left;
    struct Node* right;
} Node;

// Function to create a new node
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Function to print a binary tree in a tree-like format
void printTree(Node* root) {
    if (root == NULL)
        return;

    printf("    %d\n", root->data);
    printf("   / \\\n");

    if (root->left != NULL || root->right != NULL) {
        if (root->left == NULL)
            printf("  /   ");
        else
            printf("  %d   ", root->left->data);

        if (root->right == NULL)
            printf("\\\n");
        else
            printf("%d\n", root->right->data);
    }

    printTree(root->left);
    printTree(root->right);
}

int main() {
    // Create a sample binary tree
    Node* root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);
    root->right->left = createNode(6);
    root->right->right = createNode(7);

    // Print the binary tree in tree-like format
    printf("Printing the binary tree in tree-like format:\n");
    printTree(root);

    // Free allocated memory
    // You should have a proper deallocation function for larger trees
    free(root->left->left);
    free(root->left->right);
    free(root->right->left);
    free(root->right->right);
    free(root->left);
    free(root->right);
    free(root);

    return 0;
}
