#include "lists.h"
#include <stdbool.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - functions inside a sorted list.
 * @head: this is the pointer to the lists.
 * @n: this is the data to add.
 *
 * Return: returns pointer to new node
 */
listint_t *insert_node(listint_t **head, int n)
{
	listint_t *new, *tmp, *prev;

	if (!head)
		return (0);
	new = malloc(sizeof(*new));
	if (!new)
		return (0);
	new->n = n;
	if (!(*head))
	{
		*head = new;
		return (new);
	}
	tmp = prev = *head;
	while (tmp && tmp->n < n)
	{
		prev = tmp;
		tmp = tmp->next;
	}
	if (prev == tmp)
		*head = new;
	else
		prev->next = new;
	new->next = tmp;
	return (new);
}
