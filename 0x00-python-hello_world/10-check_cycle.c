#include "lists.h"

/**
 * check_cycle - C program that check cycle in a singly linked list
 * @list: pointer to header
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *A, *B;

	if (list == NULL)
		return (0);

	B = list;
	A = list->next;

	if (A == NULL)
		return (0);

	while (B != A)
	{
		if (A->next == NULL || A->next->next == NULL)
			return (0);
		B = B->next;
		A = A->next->next;
	}
	return (1);
}
