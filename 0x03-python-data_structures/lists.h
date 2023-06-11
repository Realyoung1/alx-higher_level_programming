#ifndef LIST_H
#define LIST_H

#include <stdbool.h>
#include <unistd.h>
#include <stdio.h>
#include<stdlib.h>

/**
 * struct listint_s - function of singly linked list.
 * @n: the int value stored.
 * @next: the points to the next node.
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
listint_t *insert_node(listint_t **head, int number);
int is_palindrome(listint_t **head);
listint_t *reverse_listint(listint_t **h);

#endif
