#ifndef LISTS_H
#define LISTS_H

#include <stdbool.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - function for the singly linked lists.
 * @n: integer.
 * @next: points to the next node.
 *
 * Description: singly linked list node structs.
 *
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);
listint_t *insert_node(listint_t **head, int number);

#endif
