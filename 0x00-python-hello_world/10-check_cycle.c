#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: List to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *advanced = list;

	while (current && advanced && advanced->next)
	{
		current = current->next;
		advanced = advanced->next->next;
		if (current == advanced)
			return (1);
	}

	return (0);
}
