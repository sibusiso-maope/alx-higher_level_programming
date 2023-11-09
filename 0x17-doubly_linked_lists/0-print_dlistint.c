#include "lists.h"

/**
 * print_dlistint - prints all  the elements
 * dlistint list
 *
 * @h: head of the list
 * Return number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	int args;

	args = 0;

	if (h == NULL)
		return (args);

	while (h->prev != NULL)
		h = h->prev;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		args++;
		h = h->next;
	}

	return (args);
}
