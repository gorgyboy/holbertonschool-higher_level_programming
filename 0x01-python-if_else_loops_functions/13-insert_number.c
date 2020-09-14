#include "lists.h"


/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: list where new node will be inserted
 * @number: node value
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *prev;
	listint_t *new_node;

	temp = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
		return (*head = new_node);
	while (temp != NULL)
	{
		if (temp->n < number)
		{
			prev = temp;
			temp = temp->next;
		}
		else if (temp->n == number)
		{
			return (NULL);
		}
		else if (temp->n > number)
		{
			new_node->next = temp;
			return (*head = new_node);
		}
		else
		{
			new_node->next = prev->next;
			prev->next = new_node;
			return (new_node);
		}
	}
	prev->next = new_node;
	return (new_node);
}
