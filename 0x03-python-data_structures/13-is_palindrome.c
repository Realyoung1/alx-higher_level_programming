#include "lists.h"

#include <stdbool.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - function to chek if a list is palindrome.
 * Description:
 * The approach uses the fact that the list
 * - is palindrom if:
 *   the first half is same as the reverse
 *   of its last halfs
 * - else its not a palindrom if
 * The middle elments is found using the
 * tortoise hare algorithms
 * In the case where the list has odd length
 * the middle elments is disregarded.
 *
 * @list: pointer to list
 * Return: 1 if true 0 otherwise
 */

int is_palindrome(listint_t **list)
{
	int result = 1;
	listint_t *fast, *slow, *h1, *h2, *tmp;

	if (!list)
		return (0);

	/* if list length is less than 2 */
	if (!(*list) || !((*list)->next))
		return (1);

	/* find the middle node */
	slow = fast = *list;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast)
		slow = slow->next;

	/* reverse the last half */
	h2 = reverse_listint(&slow);
	tmp = h2;

	/* compare the two halves */
	h1 = *list;
	while (h2)
	{
		if (h2->n != h1->n)
		{
			result = 0;
			break;
		}
		h1 = h1->next;
		h2 = h2->next;
	}

	/* rever the half back to original */
	reverse_listint(&tmp);
	return (result);
}

/**
 * reverse_listint - this function reverses a linked list
 * @h: head of the list.
 *
 * Return: pointer to the reversed
 */
listint_t *reverse_listint(listint_t **h)
{
	listint_t *tmp2, *tmp1;

	if (!h || !(*h))
		return (NULL);
	tmp1 = (*h)->next;
	(*h)->next = NULL;
	while (tmp1)
	{
		tmp2 = *h;
		*h = tmp1;
		tmp1 = (*h)->next;
		(*h)->next = tmp2;
	}
	return (*h);
}
