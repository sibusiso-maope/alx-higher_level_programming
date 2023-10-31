#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: list head
 * @number: number to store in the new node
 * Return: pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node;
	listint_t *new_node;

	current_node = *head;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (current_node->next != NULL)
	{
		if ((current_node->next)->n >= number)
		{
			new_node->next = current_node->next;
			current_node->next = new_node;
			return (new_node);
		}
		current_node = current_node->next;
	}

	new_node->next = NULL;
	current_node->next = new_node;
	return (new_node);
}
