#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: list to check
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int buffer[2048];
	int i = 0;
	int j;
	int same = 1;

	listint_t *temp = *head;

	if (temp)
	{
		for (j = 0; temp; j++)
		{
			buffer[j] = temp->n;
			temp = temp->next;
		}

		for (j--; i <= j && j >= i && same == 1; i++, j--)
		{
			if (buffer[i] != buffer[j])
				same = 0;
		}

		return (same);
	}
	else
	{
		return (same);
	}
}
