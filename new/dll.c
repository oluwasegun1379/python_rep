#include <stdio.h>
#include <stdlib.h>
struct Node
{
	int data;
	struct Node* next;
	struct Node* prev;
};
struct Node* head; // Global variable - pointer to head node

struct Node* GetNewNode(int x);
void print();
void ReversePrint();

struct Node* GetNewNode(int x)
{
	struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

	newNode->data = x;
	newNode->prev = NULL;
	newNode->next = NULL;

	return (newNode);
}
void InsertAtHead(int x)
{
	struct Node* newNode = GetNewNode(x);
	if(head == NULL)
	{
		head = newNode;
		return;
	}
	head->prev = newNode;
	newNode->next = head;
	head = newNode;
}
void print()
{
	struct Node* temp = head;
	printf("Forward: ");
	while (temp != NULL)
	{
		printf("%d ", temp->data);
		temp = temp->next;
	}
	printf("\n");
}
void ReversePrint()
{
	struct Node* temp = head;
	if (temp == NULL) return;

	while (temp->next != NULL)
		temp = temp->next;


	printf("Reverse: ");
	while (temp != NULL)
	{
		printf("%d ", temp->data);
		temp = temp->prev;
	}
	printf("\n");
}
int main()
{
	head = NULL;
	InsertAtHead(2); print(); ReversePrint();
	InsertAtHead(4); print(); ReversePrint();
	InsertAtHead(6); print(); ReversePrint();

	return (0);
}
