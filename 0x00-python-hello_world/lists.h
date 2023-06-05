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
} listint_v;

size_t print_listint(const listint_v *h);
listint_v *add_nodeint(listint_v **head, const int n);
void free_listint(listint_v *head);
int check_cycle(listint_v *list);

#endif /* LISTS_H */
