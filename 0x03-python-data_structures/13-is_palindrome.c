#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 *
 * @head: The first item oin the list
 *
 * Return: (int) 1 if it's a palindrome, 0 if it isn't
 */

int is_palindrome(listint_t **head)
{
	int i, list_size = 0, list_len;
	listint_t *temp, *list;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	temp = *head;
	while (temp != NULL)
	{
		list_size++;
		temp = temp->next;
	}
	list = *head;
	temp = *head;
	list_len = (list_size * 2) - 2;
	for (i = 0; 1 < list_len; i += 2, list_len -= 2)
	{
		if (temp[i].n != list[list_len].n)
			return (0);
	}
	return (1);
}
