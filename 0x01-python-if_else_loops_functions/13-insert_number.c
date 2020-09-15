#include "lists.h"


/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: list where new node will be inserted
 * @number: node value
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *previous;
	listint_t *new_node;
	unsigned int first;

	first = 1;
	current = *head;
	previous = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
		return (*head = new_node);

	while (current != NULL)
	{
		if (number == current->n)
		{
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		else if (number < current->n)
		{
			if (first)
			{
				new_node->next = current;
				return (*head = new_node);
			}
			else
			{
				new_node->next = current;
				previous->next = new_node;
				return (new_node);
			}
		}
		
		previous = current;
		current = current->next;
		first = 0;
	}

	previous->next = new_node;
	return (new_node);
}
