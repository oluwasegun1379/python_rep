#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct list_s
{
    char *str;
    unsigned int len;
    struct list_s *next;
} list_t;

void add_node(list_t **h, const char *string);
void print_li(list_t *h);
void free_list(list_t *h);

int main()
{
    list_t *h = NULL;

    add_node(&h, "Yusuf");
    add_node(&h, "Shakiru");
    add_node(&h, "Oluwasegun");

    print_li(h);
    free_list(h);

    return 0;
}
void add_node(list_t **h, const char *string)
{
    list_t *new_node = malloc(sizeof(list_t));
    if (new_node == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    new_node->str = strdup(string);
    if (new_node->str == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    new_node->len = strlen(string);
    new_node->next = NULL;

    if (*h == NULL)
    {
        *h = new_node;
    }
    else
    {
        list_t *temp = *h;
        while (temp->next != NULL)
        {
            temp = temp->next;
        }
        temp->next = new_node;
    }
}
void print_li(list_t *h)
{
    while (h != NULL)
    {
        printf("name = [%s], size = [%u]\n", h->str, h->len);
        h = h->next;
    }
}
void free_list(list_t *h)
{
    while (h != NULL)
    {
        list_t *temp = h;
        h = h->next;
        free(temp->str);
        free(temp);
    }
}
